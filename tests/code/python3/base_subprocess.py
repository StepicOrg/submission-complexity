import collections
import warnings

from . import compat
from . import transports
from .coroutines import coroutine
from .log import logger


class BaseSubprocessTransport(transports.SubprocessTransport):
    def __init__(self, loop, protocol, args, shell,
                 stdin, stdout, stderr, bufsize,
                 waiter=None, extra=None, **kwargs):
        super().__init__(extra)
        self._closed = False
        self._protocol = protocol
        self._loop = loop
        self._proc = None
        self._pid = None
        self._returncode = None
        self._exit_waiters = []
        self._pending_calls = collections.deque()
        self._pipes = {}
        self._finished = False

    def close(self):
        if self._closed:
            return
        self._closed = True

        for proto in self._pipes.values():
            if proto is None:
                continue
            proto.pipe.close()

        if (self._proc is not None
            # the child process finished?
            and self._returncode is None
            # the child process finished but the transport was not notified yet?
            and self._proc.poll() is None
            ):
            if self._loop.get_debug():
                logger.warning('Close running child process: kill %r', self)

            try:
                self._proc.kill()
            except ProcessLookupError:
                pass

                # Don't clear the _proc reference yet: _post_init() may still run

    # On Python 3.3 and older, objects with a destructor part of a reference
    # cycle are never destroyed. It's not more the case on Python 3.4 thanks
    # to the PEP 442.
    if compat.PY34:
        def __del__(self):
            if not self._closed:
                warnings.warn("unclosed transport %r" % self, ResourceWarning,
                              source=self)
                self.close()

    @coroutine
    def _connect_pipes(self, waiter):
        try:
            proc = self._proc
            loop = self._loop

            if proc.stdin is not None:
                _, pipe = yield from loop.connect_write_pipe(
                    lambda: WriteSubprocessPipeProto(self, 0),
                    proc.stdin)
                self._pipes[0] = pipe

            if proc.stdout is not None:
                _, pipe = yield from loop.connect_read_pipe(
                    lambda: ReadSubprocessPipeProto(self, 1),
                    proc.stdout)
                self._pipes[1] = pipe

            if proc.stderr is not None:
                _, pipe = yield from loop.connect_read_pipe(
                    lambda: ReadSubprocessPipeProto(self, 2),
                    proc.stderr)
                self._pipes[2] = pipe

            assert self._pending_calls is not None

            loop.call_soon(self._protocol.connection_made, self)
            for callback, data in self._pending_calls:
                loop.call_soon(callback, *data)
            self._pending_calls = None
        except Exception as exc:
            if waiter is not None and not waiter.cancelled():
                waiter.set_exception(exc)
        else:
            if waiter is not None and not waiter.cancelled():
                waiter.set_result(None)
