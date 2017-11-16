/*******************************************************************************
 * The MIT License (MIT)
 *
 * Copyright (c) 2015 Camilo Sanchez (Camiloasc1)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 ******************************************************************************/

/*******************************************************************************
 * C++14 Grammar for ANTLR v4
 *
 * Based on n4140 draft paper
 * https://github.com/cplusplus/draft/blob/master/papers/n4140.pdf
 * and
 * http://www.nongnu.org/hcb/
 *
 * Possible Issues:
 *
 * Input must avoid conditional compilation blocks (this grammar ignores any preprocessor directive)
 * GCC extensions not yet supported (do not try to parse the preprocessor output)
 * Right angle bracket (C++11) - Solution '>>' and '>>=' are not tokens, only '>'
 * Lexer issue with pure-specifier rule ('0' token) - Solution in embedded code
 *   Change it to match the target language you want in line 1097 or verify inside your listeners/visitors
 *   Java:
if($val.text.compareTo("0")!=0) throw new InputMismatchException(this);
 *   JavaScript:

 *   Python2:

 *   Python3:

 *   C#:

 ******************************************************************************/
grammar CPP14;

/*Basic concepts*/
translationunit
:
    declaration* EOF
;

/*Expressions*/
unqualifiedid
:
    Operator typespecifier+ attributespecifier* (
        nestednamespecifier? '*' attributespecifier* ConstOrVolatile*
        | ('&' | '&&') attributespecifier*
    )*
    | '~' (
        Identifier ('<' (templateargument '...'?    (',' templateargument '...'?)*)? '>')?
        | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
    )
    | (Identifier | Operator (theoperator | Stringliteral Identifier | Userdefinedstringliteral)) ('<' (templateargument '...'? (',' templateargument '...'?)*)? '>')?
;

nestednamespecifier
:
    (
        Identifier ('<' (templateargument '...'?    (',' templateargument '...'?)*)? '>')?
        | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
    )?
    ('::' (Identifier | Template? Identifier '<' (templateargument '...'?    (',' templateargument '...'?)*)? '>'))* '::'
;

lambdadeclarator
:
    '(' (parameterdeclaration (',' parameterdeclaration)* ','?)? '...'? ')' Mutable? exceptionspecification?
    attributespecifier* ('->' trailingtypespecifier+ attributespecifier* abstractdeclarator?)?
;

postoperation
:
    ('.' | '->') (Template? (nestednamespecifier Template?)? unqualifiedid | pseudodestructorname)
    | ('[' (
        assignmentexpression (',' assignmentexpression)*
          | bracedinitlist
    ) ']'
    | '(' ((assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)*)? ')')
;

postfixexpression
:
    call
    | (
        (
            Numberliteral
            | Characterliteral
            | Stringliteral
            | TrueFalse
            | Nullptr
            | Userdefinedliteral
            | Userdefinedstringliteral
            | This
        )
        | (nestednamespecifier Template?)? unqualifiedid
        | '[' ('&' | '=' | (('&' | '=') ',')? ('&'? Identifier initializer? | This) '...'?
            (',' ('&'? Identifier initializer? | This) '...'?)*)? ']' lambdadeclarator? '{' statement* '}'
        | (simpletypespecifier | Typename nestednamespecifier (Identifier | Template? Identifier '<' (templateargument '...'?    (',' templateargument '...'?)*)? '>'))
            ('(' ((assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)*)? ')' | bracedinitlist)
        | (Cast '<' typespecifier+ attributespecifier* abstractdeclarator? '>')? '(' assignmentexpression (',' assignmentexpression)* ')'
        | Typeid '(' (
            assignmentexpression (',' assignmentexpression)*
            | typespecifier+ attributespecifier* abstractdeclarator?
        ) ')'
    ) postoperation*
;

// used in BRANCHES
call
:
    unqualifiedid '(' (assignmentexpression (',' assignmentexpression)*)? ')'
;

