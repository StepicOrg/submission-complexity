from antlr4 import *

from complexity.parsers.cpp.CPP14Parser import CPP14Parser
from complexity.parsers.cpp.CPP14Visitor import CPP14Visitor
from complexity.visitors.base_visitor import BaseVisitor

# ABC rules for C++

ASSIGNMENTS = (
    # Occurrence of an assignment operator (exclude constant declarations and default parameter assignments)
    #       (=, *=, /=, %=, +=, <<=, >>=, &=, !=, ^=).
    CPP14Parser.RULE_assignmentoperator,
    # (prefix or postfix) (++, --)
    CPP14Parser.RULE_unaryincdecexpression,
    # Initialization of a variable or a nonconstant class member.
    CPP14Parser.RULE_initializer)

BRANCHES = (
    # Occurrence of a function call or a class method call.
    CPP14Parser.RULE_call,
    # Occurrence of any goto statement which has a target at a deeper level of nesting than the level to the goto.
    CPP14Parser.RULE_gotostatement,
    # Occurrence of ‘new’ or ‘delete’ operators.
    CPP14Parser.RULE_newexpression,
    CPP14Parser.RULE_deleteexpression)

CONDITIONALS = (
    # Occurrence of a conditional operator (<, >, <=, >=, ==, !=).
    CPP14Parser.RULE_equalityexpression,
    CPP14Parser.RULE_relationalexpression,
    # Occurrence of the following keywords (‘else’, ‘case’, ‘default’, ‘?’, ‘try’, ‘catch’).
    CPP14Parser.RULE_elsestatement,
    CPP14Parser.RULE_casestatement,
    CPP14Parser.RULE_ternaryconditionalexpression,
    CPP14Parser.RULE_tryblock,
    CPP14Parser.RULE_handler,
    # Occurrence of a unary conditional operator.
    CPP14Parser.RULE_unaryconditionalexpression
)


# This class defines a complete listener for a parse tree produced by CPP14Parser.
class Visitor(CPP14Visitor, BaseVisitor):
    def process(self, ctx: ParserRuleContext):
        if self.check_time_over():
            return
        rule = ctx.getRuleIndex()
        if rule in ASSIGNMENTS:
            self.a += 1
        elif rule in BRANCHES:
            self.b += 1
        elif rule in CONDITIONALS:
            self.c += 1

        return self.visitChildren(ctx)

    # Enter a parse tree produced by CPP14Parser#newexpression.
    def visitNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#deleteexpression.
    def visitDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#equalityexpression.
    def visitEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def visitTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def visitUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#assignmentoperator.
    def visitAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#casestatement.
    def visitCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#elsestatement.
    def visitElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#call.
    def visitCall(self, ctx: CPP14Parser.CallContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#gotostatement.
    def visitGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#initializer.
    def visitInitializer(self, ctx: CPP14Parser.InitializerContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#tryblock.
    def visitTryblock(self, ctx: CPP14Parser.TryblockContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#handler.
    def visitHandler(self, ctx: CPP14Parser.HandlerContext):
        return self.process(ctx)

    # Enter a parse tree produced by CPP14Parser#relationalexpression.
    def visitRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        return self.process(ctx)
