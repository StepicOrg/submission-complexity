from multiprocessing import Process, Queue
from queue import Empty

from antlr4 import CommonTokenStream, PredictionMode, InputStream

from complexity.parsers.c.CLexer import CLexer
from complexity.parsers.c.CParser import CParser
from complexity.parsers.cpp.CPP14Lexer import CPP14Lexer
from complexity.parsers.cpp.CPP14Parser import CPP14Parser
from complexity.parsers.java9.Java9Lexer import Java9Lexer
from complexity.parsers.java9.Java9Parser import Java9Parser
from complexity.parsers.python3.Python3Lexer import Python3Lexer
from complexity.parsers.python3.Python3Parser import Python3Parser
from complexity.visitors.base_visitor import EmptyVisitor, BaseVisitor
from complexity.visitors.c_visitor import CCustomVisitor
from complexity.visitors.cpp_visitor import CPP14CustomVisitor
from complexity.visitors.java9_visitor import Java9CustomVisitor
from complexity.visitors.python3_visitor import Python3CustomVisitor


class ANTLRVisitor(object):
    Lexer = None
    Parser = None
    Visitor = None
    start_rule = None

    @classmethod
    def from_code(cls, code: str, time_limit: float = None, **kwargs):
        """

        :param code: Code for calculate ABC Score
        :param time_limit: max time for the calculation
        :param kwargs: other parameters
        :return: Visitor
        """
        q = Queue()
        process = Process(target=run, args=(q, code, cls.Lexer, cls.Parser,
                                            cls.Visitor, cls.start_rule))
        process.daemon = True
        process.start()
        process.join(time_limit)
        if process.is_alive():
            process.terminate()
            process.join()
            return EmptyVisitor()

        try:
            result = q.get(block=False)
        except Empty:
            return EmptyVisitor()

        cls.check_exception(result)
        if isinstance(result, BaseVisitor):
            return result
        return EmptyVisitor()

    @classmethod
    def check_exception(cls, exception):
        if isinstance(exception, Exception):
            raise exception


def run(q, code, Lexer, Parser, Visitor, start_rule):
    try:
        input = InputStream(code)
        lexer = Lexer(input)
        tokens = CommonTokenStream(lexer)

        parser = Parser(tokens)
        parser._interp.predictionMode = PredictionMode.SLL

        try:
            tree = start_rule(parser)
        except:
            tokens.reset()  # rewind
            parser.reset()
            parser._interp.predictionMode = PredictionMode.LL
            tree = start_rule(parser)
        visitor = Visitor()
        visitor.visit(tree)
        q.put(visitor, block=False)
    except Exception as e:
        q.put(e, block=False)


class CPPABCVisitor(ANTLRVisitor):
    Lexer = CPP14Lexer
    Parser = CPP14Parser
    Visitor = CPP14CustomVisitor
    start_rule = CPP14Parser.translationunit


class CABCVisitor(ANTLRVisitor):
    Lexer = CLexer
    Parser = CParser
    Visitor = CCustomVisitor
    start_rule = CParser.compilationUnit


class Python3ABCVisitor(ANTLRVisitor):
    Lexer = Python3Lexer
    Parser = Python3Parser
    Visitor = Python3CustomVisitor
    start_rule = Python3Parser.file_input


class Java9ABCVisitor(ANTLRVisitor):
    Lexer = Java9Lexer
    Parser = Java9Parser
    Visitor = Java9CustomVisitor
    start_rule = Java9Parser.compilationUnit
