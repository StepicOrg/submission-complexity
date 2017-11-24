import os
import unittest

from antlr4 import FileStream

from complexity.visitors.antlr_visitors import CPPABCVisitor, CABCVisitor

tests = (
    {
        'visitor': CPPABCVisitor,
        'file': 'code/cpp/main.cpp',
        'a': 1,
        'b': 0,
        'c': 6,
        'score': 6.08
    },
    {
        'visitor': CPPABCVisitor,
        'file': 'code/cpp/positives_negatives.cpp',
        'a': 14,
        'b': 4,
        'c': 125,
        'score': 125.85
    },
    {
        'visitor': CABCVisitor,
        'file': 'code/c/add.c',
        'a': 2,
        'b': 0,
        'c': 19,
        'score': 19.1
    },
    {
        'visitor': CABCVisitor,
        'file': 'code/c/BinaryDigit.c',
        'a': 0,
        'b': 0,
        'c': 4,
        'score': 4
    },
)


class TestComplexity(unittest.TestCase):
    def test_cpp(self):
        for test in tests:
            file = test['file']
            base_path = os.path.abspath(os.path.dirname(__file__))
            file_name = os.path.join(base_path, file)
            input = FileStream(file_name, encoding='utf8').strdata
            visitor = test['visitor'].from_code(input, time_limit=1)

            self.assertEqual(visitor.a, test['a'], f'a in {file}')
            self.assertEqual(visitor.b, test['b'], f'b in {file}')
            self.assertEqual(visitor.c, test['c'], f'c in {file}')
            self.assertEqual(visitor.abc_score, test['score'], f'score in {file}')
