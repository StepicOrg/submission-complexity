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
            'b': 434,
            'c': 171,
            'score': 509.93
        },
        {
            'file': 'code/python3/base_futures.py',
            'a': 15,
            'b': 18,
            'c': 7,
            'score': 24.45
        },
        {
            'file': 'code/python3/base_subprocess.py',
            'a': 47,
            'b': 61,
            'c': 43,
            'score': 88.2
        },
        {
            'file': 'code/python3/base_tasks.py',
            'a': 19,
            'b': 23,
            'c': 15,
            'score': 33.39
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
            'b': 96,
            'c': 43,
            'score': 130.36
        },
        {
            'file': 'code/python3/events.py',
            'a': 54,
            'b': 145,
            'c': 23,
            'score': 156.43
        },
        {
            'file': 'code/python3/futures.py',
            'a': 70,
            'b': 101,
            'c': 36,
            'score': 128.05
        },
        {
            'file': 'code/python3/locks.py',
            'a': 52,
            'b': 88,
            'c': 26,
            'score': 105.47
        },
        {
            'file': 'code/python3/log.py',
            'a': 1,
            'b': 0,
            'c': 0,
            'score': 1.0
        },
        {
            'file': 'code/python3/proactor_events.py',
            'a': 71,
            'b': 137,
            'c': 61,
            'score': 165.92
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
            'b': 50,
            'c': 12,
            'score': 56.33
        },
        {
            'file': 'code/python3/selector_events.py',
            'a': 135,
            'b': 278,
            'c': 156,
            'score': 346.19
        },
        {
            'file': 'code/python3/sslproto.py',
            'a': 98,
            'b': 147,
            'c': 64,
            'score': 187.91
        },
        {
            'file': 'code/python3/streams.py',
            'a': 91,
            'b': 173,
            'c': 56,
            'score': 203.34
        },
        {
            'file': 'code/python3/subprocess.py',
            'a': 52,
            'b': 42,
            'c': 33,
            'score': 74.55
        },
        {
            'file': 'code/python3/tasks.py',
            'a': 84,
            'b': 163,
            'c': 67,
            'score': 195.23
        },
        {
            'file': 'code/python3/test_utils.py',
            'a': 63,
            'b': 89,
            'c': 36,
            'score': 114.83
        },
        {
            'file': 'code/python3/transports.py',
            'a': 14,
            'b': 35,
            'c': 14,
            'score': 40.21
        },
        {
            'file': 'code/python3/unix_events.py',
            'a': 110,
            'b': 247,
            'c': 137,
            'score': 303.11
        },
        {
            'file': 'code/python3/windows_events.py',
            'a': 124,
            'b': 145,
            'c': 75,
            'score': 205.0
        },
        {
            'file': 'code/python3/windows_utils.py',
            'a': 51,
            'b': 55,
            'c': 41,
            'score': 85.48
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