pseudodestructorname
:
    (
        nestednamespecifier? (Identifier ('<' (templateargument '...'?    (',' templateargument '...'?)*)? '>')? '::')?
        | nestednamespecifier Template Identifier '<' (templateargument '...'?    (',' templateargument '...'?)*)? '>' '::'
    ) '~' Identifier ('<' (templateargument '...'?    (',' templateargument '...'?)*)? '>')?
    | '~' Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
;

unaryexpression
:
    postfixexpression
    | unaryincdecexpression
    | (Sizeof | ('|' | '*' | '&' | '+' | '!' | '~' | '-') ('(' typespecifier+ attributespecifier* abstractdeclarator? ')')*) unaryexpression
    | Sizeof '...' '(' Identifier ')'
    | (Alignof | Sizeof) '(' typespecifier+ attributespecifier* abstractdeclarator? ')'
    | Noexcept '(' assignmentexpression (',' assignmentexpression)* ')'
    | newexpression
    | deleteexpression
;

// used in ASSIGNMENTS
unaryincdecexpression
:
    ('++' | '--') ('(' typespecifier+ attributespecifier* abstractdeclarator? ')')* unaryexpression
    | postfixunaryincdecexpression
;

postfixunaryincdecexpression
:
    postfixexpression ('++' | '--') | postfixunaryincdecexpression postoperation* ('++' | '--')
;

// used in BRANCHES
newexpression
:
    '::'? New ('(' (assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)* ')')? (
        typespecifier+ attributespecifier* newdeclarator?
        | '(' typespecifier+ attributespecifier* abstractdeclarator? ')'
    ) ('(' ((assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)*)? ')' | bracedinitlist)?
;

newdeclarator
:
    (nestednamespecifier? '*' attributespecifier* ConstOrVolatile* | ('&' | '&&') attributespecifier*) newdeclarator?
    | noptrnewdeclarator
;

noptrnewdeclarator
:
    '[' assignmentexpression (',' assignmentexpression)* ']' attributespecifier*
    ('[' conditionalexpression ']' attributespecifier*)*
;

// used in BRANCHES
deleteexpression
:
    '::'? Delete ('[' ']')? ('(' typespecifier+ attributespecifier* abstractdeclarator? ')')* unaryexpression
;

shiftexpression
:
    ('(' typespecifier+ attributespecifier* abstractdeclarator? ')')* unaryexpression (
        ('.*' | '->*' | '*' | '/' | '%' | '+' | '-' | '<<' | Greater Greater )
        ('(' typespecifier+ attributespecifier* abstractdeclarator? ')')* unaryexpression
    )*
;

// used in CONDITIONALS
relationalexpression
:
    shiftexpression | relationalexpression ('<' | '>' | '<=' | '>=') shiftexpression
;

// used in CONDITIONALS
equalityexpression
:
    relationalexpression | equalityexpression ('==' | '!=') relationalexpression
;

// used in CONDITIONALS
ternaryconditionalexpression
:
    logicalorexpression '?' assignmentexpression (',' assignmentexpression)* ':' assignmentexpression
;

// used in CONDITIONALS
unaryconditionalexpression
:
    logicalorexpression '?:' assignmentexpression
;

logicalorexpression
:
    equalityexpression (('^' | '&' | '|' | '&&' | '||') equalityexpression)*
;

conditionalexpression
:
    logicalorexpression
    | ternaryconditionalexpression
;

assignmentexpression
:
    (logicalorexpression assignmentoperator | Throw)* (
        conditionalexpression
        | logicalorexpression assignmentoperator bracedinitlist
        | Throw
    )
;

// used in ASSIGNMENTS
assignmentoperator
:
    (
        '='
        | '*='
        | '/='
        | '%='
        | '+='
        | '-='
        | '<<='
        | '&='
        | '^='
        | '|='
    )
    | Greater Greater Assign
;

