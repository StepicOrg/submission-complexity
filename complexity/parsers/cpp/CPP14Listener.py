# Generated from /home/meanmail/StepikProjects/submission-complexity/complexity/grammars/CPP14.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CPP14Parser import CPP14Parser
else:
    from CPP14Parser import CPP14Parser


# This class defines a complete listener for a parse tree produced by CPP14Parser.
class CPP14Listener(ParseTreeListener):
    # Enter a parse tree produced by CPP14Parser#translationunit.
    def enterTranslationunit(self, ctx: CPP14Parser.TranslationunitContext):
        pass

    # Exit a parse tree produced by CPP14Parser#translationunit.
    def exitTranslationunit(self, ctx: CPP14Parser.TranslationunitContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unqualifiedid.
    def enterUnqualifiedid(self, ctx: CPP14Parser.UnqualifiedidContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unqualifiedid.
    def exitUnqualifiedid(self, ctx: CPP14Parser.UnqualifiedidContext):
        pass

    # Enter a parse tree produced by CPP14Parser#nestednamespecifier.
    def enterNestednamespecifier(self, ctx: CPP14Parser.NestednamespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#nestednamespecifier.
    def exitNestednamespecifier(self, ctx: CPP14Parser.NestednamespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#lambdadeclarator.
    def enterLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdadeclarator.
    def exitLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#postoperation.
    def enterPostoperation(self, ctx: CPP14Parser.PostoperationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postoperation.
    def exitPostoperation(self, ctx: CPP14Parser.PostoperationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#postfixexpression.
    def enterPostfixexpression(self, ctx: CPP14Parser.PostfixexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postfixexpression.
    def exitPostfixexpression(self, ctx: CPP14Parser.PostfixexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#call.
    def enterCall(self, ctx: CPP14Parser.CallContext):
        pass

    # Exit a parse tree produced by CPP14Parser#call.
    def exitCall(self, ctx: CPP14Parser.CallContext):
        pass

    # Enter a parse tree produced by CPP14Parser#pseudodestructorname.
    def enterPseudodestructorname(self, ctx: CPP14Parser.PseudodestructornameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pseudodestructorname.
    def exitPseudodestructorname(self, ctx: CPP14Parser.PseudodestructornameContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unaryexpression.
    def enterUnaryexpression(self, ctx: CPP14Parser.UnaryexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryexpression.
    def exitUnaryexpression(self, ctx: CPP14Parser.UnaryexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unaryincdecexpression.
    def enterUnaryincdecexpression(self, ctx: CPP14Parser.UnaryincdecexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryincdecexpression.
    def exitUnaryincdecexpression(self, ctx: CPP14Parser.UnaryincdecexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#postfixunaryincdecexpression.
    def enterPostfixunaryincdecexpression(self, ctx: CPP14Parser.PostfixunaryincdecexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postfixunaryincdecexpression.
    def exitPostfixunaryincdecexpression(self, ctx: CPP14Parser.PostfixunaryincdecexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#newexpression.
    def enterNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newexpression.
    def exitNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#newdeclarator.
    def enterNewdeclarator(self, ctx: CPP14Parser.NewdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newdeclarator.
    def exitNewdeclarator(self, ctx: CPP14Parser.NewdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrnewdeclarator.
    def enterNoptrnewdeclarator(self, ctx: CPP14Parser.NoptrnewdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrnewdeclarator.
    def exitNoptrnewdeclarator(self, ctx: CPP14Parser.NoptrnewdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#deleteexpression.
    def enterDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#deleteexpression.
    def exitDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#shiftexpression.
    def enterShiftexpression(self, ctx: CPP14Parser.ShiftexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#shiftexpression.
    def exitShiftexpression(self, ctx: CPP14Parser.ShiftexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#relationalexpression.
    def enterRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#relationalexpression.
    def exitRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#equalityexpression.
    def enterEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#equalityexpression.
    def exitEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def enterTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def exitTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def enterUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def exitUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#logicalorexpression.
    def enterLogicalorexpression(self, ctx: CPP14Parser.LogicalorexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#logicalorexpression.
    def exitLogicalorexpression(self, ctx: CPP14Parser.LogicalorexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#conditionalexpression.
    def enterConditionalexpression(self, ctx: CPP14Parser.ConditionalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#conditionalexpression.
    def exitConditionalexpression(self, ctx: CPP14Parser.ConditionalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#assignmentexpression.
    def enterAssignmentexpression(self, ctx: CPP14Parser.AssignmentexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#assignmentexpression.
    def exitAssignmentexpression(self, ctx: CPP14Parser.AssignmentexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#assignmentoperator.
    def enterAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#assignmentoperator.
    def exitAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#statement.
    def enterStatement(self, ctx: CPP14Parser.StatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#statement.
    def exitStatement(self, ctx: CPP14Parser.StatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#casestatement.
    def enterCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#casestatement.
    def exitCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#elsestatement.
    def enterElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#elsestatement.
    def exitElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#condition.
    def enterCondition(self, ctx: CPP14Parser.ConditionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#condition.
    def exitCondition(self, ctx: CPP14Parser.ConditionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#gotostatement.
    def enterGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#gotostatement.
    def exitGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declaration.
    def enterDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declaration.
    def exitDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#blockdeclaration.
    def enterBlockdeclaration(self, ctx: CPP14Parser.BlockdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#blockdeclaration.
    def exitBlockdeclaration(self, ctx: CPP14Parser.BlockdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#simpledeclaration.
    def enterSimpledeclaration(self, ctx: CPP14Parser.SimpledeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpledeclaration.
    def exitSimpledeclaration(self, ctx: CPP14Parser.SimpledeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declspecifier.
    def enterDeclspecifier(self, ctx: CPP14Parser.DeclspecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declspecifier.
    def exitDeclspecifier(self, ctx: CPP14Parser.DeclspecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#typespecifier.
    def enterTypespecifier(self, ctx: CPP14Parser.TypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typespecifier.
    def exitTypespecifier(self, ctx: CPP14Parser.TypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#trailingtypespecifier.
    def enterTrailingtypespecifier(self, ctx: CPP14Parser.TrailingtypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#trailingtypespecifier.
    def exitTrailingtypespecifier(self, ctx: CPP14Parser.TrailingtypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#simpletypespecifier.
    def enterSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpletypespecifier.
    def exitSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#attributespecifier.
    def enterAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributespecifier.
    def exitAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#balancedtoken.
    def enterBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by CPP14Parser#balancedtoken.
    def exitBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declarator.
    def enterDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarator.
    def exitDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ptrdeclarator.
    def enterPtrdeclarator(self, ctx: CPP14Parser.PtrdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ptrdeclarator.
    def exitPtrdeclarator(self, ctx: CPP14Parser.PtrdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parametersandqualifiers.
    def enterParametersandqualifiers(self, ctx: CPP14Parser.ParametersandqualifiersContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parametersandqualifiers.
    def exitParametersandqualifiers(self, ctx: CPP14Parser.ParametersandqualifiersContext):
        pass

    # Enter a parse tree produced by CPP14Parser#abstractdeclarator.
    def enterAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractdeclarator.
    def exitAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ptrabstractdeclarator.
    def enterPtrabstractdeclarator(self, ctx: CPP14Parser.PtrabstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ptrabstractdeclarator.
    def exitPtrabstractdeclarator(self, ctx: CPP14Parser.PtrabstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def enterNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def exitNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#abstractpackdeclarator.
    def enterAbstractpackdeclarator(self, ctx: CPP14Parser.AbstractpackdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractpackdeclarator.
    def exitAbstractpackdeclarator(self, ctx: CPP14Parser.AbstractpackdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
    def enterNoptrabstractpackdeclarator(self, ctx: CPP14Parser.NoptrabstractpackdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
    def exitNoptrabstractpackdeclarator(self, ctx: CPP14Parser.NoptrabstractpackdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parameterdeclaration.
    def enterParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterdeclaration.
    def exitParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#functionbody.
    def enterFunctionbody(self, ctx: CPP14Parser.FunctionbodyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionbody.
    def exitFunctionbody(self, ctx: CPP14Parser.FunctionbodyContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initializer.
    def enterInitializer(self, ctx: CPP14Parser.InitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializer.
    def exitInitializer(self, ctx: CPP14Parser.InitializerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#bracedinitlist.
    def enterBracedinitlist(self, ctx: CPP14Parser.BracedinitlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#bracedinitlist.
    def exitBracedinitlist(self, ctx: CPP14Parser.BracedinitlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberspecification.
    def enterMemberspecification(self, ctx: CPP14Parser.MemberspecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberspecification.
    def exitMemberspecification(self, ctx: CPP14Parser.MemberspecificationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclaration.
    def enterMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclaration.
    def exitMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclarator.
    def enterMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclarator.
    def exitMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#purespecifier.
    def enterPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#purespecifier.
    def exitPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#basespecifier.
    def enterBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#basespecifier.
    def exitBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#classordecltype.
    def enterClassordecltype(self, ctx: CPP14Parser.ClassordecltypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classordecltype.
    def exitClassordecltype(self, ctx: CPP14Parser.ClassordecltypeContext):
        pass

    # Enter a parse tree produced by CPP14Parser#meminitializer.
    def enterMeminitializer(self, ctx: CPP14Parser.MeminitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#meminitializer.
    def exitMeminitializer(self, ctx: CPP14Parser.MeminitializerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#templateparameter.
    def enterTemplateparameter(self, ctx: CPP14Parser.TemplateparameterContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateparameter.
    def exitTemplateparameter(self, ctx: CPP14Parser.TemplateparameterContext):
        pass

    # Enter a parse tree produced by CPP14Parser#typeparameter.
    def enterTypeparameter(self, ctx: CPP14Parser.TypeparameterContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeparameter.
    def exitTypeparameter(self, ctx: CPP14Parser.TypeparameterContext):
        pass

    # Enter a parse tree produced by CPP14Parser#templateargument.
    def enterTemplateargument(self, ctx: CPP14Parser.TemplateargumentContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateargument.
    def exitTemplateargument(self, ctx: CPP14Parser.TemplateargumentContext):
        pass

    # Enter a parse tree produced by CPP14Parser#tryblock.
    def enterTryblock(self, ctx: CPP14Parser.TryblockContext):
        pass

    # Exit a parse tree produced by CPP14Parser#tryblock.
    def exitTryblock(self, ctx: CPP14Parser.TryblockContext):
        pass

    # Enter a parse tree produced by CPP14Parser#handler.
    def enterHandler(self, ctx: CPP14Parser.HandlerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#handler.
    def exitHandler(self, ctx: CPP14Parser.HandlerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#exceptionspecification.
    def enterExceptionspecification(self, ctx: CPP14Parser.ExceptionspecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exceptionspecification.
    def exitExceptionspecification(self, ctx: CPP14Parser.ExceptionspecificationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#theoperator.
    def enterTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#theoperator.
    def exitTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        pass
