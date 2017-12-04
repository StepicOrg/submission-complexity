/*
 [The "BSD licence"]
 Copyright (c) 2013 Sam Harwell
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** C 2011 grammar built from the C11 Spec */
grammar C;

primaryExpression
:
    (
        Identifier
        | Constant
        | StringLiteral+
    )
    | '(' expression ')'
    | genericSelection
    | '__extension__'? '(' '{' blockItem* '}' ')' // Blocks (GCC extension)
    | '__builtin_va_arg' '(' unaryExpression ',' typeName ')'
    | '__builtin_offsetof' '(' typeName ',' unaryExpression ')'
;

genericSelection
:
    '_Generic' '(' assignmentExpression (',' (typeName | 'default') ':' assignmentExpression)+ ')'
;

postOperation
:
      '[' expression ']'
    | call
    | ('.' | '->') Identifier
;

postfixExpression
:
    (
        primaryExpression
        | '__extension__'? '(' typeName ')' '{' initializerList ','? '}'
    ) postOperation*
;

// used in BRANCHES
call
:
    '(' argumentExpressionList? ')'
;

// used in ASSIGNMENTS
unaryIncDecExpression
:
    ('++' | '--') unaryExpression
    |  postfixUnaryIncDecExpression
;

postfixUnaryIncDecExpression
:
    postfixExpression ('++' | '--') | postfixUnaryIncDecExpression postOperation* ('++' | '--')
;

argumentExpressionList
:
    assignmentExpression (',' assignmentExpression)*
;

unaryExpression
:
      postfixExpression
    | unaryIncDecExpression
    | ('&' | '*' | '+' | '-' | '~' | '!') castExpression
    | 'sizeof' (unaryExpression | '(' typeName ')')
    | '_Alignof' '(' typeName ')'
    | '&&' Identifier // GCC extension address of label
;

castExpression
:
    unaryExpression
    | '__extension__'? '(' typeName ')' castExpression
    | DigitSequence // for
;

shiftExpression
:
    castExpression (('<<' | '>>' | '+' | '-' | '*' | '/' | '%') castExpression)*
;

// used in CONDITIONALS
relationalExpression
:
    shiftExpression
    | relationalExpression ('<' | '>' | '<=' | '>=') shiftExpression
;

// used in CONDITIONALS
equalityExpression
:
    relationalExpression
    | equalityExpression ('==' | '!=') relationalExpression
;

logicalOrExpression
:
    equalityExpression (('||' | '&&' | '|' | '^' | '&') equalityExpression)*
;

conditionalExpression
:
    ternaryConditionalExpression
    | unaryConditionalExpression
    | logicalOrExpression
;

// used in CONDITIONALS
ternaryConditionalExpression
:
    logicalOrExpression '?' expression ':' conditionalExpression
;

// used in CONDITIONALS
unaryConditionalExpression
:
    logicalOrExpression '?:' conditionalExpression
;

assignmentExpression
:
    conditionalExpression
    | unaryExpression assignmentOperator assignmentExpression
    | DigitSequence // for
;

// used in ASSIGNMENTS
assignmentOperator
:
    '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
;

expression
:
    assignmentExpression (',' assignmentExpression)*
;

declaration
:
    declarationSpecifier+ initDeclaratorList? ';'
    | staticAssertDeclaration
;

declarationSpecifier
:
    (StorageClassSpecifier | TypeQualifier)
    | typeSpecifier
    | functionSpecifier
    | alignmentSpecifier
;

initDeclaratorList
:
    initDeclarator (',' initDeclarator)*
;

initDeclarator
:
    declarator ('=' initializer)?
;

StorageClassSpecifier
:
    'typedef'
    | 'extern'
    | 'static'
    | '_Thread_local'
    | 'auto'
    | 'register'
;

typeSpecifier
:
    (
        'void'
        | 'char'
        | 'short'
        | 'int'
        | 'long'
        | 'float'
        | 'double'
        | 'signed'
        | 'unsigned'
        | '_Bool'
        | '_Complex'
        | '__m128'
        | '__m128d'
        | '__m128i'
        | '__extension__' '(' ('__m128' | '__m128d' | '__m128i') ')'
    )    
    | '_Atomic' '(' typeName ')'
    | structOrUnionSpecifier
    | 'enum' (Identifier? '{' enumerator (',' enumerator)* ','? '}' | Identifier)
    | Identifier
    | '__typeof__' '(' conditionalExpression ')' // GCC extension
