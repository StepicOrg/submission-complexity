# Generated from complexity/grammars/CPP14.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CPP14Parser import CPP14Parser
else:
    from CPP14Parser import CPP14Parser


# This class defines a complete generic visitor for a parse tree produced by CPP14Parser.

class CPP14Visitor(ParseTreeVisitor):
    # Visit a parse tree produced by CPP14Parser#translationunit.
    def visitTranslationunit(self, ctx: CPP14Parser.TranslationunitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#unqualifiedid.
    def visitUnqualifiedid(self, ctx: CPP14Parser.UnqualifiedidContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#nestednamespecifier.
    def visitNestednamespecifier(self, ctx: CPP14Parser.NestednamespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#lambdadeclarator.
    def visitLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#postoperation.
    def visitPostoperation(self, ctx: CPP14Parser.PostoperationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#postfixexpression.
    def visitPostfixexpression(self, ctx: CPP14Parser.PostfixexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#call.
    def visitCall(self, ctx: CPP14Parser.CallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#unaryexpression.
    def visitUnaryexpression(self, ctx: CPP14Parser.UnaryexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#unaryincdecexpression.
    def visitUnaryincdecexpression(self, ctx: CPP14Parser.UnaryincdecexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#postfixunaryincdecexpression.
    def visitPostfixunaryincdecexpression(self, ctx: CPP14Parser.PostfixunaryincdecexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#newexpression.
    def visitNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#newdeclarator.
    def visitNewdeclarator(self, ctx: CPP14Parser.NewdeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#deleteexpression.
    def visitDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#relationalexpression.
    def visitRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#equalityexpression.
    def visitEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def visitTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def visitUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#logicalorexpression.
    def visitLogicalorexpression(self, ctx: CPP14Parser.LogicalorexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#conditionalexpression.
    def visitConditionalexpression(self, ctx: CPP14Parser.ConditionalexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#assignmentexpression.
    def visitAssignmentexpression(self, ctx: CPP14Parser.AssignmentexpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#assignmentoperator.
    def visitAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#statement.
    def visitStatement(self, ctx: CPP14Parser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#casestatement.
    def visitCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#elsestatement.
    def visitElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#condition.
    def visitCondition(self, ctx: CPP14Parser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#gotostatement.
    def visitGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#declaration.
    def visitDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#blockdeclaration.
    def visitBlockdeclaration(self, ctx: CPP14Parser.BlockdeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#simpledeclaration.
    def visitSimpledeclaration(self, ctx: CPP14Parser.SimpledeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#declspecifier.
    def visitDeclspecifier(self, ctx: CPP14Parser.DeclspecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#typespecifier.
    def visitTypespecifier(self, ctx: CPP14Parser.TypespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#trailingtypespecifier.
    def visitTrailingtypespecifier(self, ctx: CPP14Parser.TrailingtypespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#simpletypespecifier.
    def visitSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#attributespecifier.
    def visitAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#balancedtoken.
    def visitBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#declarator.
    def visitDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#ptrdeclarator.
    def visitPtrdeclarator(self, ctx: CPP14Parser.PtrdeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#parametersandqualifiers.
    def visitParametersandqualifiers(self, ctx: CPP14Parser.ParametersandqualifiersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#abstractdeclarator.
    def visitAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#ptrabstractdeclarator.
    def visitPtrabstractdeclarator(self, ctx: CPP14Parser.PtrabstractdeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def visitNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#parameterdeclaration.
    def visitParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#functionbody.
    def visitFunctionbody(self, ctx: CPP14Parser.FunctionbodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#initializer.
    def visitInitializer(self, ctx: CPP14Parser.InitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#bracedinitlist.
    def visitBracedinitlist(self, ctx: CPP14Parser.BracedinitlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#memberspecification.
    def visitMemberspecification(self, ctx: CPP14Parser.MemberspecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#memberdeclarator.
    def visitMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#purespecifier.
    def visitPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#basespecifier.
    def visitBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#classordecltype.
    def visitClassordecltype(self, ctx: CPP14Parser.ClassordecltypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#meminitializer.
    def visitMeminitializer(self, ctx: CPP14Parser.MeminitializerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#templateparameter.
    def visitTemplateparameter(self, ctx: CPP14Parser.TemplateparameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#templateargument.
    def visitTemplateargument(self, ctx: CPP14Parser.TemplateargumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#tryblock.
    def visitTryblock(self, ctx: CPP14Parser.TryblockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#handler.
    def visitHandler(self, ctx: CPP14Parser.HandlerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#exceptionspecification.
    def visitExceptionspecification(self, ctx: CPP14Parser.ExceptionspecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPP14Parser#theoperator.
    def visitTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        return self.visitChildren(ctx)


del CPP14Parser
