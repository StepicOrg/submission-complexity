from complexity.parsers.python3.Python3Parser import Python3Parser
from complexity.parsers.python3.Python3Visitor import Python3Visitor
from complexity.visitors.base_visitor import BaseVisitor


class Python3CustomVisitor(Python3Visitor, BaseVisitor):
    ASSIGNMENTS = (
        # Occurrence of an assignment operator (=, +=, -=, *=, @=, /=, %=, &=, |=, ^=, <<=, >>=, **=, //=).
        Python3Parser.RULE_assign,
        Python3Parser.RULE_augassign,
    )

    BRANCHES = (
        # Occurrence of a function call.
        Python3Parser.RULE_call,
        # ('If', 'While', 'For', 'Raise', 'Break', 'cond', 'iter', 'In')
        Python3Parser.RULE_if_stmt,
        Python3Parser.RULE_while_stmt,
        Python3Parser.RULE_for_stmt,
        Python3Parser.RULE_raise_stmt,
        Python3Parser.RULE_break_stmt,
        Python3Parser.RULE_comp_iter,
    )

    CONDITIONALS = (
        # Occurrence of a conditional operator ('<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not').
        Python3Parser.RULE_comp_op,
        # Occurrence of the following keywords ('else', 'Try', 'ExceptHandler').
        Python3Parser.RULE_else_suite,
        Python3Parser.RULE_try_stmt,
        Python3Parser.RULE_except_clause,
    )

    def visitAssign(self, ctx: Python3Parser.AssignContext):
        return self.process(ctx)

    def visitAugassign(self, ctx: Python3Parser.AugassignContext):
        return self.process(ctx)

    def visitCall(self, ctx: Python3Parser.CallContext):
        return self.process(ctx)

    def visitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        return self.process(ctx)

    def visitWhile_stmt(self, ctx: Python3Parser.While_stmtContext):
        return self.process(ctx)

    def visitFor_stmt(self, ctx: Python3Parser.For_stmtContext):
        return self.process(ctx)

    def visitRaise_stmt(self, ctx: Python3Parser.Raise_stmtContext):
        return self.process(ctx)

    def visitBreak_stmt(self, ctx: Python3Parser.Break_stmtContext):
        return self.process(ctx)

    def visitComp_iter(self, ctx: Python3Parser.Comp_iterContext):
        return self.process(ctx)

    def visitComp_op(self, ctx: Python3Parser.Comp_opContext):
        return self.process(ctx)

    def visitOr_test(self, ctx: Python3Parser.Or_testContext):
        return self.process(ctx)

    def visitElse_suite(self, ctx: Python3Parser.Else_suiteContext):
        return self.process(ctx)

    def visitTry_stmt(self, ctx: Python3Parser.Try_stmtContext):
        return self.process(ctx)

    def visitExcept_clause(self, ctx: Python3Parser.Except_clauseContext):
        return self.process(ctx)
