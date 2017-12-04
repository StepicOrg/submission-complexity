# Generated from complexity/grammars/Java9.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .Java9Parser import Java9Parser
else:
    from Java9Parser import Java9Parser


# This class defines a complete generic visitor for a parse tree produced by Java9Parser.

class Java9Visitor(ParseTreeVisitor):
    # Visit a parse tree produced by Java9Parser#referenceType.
    def visitReferenceType(self, ctx: Java9Parser.ReferenceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx: Java9Parser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classType.
    def visitClassType(self, ctx: Java9Parser.ClassTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#arrayType.
    def visitArrayType(self, ctx: Java9Parser.ArrayTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#dims.
    def visitDims(self, ctx: Java9Parser.DimsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#typeParameter.
    def visitTypeParameter(self, ctx: Java9Parser.TypeParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#typeArguments.
    def visitTypeArguments(self, ctx: Java9Parser.TypeArgumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#typeArgument.
    def visitTypeArgument(self, ctx: Java9Parser.TypeArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#compilationUnit.
    def visitCompilationUnit(self, ctx: Java9Parser.CompilationUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#packageDeclaration.
    def visitPackageDeclaration(self, ctx: Java9Parser.PackageDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#importDeclaration.
    def visitImportDeclaration(self, ctx: Java9Parser.ImportDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#typeDeclaration.
    def visitTypeDeclaration(self, ctx: Java9Parser.TypeDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#moduleDirective.
    def visitModuleDirective(self, ctx: Java9Parser.ModuleDirectiveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#normalClassDeclaration.
    def visitNormalClassDeclaration(self, ctx: Java9Parser.NormalClassDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classModifier.
    def visitClassModifier(self, ctx: Java9Parser.ClassModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#typeParameters.
    def visitTypeParameters(self, ctx: Java9Parser.TypeParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classBody.
    def visitClassBody(self, ctx: Java9Parser.ClassBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx: Java9Parser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#fieldModifier.
    def visitFieldModifier(self, ctx: Java9Parser.FieldModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#variableDeclaratorList.
    def visitVariableDeclaratorList(self, ctx: Java9Parser.VariableDeclaratorListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#variableDeclarator.
    def visitVariableDeclarator(self, ctx: Java9Parser.VariableDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#variableInitializer.
    def visitVariableInitializer(self, ctx: Java9Parser.VariableInitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#unannType.
    def visitUnannType(self, ctx: Java9Parser.UnannTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#unannClassType.
    def visitUnannClassType(self, ctx: Java9Parser.UnannClassTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#methodModifier.
    def visitMethodModifier(self, ctx: Java9Parser.MethodModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#formalParameterList.
    def visitFormalParameterList(self, ctx: Java9Parser.FormalParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#formalParameters.
    def visitFormalParameters(self, ctx: Java9Parser.FormalParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#formalParameter.
    def visitFormalParameter(self, ctx: Java9Parser.FormalParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#variableModifier.
    def visitVariableModifier(self, ctx: Java9Parser.VariableModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#lastFormalParameter.
    def visitLastFormalParameter(self, ctx: Java9Parser.LastFormalParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#throws_.
    def visitThrows_(self, ctx: Java9Parser.Throws_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#exceptionType.
    def visitExceptionType(self, ctx: Java9Parser.ExceptionTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#constructorModifier.
    def visitConstructorModifier(self, ctx: Java9Parser.ConstructorModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#explicitConstructorInvocation.
    def visitExplicitConstructorInvocation(self, ctx: Java9Parser.ExplicitConstructorInvocationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#enumDeclaration.
    def visitEnumDeclaration(self, ctx: Java9Parser.EnumDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#enumConstant.
    def visitEnumConstant(self, ctx: Java9Parser.EnumConstantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#normalInterfaceDeclaration.
    def visitNormalInterfaceDeclaration(self, ctx: Java9Parser.NormalInterfaceDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#interfaceModifier.
    def visitInterfaceModifier(self, ctx: Java9Parser.InterfaceModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx: Java9Parser.InterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#constantModifier.
    def visitConstantModifier(self, ctx: Java9Parser.ConstantModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#interfaceMethodModifier.
    def visitInterfaceMethodModifier(self, ctx: Java9Parser.InterfaceMethodModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx: Java9Parser.AnnotationTypeDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#annotationTypeMemberDeclaration.
    def visitAnnotationTypeMemberDeclaration(self, ctx: Java9Parser.AnnotationTypeMemberDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#annotation.
    def visitAnnotation(self, ctx: Java9Parser.AnnotationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#elementValue.
    def visitElementValue(self, ctx: Java9Parser.ElementValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#variableInitializerList.
    def visitVariableInitializerList(self, ctx: Java9Parser.VariableInitializerListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#blockStatement.
    def visitBlockStatement(self, ctx: Java9Parser.BlockStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#statement.
    def visitStatement(self, ctx: Java9Parser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#ifStatement.
    def visitIfStatement(self, ctx: Java9Parser.IfStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#whileStatement.
    def visitWhileStatement(self, ctx: Java9Parser.WhileStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#forStatement.
    def visitForStatement(self, ctx: Java9Parser.ForStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#statementNoShortIf.
    def visitStatementNoShortIf(self, ctx: Java9Parser.StatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#ifStatementNoShortIf.
    def visitIfStatementNoShortIf(self, ctx: Java9Parser.IfStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#whileStatementNoShortIf.
    def visitWhileStatementNoShortIf(self, ctx: Java9Parser.WhileStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#forStatementNoShortIf.
    def visitForStatementNoShortIf(self, ctx: Java9Parser.ForStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#statementWithoutTrailingSubstatement.
    def visitStatementWithoutTrailingSubstatement(self, ctx: Java9Parser.StatementWithoutTrailingSubstatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#synchronizedStatement.
    def visitSynchronizedStatement(self, ctx: Java9Parser.SynchronizedStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#assertStatement.
    def visitAssertStatement(self, ctx: Java9Parser.AssertStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#switchStatement.
    def visitSwitchStatement(self, ctx: Java9Parser.SwitchStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#doStatement.
    def visitDoStatement(self, ctx: Java9Parser.DoStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#breakAndContinueStatement.
    def visitBreakAndContinueStatement(self, ctx: Java9Parser.BreakAndContinueStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#returnStatement.
    def visitReturnStatement(self, ctx: Java9Parser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#throwStatement.
    def visitThrowStatement(self, ctx: Java9Parser.ThrowStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#statementExpression.
    def visitStatementExpression(self, ctx: Java9Parser.StatementExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#elseStatement.
    def visitElseStatement(self, ctx: Java9Parser.ElseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#elseStatementNoShortIf.
    def visitElseStatementNoShortIf(self, ctx: Java9Parser.ElseStatementNoShortIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#switchLabel.
    def visitSwitchLabel(self, ctx: Java9Parser.SwitchLabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#forInit.
    def visitForInit(self, ctx: Java9Parser.ForInitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#statementExpressionList.
    def visitStatementExpressionList(self, ctx: Java9Parser.StatementExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#tryStatement.
    def visitTryStatement(self, ctx: Java9Parser.TryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#catchClause.
    def visitCatchClause(self, ctx: Java9Parser.CatchClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#resource.
    def visitResource(self, ctx: Java9Parser.ResourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#primary.
    def visitPrimary(self, ctx: Java9Parser.PrimaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#primaryNoNewArray_lfno_arrayAccess.
    def visitPrimaryNoNewArray_lfno_arrayAccess(self, ctx: Java9Parser.PrimaryNoNewArray_lfno_arrayAccessContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#primaryNoNewArray_lfno_primary.
    def visitPrimaryNoNewArray_lfno_primary(self, ctx: Java9Parser.PrimaryNoNewArray_lfno_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classInstanceCreationExpression.
    def visitClassInstanceCreationExpression(self, ctx: Java9Parser.ClassInstanceCreationExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classInstanceCreationExpression_lf_primary.
    def visitClassInstanceCreationExpression_lf_primary(self,
                                                        ctx: Java9Parser.ClassInstanceCreationExpression_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#classInstanceCreationExpression_lfno_primary.
    def visitClassInstanceCreationExpression_lfno_primary(self,
                                                          ctx: Java9Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx: Java9Parser.TypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#methodInvocation.
    def visitMethodInvocation(self, ctx: Java9Parser.MethodInvocationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#methodInvocation_lf_primary.
    def visitMethodInvocation_lf_primary(self, ctx: Java9Parser.MethodInvocation_lf_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#methodInvocation_lfno_primary.
    def visitMethodInvocation_lfno_primary(self, ctx: Java9Parser.MethodInvocation_lfno_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#argumentList.
    def visitArgumentList(self, ctx: Java9Parser.ArgumentListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#arrayCreationExpression.
    def visitArrayCreationExpression(self, ctx: Java9Parser.ArrayCreationExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#expression.
    def visitExpression(self, ctx: Java9Parser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#lambdaExpression.
    def visitLambdaExpression(self, ctx: Java9Parser.LambdaExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#assignment.
    def visitAssignment(self, ctx: Java9Parser.AssignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: Java9Parser.AssignmentOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#conditionalExpression.
    def visitConditionalExpression(self, ctx: Java9Parser.ConditionalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#ternaryConditionalExpression.
    def visitTernaryConditionalExpression(self, ctx: Java9Parser.TernaryConditionalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#conditionalOrExpression.
    def visitConditionalOrExpression(self, ctx: Java9Parser.ConditionalOrExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#equalityExpression.
    def visitEqualityExpression(self, ctx: Java9Parser.EqualityExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#relationalExpression.
    def visitRelationalExpression(self, ctx: Java9Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#comparision.
    def visitComparision(self, ctx: Java9Parser.ComparisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#shiftExpression.
    def visitShiftExpression(self, ctx: Java9Parser.ShiftExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#unaryExpression.
    def visitUnaryExpression(self, ctx: Java9Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#preIncrementDecrementExpression.
    def visitPreIncrementDecrementExpression(self, ctx: Java9Parser.PreIncrementDecrementExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#unaryExpressionNotPlusMinus.
    def visitUnaryExpressionNotPlusMinus(self, ctx: Java9Parser.UnaryExpressionNotPlusMinusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Java9Parser#postIncrementDecrementExpression.
    def visitPostIncrementDecrementExpression(self, ctx: Java9Parser.PostIncrementDecrementExpressionContext):
        return self.visitChildren(ctx)


del Java9Parser
