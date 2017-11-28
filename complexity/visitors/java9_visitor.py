from complexity.parsers.java9.Java9Parser import Java9Parser
from complexity.parsers.java9.Java9Visitor import Java9Visitor
from complexity.visitors.base_visitor import BaseVisitor


# Occurrence of a unary conditional operator.

class Java9CustomVisitor(Java9Visitor, BaseVisitor):
    ASSIGNMENTS = (
        # Occurrence of an assignment operator (exclude constant declarations and default parameter assignments)
        # (=, *=, /=, %=, +=, -=, <<=, >>=, &=, |=, ^=, >>>=).
        Java9Parser.RULE_assignmentOperator,
        # Occurrence of an increment or a decrement operator (prefix or postfix) (++, --).
        Java9Parser.RULE_preIncrementExpression,
        Java9Parser.RULE_preDecrementExpression,
        Java9Parser.RULE_postIncrementExpression,
        Java9Parser.RULE_postDecrementExpression,
    )

    BRANCHES = (
        # Occurrence of a function call or a class method call.
        Java9Parser.RULE_methodInvocation,
        Java9Parser.RULE_methodInvocation_lf_primary,
        Java9Parser.RULE_methodInvocation_lfno_primary,
        # Occurrence of a ‘new’ operator.
        Java9Parser.RULE_arrayCreationExpression,
        Java9Parser.RULE_classInstanceCreationExpression,
        Java9Parser.RULE_classInstanceCreationExpression_lf_primary,
        Java9Parser.RULE_classInstanceCreationExpression_lfno_primary,
    )

    CONDITIONALS = (
        # Occurrence of a conditional operator (<, >, <=, >=, ==, !=).
        Java9Parser.RULE_comparision,
        Java9Parser.RULE_equalityExpression,
        # Occurrence of the following keywords (‘else’, ‘case’, ‘default’, ‘?’, ‘try’, ‘catch’).
        Java9Parser.RULE_elseStatement,
        Java9Parser.RULE_elseStatementNoShortIf,
        Java9Parser.RULE_switchLabel,
        Java9Parser.RULE_ternaryConditionalExpression,
        Java9Parser.RULE_tryStatement,
        Java9Parser.RULE_catchClause,

    )

    def visitAssignmentOperator(self, ctx: Java9Parser.AssignmentOperatorContext):
        return self.process(ctx)

    def visitPreIncrementExpression(self, ctx: Java9Parser.PreIncrementExpressionContext):
        return self.process(ctx)

    def visitPreDecrementExpression(self, ctx: Java9Parser.PreDecrementExpressionContext):
        return self.process(ctx)

    def visitPostIncrementExpression(self, ctx: Java9Parser.PostIncrementExpressionContext):
        return self.process(ctx)

    def visitPostDecrementExpression(self, ctx: Java9Parser.PostDecrementExpressionContext):
        return self.process(ctx)

    def visitMethodInvocation(self, ctx: Java9Parser.MethodInvocationContext):
        return self.process(ctx)

    def visitMethodInvocation_lf_primary(self, ctx: Java9Parser.MethodInvocation_lf_primaryContext):
        return self.process(ctx)

    def visitMethodInvocation_lfno_primary(self, ctx: Java9Parser.MethodInvocation_lfno_primaryContext):
        return self.process(ctx)

    def visitArrayCreationExpression(self, ctx: Java9Parser.ArrayCreationExpressionContext):
        return self.process(ctx)

    def visitClassInstanceCreationExpression(self, ctx: Java9Parser.ClassInstanceCreationExpressionContext):
        return self.process(ctx)

    def visitClassInstanceCreationExpression_lf_primary(self,
                                                        ctx: Java9Parser.ClassInstanceCreationExpression_lf_primaryContext):
        return self.process(ctx)

    def visitClassInstanceCreationExpression_lfno_primary(self,
                                                          ctx: Java9Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        return self.process(ctx)

    def visitComparision(self, ctx: Java9Parser.ComparisionContext):
        return self.process(ctx)

    def visitEqualityExpression(self, ctx: Java9Parser.EqualityExpressionContext):
        return self.process(ctx)

    def visitElseStatement(self, ctx: Java9Parser.ElseStatementContext):
        return self.process(ctx)

    def visitElseStatementNoShortIf(self, ctx: Java9Parser.ElseStatementNoShortIfContext):
        return self.process(ctx)

    def visitSwitchLabel(self, ctx: Java9Parser.SwitchLabelContext):
        return self.process(ctx)

    def visitTernaryConditionalExpression(self, ctx: Java9Parser.TernaryConditionalExpressionContext):
        return self.process(ctx)

    def visitTryStatement(self, ctx: Java9Parser.TryStatementContext):
        return self.process(ctx)

    def visitCatchClause(self, ctx: Java9Parser.CatchClauseContext):
        return self.process(ctx)