;

structOrUnionSpecifier
:
    StructOrUnion (Identifier? '{' structDeclaration+ '}' | Identifier)
;

StructOrUnion
:
    'struct' | 'union'
;

structDeclaration
:
    specifierQualifierList (structDeclarator (',' structDeclarator)*)? ';'
    | staticAssertDeclaration
;

specifierQualifierList
:
    (typeSpecifier | TypeQualifier) specifierQualifierList?
;

structDeclarator
:
      declarator
    | declarator? ':' conditionalExpression
;

enumerator
:
    Identifier ('=' conditionalExpression)?
;

TypeQualifier
:
      'const'
    | 'restrict'
    | 'volatile'
    | '_Atomic'
;

functionSpecifier
:
    (
          'inline'
        | '_Noreturn'
        | '__inline__' // GCC extension
        | '__stdcall'
        | '__declspec' '(' Identifier ')'
    )
    | gccAttributeSpecifier
;

alignmentSpecifier
:
    '_Alignas' '(' typeName | conditionalExpression ')'
;

declarator
:
    pointer? directDeclarator gccDeclaratorExtension*
;

directDeclarator
:
    Identifier (':' DigitSequence)?
    | '(' declarator ')'
    | directDeclarator (
        '[' (
            TypeQualifier* (assignmentExpression? | '*')
            | ('static' TypeQualifier* ']' | TypeQualifier+ 'static') assignmentExpression
        ) ']'
        | '(' (parameterList (',' '...')? | identifierList?) ')'
    )
;

gccDeclaratorExtension
:
    '__asm' '(' StringLiteral+ ')'
    | gccAttributeSpecifier
;

gccAttributeSpecifier
:
    '__attribute__' '(' '(' gccAttributeList ')' ')'
;

gccAttributeList
:
    gccAttribute (',' gccAttribute)*
    | // empty
;

gccAttribute
:
    ~(',' | '(' | ')') ('(' argumentExpressionList? ')')?
    | // empty
;

nestedParenthesesBlock
:
    ( ~('(' | ')') | '(' nestedParenthesesBlock ')')*
;

pointer
:
    ('*' | '^') TypeQualifier* pointer?
;

parameterList
:
    parameterDeclaration (',' parameterDeclaration)*
;

parameterDeclaration
:
    declarationSpecifier+ (declarator | abstractDeclarator?)
;

identifierList
:
    Identifier (',' Identifier)*
;

typeName
:
    specifierQualifierList abstractDeclarator?
;

abstractDeclarator
:
    pointer
    | pointer? directAbstractDeclarator gccDeclaratorExtension*
;

directAbstractDeclarator
:
    '(' abstractDeclarator ')' gccDeclaratorExtension*
    | '[' (TypeQualifier* assignmentExpression?
        | ('static' TypeQualifier* | TypeQualifier+ 'static') assignmentExpression
        | '*'
    ) ']'
    | '(' (parameterList (',' '...')?)? ')' gccDeclaratorExtension*
    | directAbstractDeclarator (
        '[' (
            TypeQualifier* assignmentExpression?
            | ('static' TypeQualifier* | TypeQualifier+ 'static') assignmentExpression
            | '*'
        ) ']'
        | '(' (parameterList (',' '...')?)? ')' gccDeclaratorExtension*
    )
;

initializer
:
    assignmentExpression | '{' initializerList ','? '}'
;

initializerList
:
    (designator+ '=')? initializer (',' (designator+ '=')? initializer)*
;

designator
:
    '[' conditionalExpression ']'
    | '.' Identifier
;

staticAssertDeclaration
:
    '_Static_assert' '(' conditionalExpression ',' StringLiteral+ ')' ';'
;

statement
:
      Identifier ':' statement
    | caseStatement
    | '{' blockItem* '}'
    | expression? ';'
    | selectionStatement
    | iterationStatement
    | jumpStatement
    | ('__asm' | '__asm__') ('volatile' | '__volatile__') '(' (logicalOrExpression (',' logicalOrExpression)*)? (':' (logicalOrExpression (',' logicalOrExpression)*)?)* ')' ';'
