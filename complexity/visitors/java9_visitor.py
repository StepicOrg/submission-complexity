from complexity.parsers.java9.Java9Lexer import Java9Lexer
from complexity.parsers.java9.Java9Parser import Java9Parser
from complexity.parsers.java9.Java9Visitor import Java9Visitor
from complexity.visitors.antlr_visitor import ANTLRVisitor
from complexity.visitors.base_visitor import BaseVisitor


class Java9CustomVisitor(Java9Visitor, BaseVisitor):
    ASSIGNMENTS = (
        # Occurrence of an assignment operator (exclude constant declarations and default parameter assignments)
        # (=, *=, /=, %=, +=, -=, <<=, >>=, &=, |=, ^=, >>>=).
        Java9Parser.RULE_assignmentOperator,
        # Occurrence of an increment or a decrement operator (prefix or postfix) (++, --).
        Java9Parser.RULE_preIncrementDecrementExpression,
        Java9Parser.RULE_postIncrementDecrementExpression,
        Java9Parser.RULE_variableInitializer,
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
        Java9Parser.RULE_whileStatement,
        Java9Parser.RULE_whileStatementNoShortIf,
        Java9Parser.RULE_doStatement,
        Java9Parser.RULE_forStatement,
        Java9Parser.RULE_forStatementNoShortIf,
        Java9Parser.RULE_assertStatement,
        Java9Parser.RULE_breakAndContinueStatement,
        Java9Parser.RULE_returnStatement,
        Java9Parser.RULE_throwStatement,
        Java9Parser.RULE_synchronizedStatement,
        Java9Parser.RULE_ifStatement,
        Java9Parser.RULE_ifStatementNoShortIf,
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
        Java9Parser.RULE_switchStatement,
    )

    def visitAssignmentOperator(self, ctx: Java9Parser.AssignmentOperatorContext):
        return self.process(ctx)

    def visitPreIncrementDecrementExpression(self, ctx: Java9Parser.PreIncrementDecrementExpressionContext):
        return self.process(ctx)

    def visitPostIncrementDecrementExpression(self, ctx: Java9Parser.PostIncrementDecrementExpressionContext):
        return self.process(ctx)

    def visitVariableInitializer(self, ctx: Java9Parser.VariableInitializerContext):
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

    def visitWhileStatement(self, ctx: Java9Parser.WhileStatementContext):
        return self.process(ctx)

    def visitWhileStatementNoShortIf(self, ctx: Java9Parser.WhileStatementNoShortIfContext):
        return self.process(ctx)

    def visitDoStatement(self, ctx: Java9Parser.DoStatementContext):
        return self.process(ctx)

    def visitForStatement(self, ctx: Java9Parser.ForStatementContext):
        return self.process(ctx)

    def visitForStatementNoShortIf(self, ctx: Java9Parser.ForStatementNoShortIfContext):
        return self.process(ctx)

    def visitAssertStatement(self, ctx: Java9Parser.ComparisionContext):
        return self.process(ctx)

    def visitBreakAndContinueStatement(self, ctx: Java9Parser.BreakAndContinueStatementContext):
        return self.process(ctx)

    def visitReturnStatement(self, ctx: Java9Parser.ReturnStatementContext):
        return self.process(ctx)

    def visitThrowStatement(self, ctx: Java9Parser.ThrowStatementContext):
        return self.process(ctx)

    def visitSynchronizedStatement(self, ctx: Java9Parser.SynchronizedStatementContext):
        return self.process(ctx)

    def visitIfStatement(self, ctx: Java9Parser.IfStatementContext):
        return self.process(ctx)

    def visitIfStatementNoShortIf(self, ctx: Java9Parser.IfStatementNoShortIfContext):
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

    def visitSwitchStatement(self, ctx: Java9Parser.SwitchStatementContext):
        return self.process(ctx)


class Java9ABCVisitor(ANTLRVisitor):
    Lexer = Java9Lexer
    Parser = Java9Parser
    Visitor = Java9CustomVisitor
    start_rule = Java9Parser.compilationUnit
