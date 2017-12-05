import math
from datetime import datetime, timedelta

from antlr4 import ParserRuleContext, ParseTreeVisitor


class BaseVisitor(ParseTreeVisitor):
    ASSIGNMENTS = []
    BRANCHES = []
    CONDITIONALS = []

    def __init__(self, start_time=None, time_limit=None):
        self.a = 0
        self.b = 0
        self.c = 0
        if start_time and time_limit:
            self.max_datetime = start_time + timedelta(seconds=time_limit)
        else:
            self.max_datetime = None
        self.success = True

    @property
    def abc_score(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2), 2)

    def check_time_over(self):
        if self.max_datetime and datetime.now() > self.max_datetime:
            self.success = False
            return False
        return True

    def visitChildren(self, node):
        if not self.check_time_over():
            return
        return super(BaseVisitor, self).visitChildren(node)

    def process(self, ctx: ParserRuleContext):
        rule = ctx.getRuleIndex()
        if rule in self.ASSIGNMENTS:
            self.a += 1
        elif rule in self.BRANCHES:
            self.b += 1
        elif rule in self.CONDITIONALS:
            self.c += 1

        return self.visitChildren(ctx)