;

// used in CONDITIONALS
caseStatement
:
    ('case' conditionalExpression | 'default') ':' statement
;

blockItem
:
    declaration
    | statement
;

selectionStatement
:
      'if' '(' expression ')' statement elseStatement?
    | 'switch' '(' expression ')' statement
;

// used in CONDITIONALS
elseStatement
:
    'else' statement
;

iterationStatement
:
      While '(' expression ')' statement
    | Do statement While '(' expression ')' ';'
    | For '(' forCondition ')' statement
;

forCondition
:
    (declarationSpecifier+ initDeclaratorList? | expression?) ';' forExpression? ';' forExpression?
;

forExpression
:
    assignmentExpression (',' assignmentExpression)*
;

jumpStatement
:
    gotoStatement
    | ('continue' | 'break') ';'
    | 'return' expression? ';'
;

// used in BRANCHES
gotoStatement
:
    'goto' (Identifier | unaryExpression) ';'
;

compilationUnit
:
    externalDeclaration* EOF
;

externalDeclaration
:
    declarationSpecifier* declarator declaration* '{' blockItem* '}'
    | declaration
    | ';' // stray ;
;

Auto : 'auto';
Break : 'break';
Case : 'case';
Char : 'char';
Const : 'const';
Continue : 'continue';
Default : 'default';
Do : 'do';
Double : 'double';
Else : 'else';
Enum : 'enum';
Extern : 'extern';
Float : 'float';
For : 'for';
Goto : 'goto';
If : 'if';
Inline : 'inline';
Int : 'int';
Long : 'long';
Register : 'register';
Restrict : 'restrict';
Return : 'return';
Short : 'short';
Signed : 'signed';
Sizeof : 'sizeof';
Static : 'static';
Struct : 'struct';
Switch : 'switch';
Typedef : 'typedef';
Union : 'union';
Unsigned : 'unsigned';
Void : 'void';
Volatile : 'volatile';
While : 'while';

Alignas : '_Alignas';
Alignof : '_Alignof';
Atomic : '_Atomic';
Bool : '_Bool';
Complex : '_Complex';
Generic : '_Generic';
Imaginary : '_Imaginary';
Noreturn : '_Noreturn';
StaticAssert : '_Static_assert';
ThreadLocal : '_Thread_local';

LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
LeftShift : '<<';
RightShift : '>>';

Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';

And : '&';
Or : '|';
AndAnd : '&&';
OrOr : '||';
Caret : '^';
Not : '!';
Tilde : '~';

Question : '?';
UnaryCondition: '?:';
Colon : ':';
Semi : ';';
Comma : ',';

Assign : '=';
// '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
StarAssign : '*=';
DivAssign : '/=';
ModAssign : '%=';
PlusAssign : '+=';
MinusAssign : '-=';
LeftShiftAssign : '<<=';
RightShiftAssign : '>>=';
AndAssign : '&=';
XorAssign : '^=';
OrAssign : '|=';

Equal : '==';
NotEqual : '!=';

Arrow : '->';
Dot : '.';
Ellipsis : '...';

Identifier
:
    IdentifierNondigit(IdentifierNondigit | Digit)*
;

fragment
IdentifierNondigit
:
    Nondigit
    | UniversalCharacterName
    //| // other implementation-defined characters...
;

fragment
Nondigit
:
    [a-zA-Z_]
;

fragment
Digit
:
    [0-9]
;

fragment
UniversalCharacterName
:
      '\\u' HexQuad
    | '\\U' HexQuad HexQuad
;

fragment
HexQuad
:
    HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit
;

Constant
:
      IntegerConstant
    | FloatingConstant
    //| EnumerationConstant
    | CharacterConstant
;

fragment
IntegerConstant
:
      DecimalConstant IntegerSuffix?
    | OctalConstant IntegerSuffix?
    | HexadecimalConstant IntegerSuffix?
    | BinaryConstant
;

fragment
BinaryConstant
:
    '0' [bB] [0-1]+
;

fragment
DecimalConstant
:
    NonzeroDigit Digit*
