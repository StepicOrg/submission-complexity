"""Synchronization primitives."""

__all__ = ['Lock', 'Event', 'Condition', 'Semaphore', 'BoundedSemaphore']

import collections

from . import events
from .coroutines import coroutine


class Lock():
    """Primitive lock objects.

    A primitive lock is a synchronization primitive that is not owned
    by a particular coroutine when locked.  A primitive lock is in one
    of two states, 'locked' or 'unlocked'.

    It is created in the unlocked state.  It has two basic methods,
    acquire() and release().  When the state is unlocked, acquire()
    changes the state to locked and returns immediately.  When the
    state is locked, acquire() blocks until a call to release() in
    another coroutine changes it to unlocked, then the acquire() call
    resets it to locked and returns.  The release() method should only
    be called in the locked state; it changes the state to unlocked
    and returns immediately.  If an attempt is made to release an
    unlocked lock, a RuntimeError will be raised.

    When more than one coroutine is blocked in acquire() waiting for
    the state to turn to unlocked, only one coroutine proceeds when a
    release() call resets the state to unlocked; first coroutine which
    is blocked in acquire() is being processed.

    acquire() is a coroutine and should be called with 'yield from'.

    Locks also support the context management protocol.  '(yield from lock)'
    should be used as the context manager expression.

    Usage:

        lock = Lock()
        ...
        yield from lock
        try:
            ...
        finally:
            lock.release()

    Context manager usage:

        lock = Lock()
        ...
        with (yield from lock):
             ...

    Lock objects can be tested for locking state:

        if not lock.locked():
           yield from lock
        else:
           # lock is acquired
           ...

    """

    def __init__(self, *, loop=None):
        self._waiters = collections.deque()
        self._locked = False
        if loop is not None:
            self._loop = loop
        else:
            self._loop = events.get_event_loop()

    def __repr__(self):
        res = super().__repr__()
        extra = 'locked' if self._locked else 'unlocked'
        if self._waiters:
            extra = '{},waiters:{}'.format(extra, len(self._waiters))
        return '<{} [{}]>'.format(res[1:-1], extra)

    def locked(self):
        """Return True if lock is acquired."""
        return self._locked

    @coroutine
    def acquire(self):
        """Acquire a lock.

        This method blocks until the lock is unlocked, then sets it to
        locked and returns True.
        """
        if not self._locked and all(w.cancelled() for w in self._waiters):
            self._locked = True
            return True

        fut = self._loop.create_future()
        self._waiters.append(fut)
        try:
            yield from fut
            self._locked = True
            return True
        finally:
            self._waiters.remove(fut)

    def release(self):
        """Release a lock.

        When the lock is locked, reset it to unlocked, and return.
        If any other coroutines are blocked waiting for the lock to become
        unlocked, allow exactly one of them to proceed.

        When invoked on an unlocked lock, a RuntimeError is raised.

        There is no return value.
        """
        if self._locked:
            self._locked = False
            # Wake up the first waiter who isn't cancelled.
            for fut in self._waiters:
                if not fut.done():
                    fut.set_result(True)
                    break
        else:
            raise RuntimeError('Lock is not acquired.')
