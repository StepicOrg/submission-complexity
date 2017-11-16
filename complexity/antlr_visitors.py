from datetime import datetime

from antlr4 import CommonTokenStream, PredictionMode, InputStream

from complexity.base_visitor import BaseVisitor
from complexity.parsers.cpp.CPP14Lexer import CPP14Lexer
from complexity.parsers.cpp.CPP14Parser import CPP14Parser
from complexity.parsers.cpp_visitor import Visitor


class ANTLRVisitor(object):
    Lexer = None
    Parser = None
    Visitor = None
    start_rule = None

    @classmethod
    def from_code(cls, code: str, time_limit: float = None, **kwargs) -> BaseVisitor:
        """

        :param code: Code for calculate ABC Score
        :param time_limit: max time for the calculation
        :param kwargs: other parameters
        :return: Visitor
        """
        start_time = datetime.now()
        input = InputStream(code)
        lexer = cls.Lexer(input)
        tokens = CommonTokenStream(lexer)

        parser = cls.Parser(tokens)
        parser._interp.predictionMode = PredictionMode.SLL

        try:
            tree = cls.start_rule(parser)
        except:
            tokens.reset()  # rewind
            parser.reset()
            parser._interp.predictionMode = PredictionMode.LL
            tree = cls.start_rule(parser)

        visitor = cls.Visitor(start_time, time_limit)
        visitor.visit(tree)

        return visitor


class CPPABCVisitor(ANTLRVisitor):
    Lexer = CPP14Lexer
    Parser = CPP14Parser
    Visitor = Visitor
    start_rule = CPP14Parser.translationunit