/*Statements*/
statement
:
    attributespecifier* (
        (Identifier ':' | (Switch | While) '(' condition ')') statement
        | casestatement
        | (assignmentexpression (',' assignmentexpression)*)? ';'
        | '{' statement* '}'
        | If '(' condition ')' statement elsestatement?
        | Do statement While '(' assignmentexpression (',' assignmentexpression)* ')' ';'
        | For '(' ((
                (assignmentexpression (',' assignmentexpression)*)? ';'
                | simpledeclaration
            ) condition? ';' (assignmentexpression (',' assignmentexpression)*)?
            | attributespecifier* declspecifier+ attributespecifier* declarator ':' (
                assignmentexpression (',' assignmentexpression)*
                | bracedinitlist)
        ) ')' statement
        | (
              (Break | Continue)
              | Return ((assignmentexpression (',' assignmentexpression)*)? | bracedinitlist)
        ) ';'
        | gotostatement
        | tryblock
    )
    | blockdeclaration
;

// used in CONDITIONALS
casestatement
:
    Case (conditionalexpression | Default) ':' statement
;

// used in CONDITIONALS
elsestatement
:
    Else statement
;

condition
:
    assignmentexpression (',' assignmentexpression)*
    | attributespecifier* declspecifier+ attributespecifier* declarator (
        '=' assignmentexpression
        | '='? bracedinitlist
    )
;

// used in BRANCHES
gotostatement
:
    Goto Identifier ';'
;

/*Declarations*/
declaration
:
    blockdeclaration
    | attributespecifier* ((declspecifier+ attributespecifier*)? declarator (Override | Final)* functionbody | ';')
    | (
        Template ('<' (templateparameter (',' templateparameter)*)? '>')?
        | Extern (Template | Stringliteral)
    ) declaration
    | (Extern Stringliteral | Inline? Namespace Identifier?) '{' declaration* '}'
;

blockdeclaration
:
    simpledeclaration
    | (
        Asm '(' Stringliteral ')'
        | (attributespecifier* Using Namespace | Namespace Identifier '=') nestednamespecifier? Identifier
        | Using (
            (Typename? nestednamespecifier | '::') unqualifiedid
            | Identifier attributespecifier* '=' typespecifier+ attributespecifier* abstractdeclarator?
        )
        | Static_assert '(' conditionalexpression ',' Stringliteral ')'
        | Enum (Class | Struct)? attributespecifier* Identifier (':' typespecifier+ attributespecifier*)?
    ) ';'
;

simpledeclaration
:
    (declspecifier+ attributespecifier*)? (declarator initializer? (',' declarator initializer?)*)? ';'
    | attributespecifier+ (declspecifier+ attributespecifier*)? declarator initializer? (',' declarator initializer?)* ';'
;

declspecifier
:
    (
        Specifier
        | Extern
        | Mutable
        | Inline
        | Virtual
    )
    | typespecifier
;

typespecifier
:
    trailingtypespecifier
    | (Class | Struct | Union) attributespecifier* (nestednamespecifier? Identifier ('<' (templateargument '...'?    (',' templateargument '...'?)*)? '>')? Final?)?
        ':' (basespecifier '...'? (',' basespecifier '...'?)*)? '{' memberspecification? '}'
    | Enum (Class | Struct)? attributespecifier* (Identifier? | nestednamespecifier Identifier)
        (':' typespecifier+ attributespecifier*)?
        '{' (Identifier ('=' conditionalexpression)? (',' Identifier ('=' conditionalexpression)?)* ','?)? '}'
;

trailingtypespecifier
:
    simpletypespecifier
    | (Class | Struct | Union) (
        attributespecifier* nestednamespecifier? Identifier
        | (nestednamespecifier Template?)? Identifier '<' (templateargument '...'? (',' templateargument '...'?)*)? '>'
    )
    | Enum nestednamespecifier? Identifier
    | Typename nestednamespecifier (
        Identifier
        | Template? Identifier '<' (templateargument '...'? (',' templateargument '...'?)*)? '>'
    )
    | ConstOrVolatile
;

simpletypespecifier
:
    nestednamespecifier? Identifier ('<' (templateargument '...'? (',' templateargument '...'?)*)? '>')?
    | nestednamespecifier Template Identifier '<' (templateargument '...'? (',' templateargument '...'?)*)? '>'
    | (
        Types
        | SignedUnsigned
        | Auto
    )
    | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
;

