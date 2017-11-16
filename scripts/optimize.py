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
    )
}

FILE_NAMES = {
    'cpp': 'CPP14Parser.py',
}


def optimize(parsers_path):
    for language, parser_file in FILE_NAMES.items():
        file_name = f'{parsers_path}/{language}/{parser_file}'
        with open(file_name, 'r') as file:
            data = file.read()
            data = re.sub(r'(def exitRule\(self, listener:\s*ParseTreeListener\):\s*)'
                          r'if hasattr\(\s*listener, "[a-zA-Z][a-zA-Z0-9]*"\s*\):\s*'
                          r'listener\.exit[a-zA-Z][a-zA-Z0-9]*\(self\)',
                          r'\g<1>pass', data)

            data = re.sub(r'(def enterRule\(self, listener:\s*ParseTreeListener\):\s*)'
                          r'if hasattr\(\s*listener, "enter(?!({})")[a-zA-Z0-9]*"\s*\):\s*'
                          r'listener\.enter[a-zA-Z][a-zA-Z0-9]*\(self\)'.format("|".join(RULES[language])),
                          r'\g<1>pass', data, flags=re.IGNORECASE)

            data = re.sub(r'(if .*) in \[(\w*\.\w*)\]', r'\g<1> == \g<2>', data)

        with open(file_name, 'w') as file:
            file.write(data)

        print(f"{file_name} optimized")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parsers_path", help="Path to parsers", default='../complexity/parsers')
    args = parser.parse_args()
    print(f"Optimize parsers {args.parsers_path}...")
    optimize(args.parsers_path)
