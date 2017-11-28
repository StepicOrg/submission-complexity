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
            'a': 206,
            'b': 361,
            'c': 171,
            'score': 449.44
        },
        {
            'file': 'code/python3/base_futures.py',
            'a': 15,
            'b': 14,
            'c': 7,
            'score': 21.68
        },
        {
            'file': 'code/python3/base_subprocess.py',
            'a': 47,
            'b': 44,
            'c': 43,
            'score': 77.42
        },
        {
            'file': 'code/python3/base_tasks.py',
            'a': 19,
            'b': 21,
            'c': 15,
            'score': 32.05
        },
        {
            'file': 'code/python3/compat.py',
            'a': 4,
            'b': 3,
            'c': 3,
            'score': 5.83
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
            'b': 62,
            'c': 43,
            'score': 107.81
        },
        {
            'file': 'code/python3/events.py',
            'a': 54,
            'b': 108,
            'c': 23,
            'score': 122.92
        },
        {
            'file': 'code/python3/futures.py',
            'a': 70,
            'b': 79,
            'c': 36,
            'score': 111.52
        },
        {
            'file': 'code/python3/locks.py',
            'a': 52,
            'b': 60,
            'c': 26,
            'score': 83.55
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
            'b': 100,
            'c': 61,
            'score': 136.97
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
            'b': 33,
            'c': 12,
            'score': 41.98
        },
        {
            'file': 'code/python3/selector_events.py',
            'a': 135,
            'b': 208,
            'c': 156,
            'score': 292.96
        },
        {
            'file': 'code/python3/sslproto.py',
            'a': 98,
            'b': 115,
            'c': 64,
            'score': 164.09
        },
        {
            'file': 'code/python3/streams.py',
            'a': 91,
            'b': 126,
            'c': 56,
            'score': 165.21
        },
        {
            'file': 'code/python3/subprocess.py',
            'a': 52,
            'b': 29,
            'c': 33,
            'score': 68.07
        },
        {
            'file': 'code/python3/tasks.py',
            'a': 84,
            'b': 123,
            'c': 67,
            'score': 163.32
        },
        {
            'file': 'code/python3/test_utils.py',
            'a': 63,
            'b': 45,
            'c': 36,
            'score': 85.38
        },
        {
            'file': 'code/python3/transports.py',
            'a': 14,
            'b': 31,
            'c': 14,
            'score': 36.78
        },
        {
            'file': 'code/python3/unix_events.py',
            'a': 110,
            'b': 196,
            'c': 137,
            'score': 263.22
        },
        {
            'file': 'code/python3/windows_events.py',
            'a': 124,
            'b': 97,
            'c': 75,
            'score': 174.38
        },
        {
            'file': 'code/python3/windows_utils.py',
            'a': 51,
            'b': 47,
            'c': 41,
            'score': 80.57
        },
    ),
    Java9ABCVisitor: (
        {
            'file': 'code/java9/helloworld.java',
            'a': 0,
            'b': 1,
            'c': 0,
            'score': 1.0
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
            'a': 0,
            'b': 4,
            'c': 2,
            'score': 4.47
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
            visitor = visitor_class.from_code(input, time_limit=1)

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
