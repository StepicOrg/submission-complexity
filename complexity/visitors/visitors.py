import math

import javalang
import javalang.tree as java_ast
from radon.visitors import CodeVisitor

# TODO read carefully about Node Types
CONDITIONALS = ('Compare', 'Try', 'ExceptHandler')
BRANCHES = ('If', 'While', 'For', 'Raise', 'Break', 'cond', 'iter', 'Call', 'In')
ASSIGNMENTS = ('Assign', 'AugAssign')


class ABCVisitor(CodeVisitor):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    @property
    def abc_score(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2), 2)

    @property
    def abc_vector(self):
        return self.a, self.b, self.c

    def is_assignment(self, node):
        return self.get_name(node) in ASSIGNMENTS

    def is_branch(self, node):
        return self.get_name(node) in BRANCHES

    def is_condition(self, node):
        return self.get_name(node) in CONDITIONALS

    def visit_node(self, node):
        if self.is_assignment(node):
            self.a += 1
        elif self.is_branch(node):
            self.b += 1
        elif self.is_condition(node):
            self.c += 1

    def generic_visit(self, node):
        self.visit_node(node)
        super().generic_visit(node)


class JavaABCVisitor(ABCVisitor):
    @classmethod
    def from_code(cls, code, **kwargs):
        return cls.from_ast(javalang.parse.parse(code), **kwargs)

    def is_assignment(self, node):
        return isinstance(node, (java_ast.VariableDeclarator, java_ast.Assignment))

    def is_branch(self, node):
        return isinstance(node, (java_ast.Invocation, java_ast.Creator, java_ast.WhileStatement, java_ast.DoStatement,
                                 java_ast.ForStatement, java_ast.AssertStatement, java_ast.BreakStatement,
                                 java_ast.ContinueStatement, java_ast.ReturnStatement, java_ast.ThrowStatement,
                                 java_ast.SynchronizedStatement, java_ast.Cast, java_ast.IfStatement))

    def is_condition(self, node):
        return isinstance(node, (java_ast.TryStatement, java_ast.SwitchStatement, java_ast.TryResource,
                                 java_ast.CatchClause, java_ast.TernaryExpression, java_ast.SwitchStatementCase,
                                 java_ast.ForControl, java_ast.EnhancedForControl, java_ast.BinaryOperation))

    def generic_visit(self, node):
        if isinstance(node, java_ast.Node):
            self.visit_node(node)
            children = node.children
        else:
            children = node

        for child in children:
            if isinstance(child, (java_ast.Node, list, tuple)):
                self.visit(child)
