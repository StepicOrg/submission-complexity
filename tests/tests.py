import os
import unittest

from antlr4 import FileStream

from complexity.visitors.antlr_visitors import CPPABCVisitor, CABCVisitor, Python3ABCVisitor, Java9ABCVisitor

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
            'a': 8,
            'b': 8,
            'c': 76,
            'score': 76.84
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
            'a': 9,
            'b': 2,
            'c': 33,
            'score': 34.26
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
            'a': 206,
            'b': 643,
            'c': 171,
            'score': 696.51
        },
        {
            'file': 'code/python3/base_futures.py',
            'a': 15,
            'b': 24,
            'c': 7,
            'score': 29.15
        },
        {
            'file': 'code/python3/base_subprocess.py',
            'a': 47,
            'b': 101,
            'c': 43,
            'score': 119.41
        },
        {
            'file': 'code/python3/base_tasks.py',
            'a': 19,
            'b': 37,
            'c': 15,
            'score': 44.22
        },
        {
            'file': 'code/python3/compat.py',
            'a': 4,
            'b': 4,
            'c': 3,
            'score': 6.4
        },
        {
            'file': 'code/python3/constants.py',
            'a': 2,
            'b': 0,
            'c': 0,
            'score': 2.0
        },
        {
            'file': 'code/python3/coroutines.py',
            'a': 77,
            'b': 111,
            'c': 43,
            'score': 141.77
        },
        {
            'file': 'code/python3/events.py',
            'a': 54,
            'b': 186,
            'c': 23,
            'score': 195.04
        },
        {
            'file': 'code/python3/futures.py',
            'a': 70,
            'b': 141,
            'c': 36,
            'score': 161.48
        },
        {
            'file': 'code/python3/locks.py',
            'a': 52,
            'b': 133,
            'c': 26,
            'score': 145.15
        },
        {
            'file': 'code/python3/log.py',
            'a': 1,
            'b': 1,
            'c': 0,
            'score': 1.41
        },
        {
            'file': 'code/python3/proactor_events.py',
            'a': 71,
            'b': 218,
            'c': 61,
            'score': 237.25
        },
        {
            'file': 'code/python3/protocols.py',
            'a': 1,
            'b': 0,
            'c': 0,
            'score': 1.0
        },
        {
            'file': 'code/python3/queues.py',
            'a': 23,
            'b': 81,
            'c': 12,
            'score': 85.05
        },
        {
            'file': 'code/python3/selector_events.py',
            'a': 135,
            'b': 457,
            'c': 156,
            'score': 501.41
        },
        {
            'file': 'code/python3/sslproto.py',
            'a': 98,
            'b': 189,
            'c': 64,
            'score': 222.31
        },
        {
            'file': 'code/python3/streams.py',
            'a': 91,
            'b': 228,
            'c': 56,
            'score': 251.8
        },
        {
            'file': 'code/python3/subprocess.py',
            'a': 52,
            'b': 78,
            'c': 33,
            'score': 99.38
        },
        {
            'file': 'code/python3/tasks.py',
            'a': 84,
            'b': 277,
            'c': 67,
            'score': 297.11
        },
        {
            'file': 'code/python3/test_utils.py',
            'a': 63,
            'b': 162,
            'c': 36,
            'score': 177.51
        },
        {
            'file': 'code/python3/transports.py',
            'a': 14,
            'b': 44,
            'c': 14,
            'score': 48.25
        },
        {
            'file': 'code/python3/unix_events.py',
            'a': 110,
            'b': 395,
            'c': 137,
            'score': 432.31
        },
        {
            'file': 'code/python3/windows_events.py',
            'a': 124,
            'b': 305,
            'c': 75,
            'score': 337.68
        },
        {
            'file': 'code/python3/windows_utils.py',
            'a': 51,
            'b': 88,
            'c': 41,
            'score': 109.66
        },
    ),
    Java9ABCVisitor: (
        {
            'file': 'code/java9/helloworld.java',
            'a': 0,
            'b': 1,
            'c': 1,
            'score': 1.41
        },
        {
            'file': 'code/java9/method.java',
            'a': 1,
            'b': 2,
            'c': 2,
            'score': 3.0
        },
        {
            'file': 'code/java9/module-info.java',
            'a': 0,
            'b': 0,
            'c': 0,
            'score': 0.0
        },
        {
            'file': 'code/java9/TryWithResourceDemo.java',
            'a': 1,
            'b': 4,
            'c': 4,
            'score': 5.74
        },
    )
}


class TestComplexity(unittest.TestCase):
    def _test(self, visitor_class):
        test_set = tests[visitor_class]
        for test in test_set:
            file = test['file']
            base_path = os.path.abspath(os.path.dirname(__file__))
            file_name = os.path.join(base_path, file)
            input = FileStream(file_name, encoding='utf8').strdata
            visitor = visitor_class.from_code(input)

            self.assertDictEqual({
                'file': file,
                'a': visitor.a,
                'b': visitor.b,
                'c': visitor.c,
                'score': visitor.abc_score
            }, test, file)
            print('.', flush=True, end='')

    def test_cpp(self):
        self._test(CPPABCVisitor)

    def test_c(self):
        self._test(CABCVisitor)

    def test_python3(self):
        self._test(Python3ABCVisitor)

    def test_java9(self):
        self._test(Java9ABCVisitor)
