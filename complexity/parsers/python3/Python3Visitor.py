# Generated from complexity/grammars/Python3.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser


# This class defines a complete generic visitor for a parse tree produced by Python3Parser.

class Python3Visitor(ParseTreeVisitor):
    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx: Python3Parser.File_inputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#typedargslist.
    def visitTypedargslist(self, ctx: Python3Parser.TypedargslistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#varargslist.
    def visitVarargslist(self, ctx: Python3Parser.VarargslistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#stmt.
    def visitStmt(self, ctx: Python3Parser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#small_stmt.
    def visitSmall_stmt(self, ctx: Python3Parser.Small_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#assign.
    def visitAssign(self, ctx: Python3Parser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#augassign.
    def visitAugassign(self, ctx: Python3Parser.AugassignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#break_stmt.
    def visitBreak_stmt(self, ctx: Python3Parser.Break_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#raise_stmt.
    def visitRaise_stmt(self, ctx: Python3Parser.Raise_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#if_stmt.
    def visitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#else_suite.
    def visitElse_suite(self, ctx: Python3Parser.Else_suiteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#while_stmt.
    def visitWhile_stmt(self, ctx: Python3Parser.While_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#for_stmt.
    def visitFor_stmt(self, ctx: Python3Parser.For_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#try_stmt.
    def visitTry_stmt(self, ctx: Python3Parser.Try_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#except_clause.
    def visitExcept_clause(self, ctx: Python3Parser.Except_clauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#suite.
    def visitSuite(self, ctx: Python3Parser.SuiteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#test.
    def visitTest(self, ctx: Python3Parser.TestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#test_nocond.
    def visitTest_nocond(self, ctx: Python3Parser.Test_nocondContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#or_test.
    def visitOr_test(self, ctx: Python3Parser.Or_testContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#not_test.
    def visitNot_test(self, ctx: Python3Parser.Not_testContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#comp_op.
    def visitComp_op(self, ctx: Python3Parser.Comp_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#expr.
    def visitExpr(self, ctx: Python3Parser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#factor.
    def visitFactor(self, ctx: Python3Parser.FactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#call.
    def visitCall(self, ctx: Python3Parser.CallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#atom.
    def visitAtom(self, ctx: Python3Parser.AtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#testlist_comp.
    def visitTestlist_comp(self, ctx: Python3Parser.Testlist_compContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#trailer.
    def visitTrailer(self, ctx: Python3Parser.TrailerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#subscript.
    def visitSubscript(self, ctx: Python3Parser.SubscriptContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#exprlist.
    def visitExprlist(self, ctx: Python3Parser.ExprlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#testlist.
    def visitTestlist(self, ctx: Python3Parser.TestlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx: Python3Parser.DictorsetmakerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#arglist.
    def visitArglist(self, ctx: Python3Parser.ArglistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#comp_iter.
    def visitComp_iter(self, ctx: Python3Parser.Comp_iterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#comp_for.
    def visitComp_for(self, ctx: Python3Parser.Comp_forContext):
        return self.visitChildren(ctx)


del Python3Parser
