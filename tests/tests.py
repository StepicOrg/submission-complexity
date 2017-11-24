import os
import unittest

from antlr4 import FileStream

from complexity.visitors.antlr_visitors import CPPABCVisitor, CABCVisitor, Python3ABCVisitor

tests = {
    CPPABCVisitor: (
        {
            'file': 'code/cpp/main.cpp',
            'a': 1,
            'b': 0,
            'c': 6,
            'score': 6.08
        },
        {
            'file': 'code/cpp/positives_negatives.cpp',
            'a': 14,
            'b': 4,
            'c': 125,
            'score': 125.85
        },
    ),
    CABCVisitor: (
        {
            'file': 'code/c/add.c',
            'a': 3,
            'b': 1,
            'c': 19,
            'score': 19.26
        },
        {
            'file': 'code/c/BinaryDigit.c',
            'a': 0,
            'b': 0,
            'c': 4,
            'score': 4
        },
        {
            'file': 'code/c/bt.c',
            'a': 7,
            'b': 8,
            'c': 76,
            'score': 76.74
        },
        {
            'file': 'code/c/dialog.c',
            'a': 0,
            'b': 5,
            'c': 34,
            'score': 34.37
        },
        {
            'file': 'code/c/helloworld.c',
            'a': 0,
            'b': 1,
            'c': 4,
            'score': 4.12
        },
        {
            'file': 'code/c/integrate.c',
            'a': 14,
            'b': 9,
            'c': 121,
            'score': 122.14
        },
        {
            'file': 'code/c/ll.c',
            'a': 8,
            'b': 2,
            'c': 33,
            'score': 34.01
        },
        {
            'file': 'code/c/pr403.c',
            'a': 0,
            'b': 2,
            'c': 10,
            'score': 10.2
        },
    ),
    Python3ABCVisitor: (
        {
            'file': 'code/python3/base_events.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/base_futures.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/base_subprocess.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/base_tasks.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/compat.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/constants.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/coroutines.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/events.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/futures.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/locks.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/log.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/proactor_events.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/protocols.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/queues.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/selector_events.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/sslproto.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/streams.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/subprocess.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/tasks.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/test_utils.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/transports.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/unix_events.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/windows_events.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
        {
            'file': 'code/python3/windows_utils.py',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0
        },
    )
}


class TestComplexity(unittest.TestCase):
    def _test(self, Visitor, test_set):
        for test in test_set:
            file = test['file']
            base_path = os.path.abspath(os.path.dirname(__file__))
            file_name = os.path.join(base_path, file)
            input = FileStream(file_name, encoding='utf8').strdata
            visitor = Visitor.from_code(input, time_limit=1)

            self.assertEqual(visitor.a, test['a'], f'a in {file}')
            self.assertEqual(visitor.b, test['b'], f'b in {file}')
            self.assertEqual(visitor.c, test['c'], f'c in {file}')
            self.assertEqual(visitor.abc_score, test['score'], f'score in {file}')

    def test_cpp(self):
        self._test(CPPABCVisitor, tests[CPPABCVisitor])

    def test_c(self):
        self._test(CABCVisitor, tests[CABCVisitor])

    def test_python3(self):
        self._test(Python3ABCVisitor, tests[Python3ABCVisitor])