attributespecifier
:
    '[' '[' (Identifier ('::' Identifier)? ('(' balancedtoken* ')')? '...'?)?
       (',' (Identifier ('::' Identifier)? ('(' balancedtoken* ')')? '...'?)?)* ']' ']'
    | Alignas '(' (
        typespecifier+ attributespecifier* abstractdeclarator?
        | conditionalexpression
    )  '...'? ')'
;

balancedtoken
:
      '(' balancedtoken* ')'
    | '[' balancedtoken* ']'
    | '{' balancedtoken* '}'
    /*any token other than a parenthesis , a bracket , or a brace*/
;

/*Declarators*/
declarator
:
    ptrdeclarator
    | ('...'? (nestednamespecifier Template?)? unqualifiedid attributespecifier* | '(' ptrdeclarator ')') (
        parametersandqualifiers
        | '[' conditionalexpression? ']' attributespecifier*
    )* parametersandqualifiers '->' trailingtypespecifier+ attributespecifier* abstractdeclarator?
;

ptrdeclarator
:
    (
        '...'? (nestednamespecifier Template?)? unqualifiedid attributespecifier*
        | '(' ptrdeclarator ')'
    ) (parametersandqualifiers | '[' conditionalexpression? ']' attributespecifier*)*
    | (nestednamespecifier? '*' attributespecifier* ConstOrVolatile* | ('&' | '&&') attributespecifier*) ptrdeclarator
;

parametersandqualifiers
:
    '(' (parameterdeclaration (',' parameterdeclaration)* ','?)? '...'? ')' ConstOrVolatile* ('&' | '&&')?
    exceptionspecification? attributespecifier*
;

abstractdeclarator
:
    ptrabstractdeclarator
    | noptrabstractdeclarator? parametersandqualifiers '->' trailingtypespecifier+ attributespecifier* abstractdeclarator?
    | abstractpackdeclarator
;

ptrabstractdeclarator
:
    noptrabstractdeclarator
    | (nestednamespecifier? '*' attributespecifier* ConstOrVolatile* | ('&' | '&&') attributespecifier*) ptrabstractdeclarator?
;

noptrabstractdeclarator
:
    noptrabstractdeclarator (parametersandqualifiers | '[' conditionalexpression? ']' attributespecifier*)
    | parametersandqualifiers
    | '[' conditionalexpression? ']' attributespecifier*
    | '(' ptrabstractdeclarator ')'
;

abstractpackdeclarator
:
    noptrabstractpackdeclarator
    | (nestednamespecifier? '*' attributespecifier* ConstOrVolatile* | ('&' | '&&') attributespecifier*) abstractpackdeclarator
;

noptrabstractpackdeclarator
:
    noptrabstractpackdeclarator (parametersandqualifiers | '[' conditionalexpression? ']' attributespecifier*)
    | '...'
;

parameterdeclaration
:
    attributespecifier* declspecifier+ attributespecifier* (declarator abstractdeclarator? ('=' (assignmentexpression | bracedinitlist))?)
;

functionbody
:
    (':' meminitializer '...'? (',' meminitializer '...'?)*)? '{' statement* '}'
    | Try (':' meminitializer '...'? (',' meminitializer '...'?)*)? '{' statement* '}' handler+
    | '=' (Default | Delete) ';'
;

// used in ASSIGNMENTS
initializer
:
    '=' assignmentexpression
    | '='? bracedinitlist
    | '(' (assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)* ')'
;

bracedinitlist
:
    '{' ((assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)* ','?)? '}'
;

/*Classes*/
memberspecification
:
    memberdeclaration memberspecification?
    | PrivateProtectedPublic ':' memberspecification?
;

memberdeclaration
:
    attributespecifier* (declspecifier+ attributespecifier*)? (
        (memberdeclarator (',' memberdeclarator))? ';'
        | declarator (Override | Final)* functionbody
    )
    | Static_assert '(' conditionalexpression ',' Stringliteral ')' ';'
    | Template '<' templateparameter (',' templateparameter)* '>' declaration
    | Using (
        (Typename? nestednamespecifier | '::') unqualifiedid
        | Identifier attributespecifier* '=' typespecifier+ attributespecifier* abstractdeclarator?
    ) ';'
    | ';'
;