;

fragment
OctalConstant
:
    '0' OctalDigit*
;

fragment
HexadecimalConstant
:
    HexadecimalPrefix HexadecimalDigit+
;

fragment
HexadecimalPrefix
:
    '0' [xX]
;

fragment
NonzeroDigit
:
    [1-9]
;

fragment
OctalDigit
:
    [0-7]
;

fragment
HexadecimalDigit
:
    [0-9a-fA-F]
;

fragment
IntegerSuffix
:
      UnsignedSuffix (LongSuffix? | LongLongSuffix)
    | (LongSuffix | LongLongSuffix) UnsignedSuffix?
;

fragment
UnsignedSuffix
:
    [uU]
;

fragment
LongSuffix
:
    [lL]
;

fragment
LongLongSuffix
:
    'll' | 'LL'
;

fragment
FloatingConstant
:
      DecimalFloatingConstant
    | HexadecimalFloatingConstant
;

fragment
DecimalFloatingConstant
:
      FractionalConstant ExponentPart? FloatingSuffix?
    | DigitSequence ExponentPart FloatingSuffix?
;

fragment
HexadecimalFloatingConstant
:
      HexadecimalPrefix HexadecimalFractionalConstant BinaryExponentPart FloatingSuffix?
    | HexadecimalPrefix HexadecimalDigitSequence BinaryExponentPart FloatingSuffix?
;

fragment
FractionalConstant
:
      DigitSequence? '.' DigitSequence
    | DigitSequence '.'
;

fragment
ExponentPart
:
      ('e' | 'E') Sign? DigitSequence
;

fragment
Sign
:
    '+' | '-'
;

DigitSequence
:
    Digit+
;

fragment
HexadecimalFractionalConstant
:
      HexadecimalDigitSequence? '.' HexadecimalDigitSequence
    | HexadecimalDigitSequence '.'
;

fragment
BinaryExponentPart
:
      ('p' | 'P') Sign? DigitSequence
;

fragment
HexadecimalDigitSequence
:
    HexadecimalDigit+
;

fragment
FloatingSuffix
:
    'f' | 'l' | 'F' | 'L'
;

fragment
CharacterConstant
:
    ('\'' | 'L\'' | 'u\'' | 'U\'') CCharSequence '\''
;

fragment
CCharSequence
:
    CChar+
;

fragment
CChar
:
    ~['\\\r\n]
    | EscapeSequence
;

fragment
EscapeSequence
:
      SimpleEscapeSequence
    | OctalEscapeSequence
    | HexadecimalEscapeSequence
    | UniversalCharacterName
;

fragment
SimpleEscapeSequence
:
    '\\' ['"?abfnrtv\\]
;

fragment
OctalEscapeSequence
:
      '\\' OctalDigit (OctalDigit OctalDigit?)?
;

fragment
HexadecimalEscapeSequence
:
    '\\x' HexadecimalDigit+
;

StringLiteral
:
    EncodingPrefix? '"' SCharSequence? '"'
;

fragment
EncodingPrefix
:
      'u8'
    | 'u'
    | 'U'
    | 'L'
;

fragment
SCharSequence
:
    SChar+
;

fragment
SChar
:
      ~["\\\r\n]
    | EscapeSequence
    | '\\\n'   // Added line
    | '\\\r\n' // Added line
;

ComplexDefine
:
    '#' Whitespace? 'define'  ~[#]* -> skip
;

// ignore the following asm blocks:
AsmBlock
:
    'asm' ~'{'* '{' ~'}'* '}' -> skip
;
 
// ignore the lines generated by c preprocessor
LineAfterPreprocessing
:
    '#line' Whitespace* ~[\r\n]* -> skip
;

LineDirective
:
    '#' Whitespace? DecimalConstant Whitespace? StringLiteral ~[\r\n]* -> skip
;

PragmaDirective
:
    '#' Whitespace? 'pragma' Whitespace ~[\r\n]* -> skip
;

Whitespace
:
    [ \t]+ -> skip
;

Newline
:
    ('\r' '\n'? | '\n') -> skip
;

BlockComment
:
    '/*' .*? '*/' -> skip
;

LineComment
:
    '//' ~[\r\n]* -> skip
;
