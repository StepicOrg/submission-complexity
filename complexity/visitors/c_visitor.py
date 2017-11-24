from complexity.parsers.c.CParser import CParser
from complexity.parsers.c.CVisitor import CVisitor
from complexity.visitors.base_visitor import BaseVisitor


class CCustomVisitor(CVisitor, BaseVisitor):
    ASSIGNMENTS = (
        # Occurrence of an assignment operator (=, *=, /=, %=, +=, <<=, >>=, &=, !=, ^=, |=).
        CParser.RULE_assignmentOperator,
        # Occurrence of an increment or a decrement operator (++, --).
        CParser.RULE_unaryIncDecExpression,
    )

    BRANCHES = (
        # Occurrence of a function call.
        CParser.RULE_call,
        # Occurrence of any goto statement which has a target at a deeper level of nesting than the level to the goto.
        CParser.RULE_gotoStatement,
    )

    CONDITIONALS = (
        # Occurrence of a conditional operator (<, >, <=, >=, ==, !=).
        CParser.RULE_equalityExpression,
        CParser.RULE_relationalExpression,
        # Occurrence of the following keywords (‘else’, ‘case’, ‘default’, ‘?’).
        CParser.RULE_elseStatement,
        CParser.RULE_caseStatement,
        CParser.RULE_ternaryConditionalExpression,
        # Occurrence of a unary conditional operator.
        CParser.RULE_unaryConditionalExpression,
    )

    # Enter a parse tree produced by CParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: CParser.AssignmentOperatorContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#unaryIncDecExpression.
    def visitUnaryIncDecExpression(self, ctx: CParser.UnaryIncDecExpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#call.
    def visitCall(self, ctx: CParser.CallContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#gotoStatement.
    def visitGotoStatement(self, ctx: CParser.GotoStatementContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#equalityExpression.
    def visitEqualityExpression(self, ctx: CParser.EqualityExpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#relationalExpression.
    def visitRelationalExpression(self, ctx: CParser.RelationalExpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#elseStatement.
    def visitElseStatement(self, ctx: CParser.ElseStatementContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#caseStatement.
    def visitCaseStatement(self, ctx: CParser.CaseStatementContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#ternaryConditionalExpression.
    def visitTernaryConditionalExpression(self, ctx: CParser.TernaryConditionalExpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CParser#unaryConditionalExpression.
    def visitUnaryConditionalExpression(self, ctx: CParser.UnaryConditionalExpressionContext):
        return self.process(ctx)
