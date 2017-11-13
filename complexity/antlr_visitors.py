from antlr4 import CommonTokenStream, ParseTreeWalker, PredictionMode, InputStream

from .cpp.listener import Listener
from .cpp.parsers.CPP14Lexer import CPP14Lexer
from .cpp.parsers.CPP14Parser import CPP14Parser


class ANTLRVisitor(object):
    Lexer = None
    Parser = None
    Listener = None
    start_rule = None

    @classmethod
    def from_code(cls, code: str, **kwargs):
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

        listener = cls.Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener


class CPPABCVisitor(ANTLRVisitor):
    Lexer = CPP14Lexer
    Parser = CPP14Parser
    Listener = Listener
    start_rule = CPP14Parser.translationunit
