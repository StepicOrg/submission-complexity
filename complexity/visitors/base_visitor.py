import math
from datetime import datetime, timedelta

from antlr4 import ParserRuleContext, ParseTreeVisitor


class BaseVisitor(ParseTreeVisitor):
    ASSIGNMENTS = []
    BRANCHES = []
    CONDITIONALS = []

    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.success = True

    @property
    def abc_score(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2), 2)

    def process(self, ctx: ParserRuleContext):
        rule = ctx.getRuleIndex()
        if rule in self.ASSIGNMENTS:
            self.a += 1
        elif rule in self.BRANCHES:
            self.b += 1
        elif rule in self.CONDITIONALS:
            self.c += 1

        return self.visitChildren(ctx)


class EmptyVisitor(object):
    def __init__(self):
        self.success = False

    @property
    def abc_score(self):
        return None