memberdeclarator
:
    declarator ((Override | Final)* purespecifier? | ('=' assignmentexpression | '='? bracedinitlist)?)
    | Identifier? attributespecifier* ':' conditionalexpression
;

/*
purespecifier:
    '=' '0'//Conflicts with the lexer
 ;
 */
purespecifier
:
    Assign val = Octalliteral
    {if $val.text.compareTo('0') != 0:
    raise InputMismatchException(self)}

;

/*Derived classes*/
basespecifier
:
    attributespecifier* (Virtual PrivateProtectedPublic? | PrivateProtectedPublic Virtual?)? classordecltype
;

classordecltype
:
    nestednamespecifier? Identifier ('<' (templateargument '...'?    (',' templateargument '...'?)*)? '>')?
    | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
;

/*Special member functions*/
meminitializer
:
    (classordecltype | Identifier) ('(' ((assignmentexpression | bracedinitlist) '...'? (',' (assignmentexpression | bracedinitlist) '...'?)*)? ')' | bracedinitlist)
;

/*Templates*/
templateparameter
:
    typeparameter
    | parameterdeclaration
;

typeparameter
:
    (Class | Typename) ('...'? Identifier? | Identifier? '=' typespecifier+ attributespecifier* abstractdeclarator?)
    | Template '<' templateparameter (',' templateparameter)* '>' Class (
        '...'? Identifier?
        | Identifier? '=' (nestednamespecifier Template?)? unqualifiedid
    )
;

templateargument
:
    typespecifier+ attributespecifier* abstractdeclarator?
    | conditionalexpression
    | (nestednamespecifier Template?)? unqualifiedid
;

/*Exception handling*/
// used in CONDITIONALS
tryblock
:
    Try '{' statement* '}' handler+
;

// used in CONDITIONALS
handler
:
    Catch '(' (
        attributespecifier* typespecifier+ attributespecifier* (declarator | abstractdeclarator?)
        | '...'
    ) ')' '{' statement* '}'
;

exceptionspecification
:
    Throw '(' (typespecifier+ attributespecifier* abstractdeclarator? '...'? (',' typespecifier+ attributespecifier* abstractdeclarator? '...'?)*)? ')'
    | Noexcept ('(' conditionalexpression ')')?
;

/*Preprocessing directives*/

MultiLineMacro
:
    '#' (~[\n]*? '\\' '\r'? '\n')+ ~[\n]+ -> channel(HIDDEN)
;

Directive
:
    '#' ~[\n]* -> channel(HIDDEN)
;

/*Lexer*/

/*Keywords*/
Alignas
:
    'alignas'
;

Alignof
:
    'alignof'
;

Asm
:
    'asm'
;

Auto
:
    'auto'
;

Break
:
    'break'
;

Case
:
    'case'
;

Catch
:
    'catch'
;

Class
:
    'class'
;

ConstOrVolatile
:
    'const' | 'volatile'
;

Cast
:
    'const_cast'
    | 'reinterpret_cast'
    | 'static_cast'
    | 'dynamic_cast'
;

Continue
:
    'continue'
;

Decltype
:
    'decltype'
;

Default
:
    'default'
;

Delete
:
    'delete'
;

Do
:
    'do'
;

Else
:
    'else'
;

Enum
:
    'enum'
;

Export
:
    'export'
;

Extern
:
    'extern'
;

TrueFalse
:
    'true' | 'false'
;

Final
:
    'final'
;

For
:
    'for'
;

Goto
:
    'goto'
;

If
:
    'if'
;

Inline
:
    'inline'
;

Types
:
    'int'
    | 'long'
    | 'short'
    | 'double'
    | 'float'
    | 'bool'
    | 'wchar_t'
    | 'char16_t'
    | 'char32_t'
    | 'char'
    | 'void'
;

Mutable
:
    'mutable'
;

Namespace
:
    'namespace'
;

New
:
    'new'
;

Noexcept
:
    'noexcept'
;

Nullptr
:
    'nullptr'
;

Operator
:
    'operator'
;

Override
:
    'override'
;

PrivateProtectedPublic
:
    'private'| 'protected' | 'public'
