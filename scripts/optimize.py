import argparse
import re

RULES = {
    'cpp': (
        'assignmentoperator',
        'unaryincdecexpression',
        'initializer',
        'call',
        'gotostatement',
        'newexpression',
        'deleteexpression',
        'equalityexpression',
        'relationalexpression',
        'elsestatement',
        'casestatement',
        'ternaryconditionalexpression',
        'tryblock',
        'handler',
        'unaryconditionalexpression'
    ),
    'c': (
        'assignmentOperator',
        'unaryIncDecExpression',
        'call',
        'gotoStatement',
        'equalityExpression',
        'relationalExpression',
        'elseStatement',
        'caseStatement',
        'ternaryConditionalExpression',
        'unaryConditionalExpression',
    ),
    'java9': (
        'assignmentOperator',
        'preIncrementDecrementExpression',
        'postIncrementDecrementExpression',
        'variableInitializer',
        'methodInvocation',
        'methodInvocation_lf_primary',
        'methodInvocation_lfno_primary',
        'arrayCreationExpression',
        'classInstanceCreationExpression',
        'classInstanceCreationExpression_lf_primary',
        'classInstanceCreationExpression_lfno_primary',
        'whileStatement',
        'whileStatementNoShortIf',
        'doStatement',
        'forStatement',
        'forStatementNoShortIf',
        'assertStatement',
        'breakAndContinueStatement',
        'returnStatement',
        'throwStatement',
        'synchronizedStatement',
        'ifStatement',
        'ifStatementNoShortIf',
        'comparision',
        'equalityExpression',
        'elseStatement',
        'elseStatementNoShortIf',
        'switchLabel',
        'ternaryConditionalExpression',
        'tryStatement',
        'catchClause',
        'switchStatement',
    ),
    'python3': (
        'assign',
        'augassign',
        'call',
        'if_stmt',
        'while_stmt',
        'for_stmt',
        'raise_stmt',
        'break_stmt',
        'continue_stmt',
        'comp_iter',
        'comp_for',
        'assert_stmt',
        'return_stmt',
        'yield_stmt',
        'comp_op',
        'else_suite',
        'try_stmt',
        'except_clause',
    ),
}

FILE_NAMES = (
    ('cpp', 'CPP14Parser.py'),
    ('c', 'CParser.py'),
    ('java9', 'Java9Parser.py'),
    ('python3', 'Python3Parser.py'),
)


def optimize(parsers_path):
    for language, parser_file in FILE_NAMES:
        file_name = f'{parsers_path}/{language}/{parser_file}'
        with open(file_name, 'r') as file:
            data = file.read()
            # Optimize listener
            data = re.sub(r'(def exitRule\(self, listener:\s*ParseTreeListener\):\s*)'
                          r'if hasattr\(\s*listener, "[a-zA-Z][a-zA-Z0-9]*"\s*\):\s*'
                          r'listener\.exit[a-zA-Z][a-zA-Z0-9]*\(self\)',
                          r'\g<1>pass', data)

            data = re.sub(r'(def enterRule\(self, listener:\s*ParseTreeListener\):\s*)'
                          r'if hasattr\(\s*listener, "enter(?!({})")[a-zA-Z0-9]*"\s*\):\s*'
                          r'listener\.enter[a-zA-Z][a-zA-Z0-9]*\(self\)'.format("|".join(RULES[language])),
                          r'\g<1>pass', data, flags=re.IGNORECASE)

            # Optimize visitor
            data = re.sub(r'(def accept\(self, visitor:\s*ParseTreeVisitor\):\s*)'
                          r'if hasattr\(\s*visitor, "visit(?!({})")[a-zA-Z0-9]*"\s*\):\s*'
                          r'return visitor\.visit[a-zA-Z][a-zA-Z0-9]*\(self\)\s*'
                          r'else:\s*'
                          r'return visitor\.visitChildren\(self\)'.format("|".join(RULES[language])),
                          r'\g<1>return visitor.visitChildren(self)', data, flags=re.IGNORECASE)

            # Common optimize
            data = re.sub(r'(if .*) in \[(\w*\.\w*)\]', r'\g<1> == \g<2>', data)

        with open(file_name, 'w') as file:
            file.write(data)

        print(f"{language}: {file_name} optimized")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parsers_path", help="Path to parsers", default='../complexity/parsers')
    args = parser.parse_args()
    print(f"Optimize parsers from {args.parsers_path}")
    optimize(args.parsers_path)
