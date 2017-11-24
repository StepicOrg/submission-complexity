import os
import unittest

from antlr4 import FileStream

from complexity.visitors.antlr_visitors import CPPABCVisitor, CABCVisitor

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