;

Specifier
:
    'register'
    | 'static'
    | 'thread_local'
    | 'explicit'
    | 'friend'
    | 'typedef'
    | 'constexpr'
;

Return
:
    'return'
;

SignedUnsigned
:
    'signed' | 'unsigned'
;

Sizeof
:
    'sizeof'
;

Static_assert
:
    'static_assert'
;

Struct
:
    'struct'
;

Switch
:
    'switch'
;

Template
:
    'template'
;

This
:
    'this'
;

Throw
:
    'throw'
;

Try
:
    'try'
;

Typeid
:
    'typeid'
;

Typename
:
    'typename'
;

Union
:
    'union'
;

Using
:
    'using'
;

Virtual
:
    'virtual'
;

While
:
    'while'
;

/*Operators*/
LeftParen
:
    '('
;

RightParen
:
    ')'
;

LeftBracket
:
    '['
;

RightBracket
:
    ']'
;

LeftBrace
:
    '{'
;

RightBrace
:
    '}'
;

Plus
:
    '+'
;

Minus
:
    '-'
;

Star
:
    '*'
;

Div
:
    '/'
;

Mod
:
    '%'
;

Caret
:
    '^'
;

And
:
    '&'
;

Or
:
    '|'
;

Tilde
:
    '~'
;

Not
:
    '!'
;

Assign
:
    '='
;

Less
:
    '<'
;

Greater
:
    '>'
;

PlusAssign
:
    '+='
;

MinusAssign
:
    '-='
;

StarAssign
:
    '*='
;

DivAssign
:
    '/='
;

ModAssign
:
    '%='
;

XorAssign
:
    '^='
;

AndAssign
:
    '&='
;

OrAssign
:
    '|='
;

LeftShift
:
    '<<'
;


LeftShiftAssign
:
    '<<='
;

Equal
:
    '=='
;

NotEqual
:
    '!='
;

LessEqual
:
    '<='
;

GreaterEqual
:
    '>='
;

AndAnd
:
    '&&'
;

OrOr
:
    '||'
;

PlusPlus
:
    '++'
;

MinusMinus
:
    '--'
;

UnaryCondition
:
    '?:'
;

Comma
:
    ','
;

ArrowStar
:
    '->*'
;

Arrow
:
    '->'
;

Question
:
    '?'
;

Colon
:
    ':'
;

Doublecolon
:
    '::'
;

Semi
:
    ';'
;

Dot
:
    '.'
;

DotStar
:
    '.*'
;

Ellipsis
:
    '...'
;

theoperator
:
    (
        New
        | Delete
        | '+'
        | '-'
        | '*'
        | '/'
        | '%'
        | '^'
        | '&'
        | '|'
        | '~'
        | '!'
        | '='
        | '<'
        | '>'
        | '+='
        | '-='
        | '*='
        | '/='
        | '%='
        | '^='
        | '&='
        | '|='
        | '<<'
        | '<<='
        | '=='
        | '!='
        | '<='
        | '>='
        | '&&'
        | '||'
        | '++'
        | '--'
        | ','
        | '->*'
        | '->'
        | '?:'
    )
    | New '[' ']'
    | Delete '[' ']'
    | Greater Greater Assign?
    | '(' ')'
    | '[' ']'
;

/*Lexer*/
fragment
Hexquad
:
    HEXADECIMALDIGIT HEXADECIMALDIGIT HEXADECIMALDIGIT HEXADECIMALDIGIT
;

fragment
Universalcharactername
:
    '\\u' Hexquad
    | '\\U' Hexquad Hexquad
;

Identifier
:
/*
    Identifiernondigit
    | Identifier Identifiernondigit
    | Identifier DIGIT
    */
    Identifiernondigit
    (
        Identifiernondigit
        | DIGIT
    )*
;

fragment
Identifiernondigit
:
    NONDIGIT
    | Universalcharactername
    /* other implementation defined characters*/
;

fragment
NONDIGIT
:
    [a-zA-Z_]
;

fragment
DIGIT
:
    [0-9]
;

