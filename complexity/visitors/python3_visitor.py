from complexity.parsers.python3.Python3Parser import Python3Parser
from complexity.parsers.python3.Python3Visitor import Python3Visitor
from complexity.visitors.base_visitor import BaseVisitor


# CONDITIONALS = ('Compare', 'Try', 'ExceptHandler')
# BRANCHES = ('If', 'While', 'For', 'Raise', 'Break', 'cond', 'iter', 'Call', 'In')


class Python3CustomVisitor(Python3Visitor, BaseVisitor):
    ASSIGNMENTS = (
        # Occurrence of an assignment operator (=, +=, -=, *=, @=, /=, %=, &=, |=, ^=, <<=, >>=, **=, //=).
        # Python3Parser.RULE_assign,
        Python3Parser.RULE_augassign,
        # Occurrence of an increment or a decrement operator (++, --).
        # Python3Parser.RULE_unaryIncDecExpression,
    )

    BRANCHES = (
        # Occurrence of a function call.
        # Python3Parser.RULE_call,
        # Occurrence of any goto statement which has a target at a deeper level of nesting than the level to the goto.
        # Python3Parser.RULE_gotoStatement,
    )

    CONDITIONALS = (
        # Occurrence of a conditional operator (<, >, <=, >=, ==, !=).
        # Python3Parser.RULE_equalityExpression,
        # Python3Parser.RULE_relationalExpression,
        # Occurrence of the following keywords (‘else’, ‘case’, ‘default’, ‘?’).
        # Python3Parser.RULE_elseStatement,
        # Python3Parser.RULE_caseStatement,
        # Python3Parser.RULE_ternaryConditionalExpression,
        # Occurrence of a unary conditional operator.
        # Python3Parser.RULE_unaryConditionalExpression,
    )

    # Enter a parse tree produced by Python3Parser#assign.
    # def visitAssignOperator(self, ctx: Python3Parser.AssignContext):
    #     return self.process(ctx)

    # Enter a parse tree produced by Python3Parser#augassign.
    def visitAugassignOperator(self, ctx: Python3Parser.AugassignContext):
        return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#unaryIncDecExpression.
        # def visitUnaryIncDecExpression(self, ctx: Python3Parser.UnaryIncDecExpressionContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#call.
        # def visitCall(self, ctx: Python3Parser.CallContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#gotoStatement.
        # def visitGotoStatement(self, ctx: Python3Parser.GotoStatementContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#equalityExpression.
        # def visitEqualityExpression(self, ctx: Python3Parser.EqualityExpressionContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#relationalExpression.
        # def visitRelationalExpression(self, ctx: Python3Parser.RelationalExpressionContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#elseStatement.
        # def visitElseStatement(self, ctx: Python3Parser.ElseStatementContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#caseStatement.
        # def visitCaseStatement(self, ctx: Python3Parser.CaseStatementContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#ternaryConditionalExpression.
        # def visitTernaryConditionalExpression(self, ctx: Python3Parser.TernaryConditionalExpressionContext):
        #     return self.process(ctx)

        # Enter a parse tree produced by Python3Parser#unaryConditionalExpression.
        # def visitUnaryConditionalExpression(self, ctx: Python3Parser.UnaryConditionalExpressionContext):
        #     return self.process(ctx)
