import threading

from antlr4 import CommonTokenStream, PredictionMode, InputStream
from antlr4.error.Errors import CancellationException

from complexity.parsers.c.CLexer import CLexer
from complexity.parsers.c.CParser import CParser
from complexity.parsers.cpp.CPP14Lexer import CPP14Lexer
from complexity.parsers.cpp.CPP14Parser import CPP14Parser
from complexity.parsers.java9.Java9Lexer import Java9Lexer
from complexity.parsers.java9.Java9Parser import Java9Parser
from complexity.parsers.python3.Python3Lexer import Python3Lexer
from complexity.parsers.python3.Python3Parser import Python3Parser
from complexity.visitors.base_visitor import EmptyVisitor
from complexity.visitors.c_visitor import CCustomVisitor
from complexity.visitors.cpp_visitor import CPP14CustomVisitor
from complexity.visitors.java9_visitor import Java9CustomVisitor
from complexity.visitors.python3_visitor import Python3CustomVisitor


class ParsingTask(threading.Thread):
    def __init__(self, code: str, Lexer, Parser, Visitor, start_rule):
        super().__init__()
        self.code = code
        self.Lexer = Lexer
        self.Parser = Parser
        self.Visitor = Visitor
        self.start_rule = start_rule
        self.parser = None
        self.visitor = EmptyVisitor()
        self.need_stop = False
        self.exception = None

    def check_exception(self):
        if self.exception:
            raise self.exception

    def stop(self):
        if self.parser:
            self.parser.stop = True
        self.need_stop = True

    def run(self):
        try:
            input = InputStream(self.code)
            lexer = self.Lexer(input)
            tokens = CommonTokenStream(lexer)

            self.parser = self.Parser(tokens)
            self.parser._interp.predictionMode = PredictionMode.SLL

            if self.need_stop:
                return

            try:
                try:
                    tree = self.start_rule(self.parser)
                except:
                    tokens.reset()  # rewind
                    self.parser.reset()
                    self.parser._interp.predictionMode = PredictionMode.LL
                    tree = self.start_rule(self.parser)
            except CancellationException:
                return
            self.visitor = self.Visitor()
            self.visitor.visit(tree)
        except Exception as e:
            self.exception = e


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
        task = ParsingTask(code, cls.Lexer, cls.Parser, cls.Visitor, cls.start_rule)
        task.start()
        task.join(time_limit)
        if task.is_alive():
            # Stop parsing
            # Do not trust the result
            # Raise exception if it was
            task.stop()
            task.join()
            task.check_exception()
            return EmptyVisitor()

        task.check_exception()
        return task.visitor


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