Numberliteral
:
    (
        Decimalliteral
        | Octalliteral
        | Hexadecimalliteral
        | Binaryliteral
    ) Integersuffix?
    | Fractionalconstant Exponentpart? Floatingsuffix?
    | Digitsequence Exponentpart Floatingsuffix?
;

fragment
Fractionalconstant
:
    Digitsequence? '.' Digitsequence
    | Digitsequence '.'
;

fragment
Exponentpart
:
    'e' SIGN? Digitsequence
    | 'E' SIGN? Digitsequence
;

Decimalliteral
:
    NONZERODIGIT ('\''? DIGIT)*
;

Octalliteral
:
    '0'
    (
        '\''? OCTALDIGIT
    )*
;

Hexadecimalliteral
:
    (
        '0x'
        | '0X'
    ) HEXADECIMALDIGIT
    (
        '\''? HEXADECIMALDIGIT
    )*
;

Binaryliteral
:
    (
        '0b'
        | '0B'
    ) BINARYDIGIT
    (
        '\''? BINARYDIGIT
    )*
;

fragment
NONZERODIGIT
:
    [1-9]
;

fragment
OCTALDIGIT
:
    [0-7]
;

fragment
HEXADECIMALDIGIT
:
    [0-9a-fA-F]
;

fragment
BINARYDIGIT
:
    [01]
;

Integersuffix
:
    Unsignedsuffix (Longsuffix | Longlongsuffix)?
    | (Longsuffix | Longlongsuffix) Unsignedsuffix?
;

fragment
Unsignedsuffix
:
    [uU]
;

fragment
Longsuffix
:
    [lL]
;

fragment
Longlongsuffix
:
    'll'
    | 'LL'
;

Characterliteral
:
    '\'' Cchar+ '\''
    | 'u' '\'' Cchar+ '\''
    | 'U' '\'' Cchar+ '\''
    | 'L' '\'' Cchar+ '\''
;

fragment
Cchar
:
    ~['\\\r\n]
    | Escapesequence
    | Universalcharactername
;

fragment
Escapesequence
:
    Simpleescapesequence
    | Octalescapesequence
    | Hexadecimalescapesequence
;

fragment
Simpleescapesequence
:
    '\\\''
    | '\\"'
    | '\\?'
    | '\\\\'
    | '\\a'
    | '\\b'
    | '\\f'
    | '\\n'
    | '\\r'
    | '\\t'
    | '\\v'
;

fragment
Octalescapesequence
:
    '\\' OCTALDIGIT
    | '\\' OCTALDIGIT OCTALDIGIT
    | '\\' OCTALDIGIT OCTALDIGIT OCTALDIGIT
;

fragment
Hexadecimalescapesequence
:
    '\\x' HEXADECIMALDIGIT+
;

fragment
SIGN
:
    [+-]
;

fragment
Digitsequence
:
    DIGIT
    (
        '\''? DIGIT
    )*
;

fragment
Floatingsuffix
:
    [flFL]
;

Stringliteral
:
    Encodingprefix? '"' Schar* '"'
    | Encodingprefix? 'R' Rawstring
;

fragment
Encodingprefix
:
    'u8'
    | 'u'
    | 'U'
    | 'L'
;

fragment
Schar
:
    ~["\\\r\n]
    | Escapesequence
    | Universalcharactername
;

fragment
Rawstring /* '"' dcharsequence? '(' rcharsequence? ')' dcharsequence? '"' */
:
    '"' .*? '(' .*? ')' .*? '"'
;

Userdefinedliteral
:
    (
        Decimalliteral
        | Octalliteral
        | Hexadecimalliteral
        | Binaryliteral
        | Fractionalconstant Exponentpart?
        | Digitsequence Exponentpart
        | Characterliteral
    ) Udsuffix
;

Userdefinedstringliteral
:
    Stringliteral Udsuffix
;

fragment
Udsuffix
:
    Identifier
;

Whitespace
:
    [ \t]+ -> skip
;

Newline
:
    (
        '\r' '\n'?
        | '\n'
    ) -> skip
;

BlockComment
:
    '/*' .*? '*/' -> skip
;

LineComment
:
    '//' ~[\r\n]* -> skip
;
