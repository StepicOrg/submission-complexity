# Generated from complexity/grammars/C.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser


# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by CParser#primaryExpression.
    def visitPrimaryExpression(self, ctx: CParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#genericSelection.
    def visitGenericSelection(self, ctx: CParser.GenericSelectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#postOperation.
    def visitPostOperation(self, ctx: CParser.PostOperationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#postfixExpression.
    def visitPostfixExpression(self, ctx: CParser.PostfixExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#call.
    def visitCall(self, ctx: CParser.CallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#unaryIncDecExpression.
    def visitUnaryIncDecExpression(self, ctx: CParser.UnaryIncDecExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#postfixUnaryIncDecExpression.
    def visitPostfixUnaryIncDecExpression(self, ctx: CParser.PostfixUnaryIncDecExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx: CParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#unaryExpression.
    def visitUnaryExpression(self, ctx: CParser.UnaryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#castExpression.
    def visitCastExpression(self, ctx: CParser.CastExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#shiftExpression.
    def visitShiftExpression(self, ctx: CParser.ShiftExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#relationalExpression.
    def visitRelationalExpression(self, ctx: CParser.RelationalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#equalityExpression.
    def visitEqualityExpression(self, ctx: CParser.EqualityExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx: CParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#conditionalExpression.
    def visitConditionalExpression(self, ctx: CParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#ternaryConditionalExpression.
    def visitTernaryConditionalExpression(self, ctx: CParser.TernaryConditionalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#unaryConditionalExpression.
    def visitUnaryConditionalExpression(self, ctx: CParser.UnaryConditionalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx: CParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: CParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx: CParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx: CParser.DeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx: CParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx: CParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initDeclarator.
    def visitInitDeclarator(self, ctx: CParser.InitDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx: CParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structDeclaration.
    def visitStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx: CParser.SpecifierQualifierListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structDeclarator.
    def visitStructDeclarator(self, ctx: CParser.StructDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#enumerator.
    def visitEnumerator(self, ctx: CParser.EnumeratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx: CParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx: CParser.AlignmentSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#declarator.
    def visitDeclarator(self, ctx: CParser.DeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#directDeclarator.
    def visitDirectDeclarator(self, ctx: CParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx: CParser.GccDeclaratorExtensionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx: CParser.GccAttributeSpecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccAttributeList.
    def visitGccAttributeList(self, ctx: CParser.GccAttributeListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccAttribute.
    def visitGccAttribute(self, ctx: CParser.GccAttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx: CParser.NestedParenthesesBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#pointer.
    def visitPointer(self, ctx: CParser.PointerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#parameterList.
    def visitParameterList(self, ctx: CParser.ParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx: CParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#identifierList.
    def visitIdentifierList(self, ctx: CParser.IdentifierListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#typeName.
    def visitTypeName(self, ctx: CParser.TypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx: CParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx: CParser.DirectAbstractDeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initializer.
    def visitInitializer(self, ctx: CParser.InitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initializerList.
    def visitInitializerList(self, ctx: CParser.InitializerListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#designator.
    def visitDesignator(self, ctx: CParser.DesignatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx: CParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx: CParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#caseStatement.
    def visitCaseStatement(self, ctx: CParser.CaseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#blockItem.
    def visitBlockItem(self, ctx: CParser.BlockItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#selectionStatement.
    def visitSelectionStatement(self, ctx: CParser.SelectionStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#elseStatement.
    def visitElseStatement(self, ctx: CParser.ElseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#iterationStatement.
    def visitIterationStatement(self, ctx: CParser.IterationStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#forCondition.
    def visitForCondition(self, ctx: CParser.ForConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#forExpression.
    def visitForExpression(self, ctx: CParser.ForExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#jumpStatement.
    def visitJumpStatement(self, ctx: CParser.JumpStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gotoStatement.
    def visitGotoStatement(self, ctx: CParser.GotoStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#compilationUnit.
    def visitCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx: CParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


del CParser
