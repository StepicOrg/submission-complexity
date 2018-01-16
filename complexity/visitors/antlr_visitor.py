from datetime import datetime, timedelta

from antlr4 import CommonTokenStream, PredictionMode, InputStream
from antlr4.error.Errors import CancellationException

from complexity.visitors.base_visitor import EmptyVisitor


class ParsingTask():
    def __init__(self, code: str, Lexer, Parser, Visitor, start_rule, time_limit):
        super().__init__()
        self.code = code
        self.Lexer = Lexer
        self.Parser = Parser
        self.Visitor = Visitor
        self.start_rule = start_rule
        self.parser = None
        self.visitor = EmptyVisitor()
        self.time_limit = timedelta(seconds=time_limit) if time_limit else None

    def run(self):
        due_date = datetime.now() + self.time_limit if self.time_limit else None
        input = InputStream(self.code)
        lexer = self.Lexer(input)
        tokens = CommonTokenStream(lexer)

        self.parser = self.Parser(tokens)
        self.parser.due_date = due_date
        self.parser._interp.predictionMode = PredictionMode.SLL

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
        task = ParsingTask(code, cls.Lexer, cls.Parser, cls.Visitor, cls.start_rule, time_limit)
        task.run()
        return task.visitor
