import os
import unittest

from antlr4 import FileStream

from complexity.visitors.antlr_visitors import CPPABCVisitor

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
        'a': 9,
        'b': 4,
        'c': 125,
        'score': 125.39
    },
)


class TestComplexity(unittest.TestCase):
    def test_cpp(self):
        for test in tests:
            base_path = os.path.abspath(os.path.dirname(__file__))
            file_name = os.path.join(base_path, test['file'])
            input = FileStream(file_name, encoding='utf8').strdata
            visitor = test['visitor'].from_code(input, time_limit=1)

            self.assertEqual(visitor.a, test['a'])
            self.assertEqual(visitor.b, test['b'])
            self.assertEqual(visitor.c, test['c'])
            self.assertEqual(visitor.abc_score, test['score'])
