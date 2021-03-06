/*
 * [The "BSD license"]
 *  Copyright (c) 2014 Terence Parr
 *  Copyright (c) 2014 Sam Harwell
 *  Copyright (c) 2017 Chan Chung Kwong
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 *  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 *  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 *  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 *  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 *  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/**
 * A Java 8 grammar for ANTLR 4 derived from the Java Language Specification
 * chapter 19.
 *
 * NOTE: This grammar results in a generated parser that is much slower
 *       than the Java 7 grammar in the grammars-v4/java directory. This
 *     one is, however, extremely close to the spec.
 *
 * You can test with
 *
 *  $ antlr4 Java9.g4
 *  $ javac *.java
 *  $ grun Java9 compilationUnit *.java
 *
 * Or,
~/antlr/code/grammars-v4/java9 $ java Test .
/Users/parrt/antlr/code/grammars-v4/java9/./Java9BaseListener.java
/Users/parrt/antlr/code/grammars-v4/java9/./Java9Lexer.java
/Users/parrt/antlr/code/grammars-v4/java9/./Java9Listener.java
/Users/parrt/antlr/code/grammars-v4/java9/./Java9Parser.java
/Users/parrt/antlr/code/grammars-v4/java9/./Test.java
Total lexer+parser time 30844ms.
~/antlr/code/grammars-v4/java9 $ java Test examples/module-info.java
/home/kwong/projects/grammars-v4/java9/examples/module-info.java
Total lexer+parser time 914ms.
~/antlr/code/grammars-v4/java9 $ java Test examples/TryWithResourceDemo.java
/home/kwong/projects/grammars-v4/java9/examples/TryWithResourceDemo.java
Total lexer+parser time 3634ms.
~/antlr/code/grammars-v4/java9 $ java Test examples/helloworld.java
/home/kwong/projects/grammars-v4/java9/examples/helloworld.java
Total lexer+parser time 2497ms.

 */
grammar Java9;

/*
 * Productions from §3 (Lexical Structure)
 */

Literal
:
    IntegerLiteral
    | FloatingPointLiteral
    | BooleanLiteral
    | CharacterLiteral
    | StringLiteral
    | NullLiteral
;

/*
 * Productions from §4 (Types, Values, and Variables)
 */

referenceType
:
    classOrInterfaceType
    | annotation* Identifier
    | arrayType
;

classOrInterfaceType
:
    annotation* Identifier typeArguments? ('.' annotation* Identifier typeArguments?)*
;

classType
:
    (classOrInterfaceType '.')? annotation* Identifier typeArguments?
;

arrayType
:
    (annotation* UnannPrimitiveType | classOrInterfaceType | annotation* Identifier) dims
;

dims
:
    (annotation* '[' ']')+
;

typeParameter
:
    annotation* Identifier ('extends' (annotation* Identifier | classOrInterfaceType ('&' classType)*))?
;

typeArguments
:
    '<' typeArgument (',' typeArgument)* '>'
;

typeArgument
:
    referenceType
    | annotation* '?' (('extends'|'super') referenceType)?
;

/*
 * Productions from §7 (Packages)
 */

compilationUnit
:
    (
        packageDeclaration? importDeclaration* typeDeclaration*
        | classBodyDeclaration*
        | importDeclaration* annotation* 'open'? 'module'  Identifier ('.' Identifier)* '{' moduleDirective* '}'
    ) EOF
;

packageDeclaration
:
    annotation* 'package' Identifier ('.' Identifier)* ';'
;

importDeclaration
:
    'import' (
        Identifier ('.' Identifier)*
        | (Identifier '.')+ '*'
        | 'static' (Identifier '.')+ (Identifier | '*')
    ) ';'
;

typeDeclaration
:
    normalClassDeclaration
    | enumDeclaration
    | normalInterfaceDeclaration
    | annotationTypeDeclaration
    | ';'
;

moduleDirective
:
    (
        ('requires' ('transitive' | 'static')* | 'uses')  Identifier ('.' Identifier)*
        | ('exports' | 'opens') Identifier ('.' Identifier)* ('to'  Identifier ('.' Identifier)* (',' Identifier ('.' Identifier)*)*)?
        | 'provides' Identifier ('.' Identifier)* 'with' Identifier ('.' Identifier)* (',' Identifier ('.' Identifier)*)*
    )';'
;

/*
 * Productions from §8 (Classes)
 */

normalClassDeclaration
:
    classModifier* 'class' Identifier typeParameters? ('extends' classType)? ('implements' classType (',' classType)*)? classBody
;

classModifier
:
    annotation
    | 'public'
    | 'protected'
    | 'private'
    | 'abstract'
    | 'static'
    | 'final'
    | 'strictfp'
;

typeParameters
:
    '<' typeParameter (',' typeParameter)* '>'
;

classBody
:
    '{' classBodyDeclaration* '}'
;

classBodyDeclaration
:
    fieldModifier* unannType variableDeclaratorList ';'
    | methodModifier* (typeParameters annotation*)? (unannType | 'void') Identifier '(' formalParameterList? ')' dims? throws_? ('{' blockStatement* '}' | ';')
    | normalClassDeclaration
    | enumDeclaration
    | normalInterfaceDeclaration
    | annotationTypeDeclaration
    | ';'
    | 'static'? '{' blockStatement* '}'
    | constructorModifier* typeParameters? Identifier '(' formalParameterList? ')' throws_? '{' explicitConstructorInvocation? blockStatement* '}'
;

fieldModifier
:
    annotation
    | 'public'
    | 'protected'
    | 'private'
    | 'static'
    | 'final'
    | 'transient'
    | 'volatile'
;

variableDeclaratorList
:
    variableDeclarator (',' variableDeclarator)*
;

variableDeclarator
:
    Identifier dims? ('=' variableInitializer)?
;

variableInitializer
:
    expression
    | '{' variableInitializerList? ','? '}'
;

unannType
:
    (
        UnannPrimitiveType
        | Identifier typeArguments? ('.' annotation* Identifier typeArguments?)*
    ) dims?
;

UnannPrimitiveType
:
    'byte'
    | 'short'
    | 'int'
    | 'long'
    | 'char'
    | 'float'
    | 'double'
    | 'boolean'
;

unannClassType
:
    Identifier typeArguments? ('.' annotation* Identifier typeArguments?)*
;

methodModifier
:
    annotation
    | 'public'
    | 'protected'
    | 'private'
    | 'abstract'
    | 'static'
    | 'final'
    | 'synchronized'
    | 'native'
    | 'strictfp'
;

formalParameterList
:
    (formalParameters ',')? lastFormalParameter
    | annotation* unannType (Identifier '.')? 'this'
;

formalParameters
:
    (formalParameter | annotation* unannType (Identifier '.')? 'this') (',' formalParameter)*
;

formalParameter
:
    variableModifier* unannType Identifier dims?
;

variableModifier
:
    annotation
    | 'final'
;

lastFormalParameter
:
    variableModifier* unannType annotation* '...' Identifier dims?
    | formalParameter
;

throws_
:
    'throws' exceptionType (',' exceptionType)*
;

exceptionType
:
    classType
    | annotation* Identifier
;

constructorModifier
:
    annotation
    | 'public'
    | 'protected'
    | 'private'
;

explicitConstructorInvocation
:
    (
        typeArguments? ('this'|'super')
        | ((Identifier '.')+ | primary '.') typeArguments? 'super'
    ) '(' argumentList? ')' ';'
;

enumDeclaration
:
    classModifier* 'enum' Identifier ('implements' classType (',' classType)*)?
    '{' (enumConstant (',' enumConstant)*)? ','? (';' classBodyDeclaration*)? '}'
;

enumConstant
:
    annotation* Identifier ('(' argumentList? ')')? classBody?
;

/*
 * Productions from §9 (Interfaces)
 */

normalInterfaceDeclaration
:
    interfaceModifier* 'interface' Identifier typeParameters? ('extends' classType (',' classType)*)? '{' interfaceMemberDeclaration* '}'
;

interfaceModifier
:
    annotation
    | 'public'
    | 'protected'
    | 'private'
    | 'abstract'
    | 'static'
    | 'strictfp'
;

interfaceMemberDeclaration
:
    constantModifier* unannType variableDeclaratorList ';'
    | interfaceMethodModifier* (typeParameters annotation*)? (unannType | 'void') Identifier '(' formalParameterList? ')' dims? throws_? ('{' blockStatement* '}' | ';')
    | normalClassDeclaration
    | enumDeclaration
    | normalInterfaceDeclaration
    | annotationTypeDeclaration
    | ';'
;

constantModifier
:
    annotation
    | 'public'
    | 'static'
    | 'final'
;

interfaceMethodModifier
:
    annotation
    | 'public'
    | 'private'//Introduced in Java 9
    | 'abstract'
    | 'default'
    | 'static'
    | 'strictfp'
;

annotationTypeDeclaration
:
    interfaceModifier* '@' 'interface' Identifier '{' annotationTypeMemberDeclaration* '}'
;

annotationTypeMemberDeclaration
:
    (annotation | 'public' | 'abstract')* unannType Identifier '(' ')' dims? ('default' elementValue)? ';'
    | constantModifier* unannType variableDeclaratorList ';'
    | normalClassDeclaration
    | enumDeclaration
    | normalInterfaceDeclaration
    | annotationTypeDeclaration
    | ';'
;

annotation
:
    '@' Identifier ('.' Identifier)* ('(' (Identifier '=' elementValue (',' Identifier '=' elementValue)*)? | elementValue ')')?
;

elementValue
:
    conditionalExpression
    | '{' (elementValue (',' elementValue)*)? ','? '}'
    | annotation
;

/*
 * Productions from §10 (Arrays)
 */

variableInitializerList
:
    variableInitializer (',' variableInitializer)*
;

/*
 * Productions from §14 (Blocks and Statements)
 */

blockStatement
:
    variableModifier* unannType variableDeclaratorList ';'
    | normalClassDeclaration
    | enumDeclaration
    | statement
;

statement
:
    statementWithoutTrailingSubstatement
    | Identifier ':' statement
    | ifStatement
    | whileStatement
    | forStatement
;

ifStatement:
      'if' '(' expression ')' statement
    | 'if' '(' expression ')' statementNoShortIf elseStatement
;

// used in BRANCHES
whileStatement:
    'while' '(' expression ')' statement
;

// used in BRANCHES
forStatement:
    'for' '(' (
        forInit? ';' expression? ';' statementExpressionList?
        | variableModifier* unannType Identifier dims? ':' expression
    ) ')' statement
;

statementNoShortIf
:
    statementWithoutTrailingSubstatement
    | Identifier ':' statementNoShortIf
    | ifStatementNoShortIf
    | whileStatementNoShortIf
    | forStatementNoShortIf
;

ifStatementNoShortIf:
    'if' '(' expression ')' statementNoShortIf elseStatementNoShortIf
;

// used in BRANCHES
whileStatementNoShortIf:
    'while' '(' expression ')' statementNoShortIf
;

// used in BRANCHES
forStatementNoShortIf:
    'for' '(' (
        forInit? ';' expression? ';' statementExpressionList? ')'
        | variableModifier* unannType Identifier dims? ':' expression
    ) ')' statementNoShortIf
;

statementWithoutTrailingSubstatement
:
    synchronizedStatement
    | ';'
    | statementExpression ';'
    | assertStatement
    | switchStatement
    | doStatement
    | breakAndContinueStatement
    | returnStatement
    | throwStatement
    | tryStatement
;

// used in BRANCHES
synchronizedStatement:
    ('synchronized' '(' expression ')')? '{' blockStatement* '}'
;

// used in BRANCHES
assertStatement:
    'assert' expression (':' expression)? ';'
;

// used in CONDITIONALS
switchStatement:
    'switch' '(' expression ')' '{' (switchLabel+ blockStatement+)* switchLabel* '}'
;

// used in BRANCHES
doStatement:
    'do' statement 'while' '(' expression ')' ';'
;

// used in BRANCHES
breakAndContinueStatement:
    ('break' | 'continue') Identifier? ';'
;

// used in BRANCHES
returnStatement:
    'return' expression? ';'
;

// used in BRANCHES
throwStatement:
    'throw' expression ';'
;

statementExpression
:
    assignment
    | preIncrementDecrementExpression
    | postIncrementDecrementExpression
    | methodInvocation
    | classInstanceCreationExpression
;

// used in CONDITIONALS
elseStatement
:
    'else' statement
;

// used in CONDITIONALS
elseStatementNoShortIf
:
    'else' statementNoShortIf
;

// used in CONDITIONALS
switchLabel
:
    ('case' (expression | Identifier) | 'default') ':'
;

forInit
:
    statementExpressionList
    | variableModifier* unannType variableDeclaratorList
;

statementExpressionList
:
    statementExpression (',' statementExpression)*
;

// used in CONDITIONALS
tryStatement
:
    'try' (
        '{' blockStatement* '}' (catchClause+ | catchClause* 'finally' '{' blockStatement* '}')
        | '(' resource (';' resource)* ';'? ')' '{' blockStatement* '}' catchClause* ('finally' '{' blockStatement* '}')?
    )
;

// used in CONDITIONALS
catchClause
:
    'catch' '(' variableModifier* unannClassType ('|' classType)* Identifier dims? ')' '{' blockStatement* '}'
;

resource
:
    variableModifier* unannType Identifier dims? '=' expression
    | (Identifier ('.' Identifier)* | (primary | (Identifier '.')* 'super') '.' Identifier)//Introduced in Java 9
;


/*
 * Productions from §15 (Expressions)
 */

primary
:
    (primaryNoNewArray_lfno_primary | arrayCreationExpression) (
        (
            classInstanceCreationExpression_lf_primary
            | ('.' | '::' typeArguments?) Identifier
            | methodInvocation_lf_primary
        ) ('[' expression ']')*
    )*
;

primaryNoNewArray_lfno_arrayAccess
:
    Literal
    | (Identifier ('.' Identifier)* ('[' ']')* | 'void') '.' 'class'
    | (Identifier '.')* 'this'
    | '(' expression ')'
    | classInstanceCreationExpression
    | (primary | (Identifier '.')* 'super') '.' Identifier
    | methodInvocation
    | (
        Identifier ('.' Identifier)*
        | referenceType
        | primary
        | (Identifier '.')* 'super'
    ) '::' typeArguments? Identifier
    | (classType '::' typeArguments? | arrayType '::') 'new'
;

primaryNoNewArray_lfno_primary
:
    (
        Literal
        | ((Identifier ('.' Identifier)* | UnannPrimitiveType) ('[' ']')* | 'void') '.' 'class'
        | (Identifier '.')* ('this' | 'super' '.' Identifier)
        | '(' expression ')'
        | classInstanceCreationExpression_lfno_primary
        | Identifier ('.' Identifier)* '[' expression ']'
        | methodInvocation_lfno_primary
        | (
            Identifier ('.' Identifier)*
            | referenceType
            | (Identifier '.')* 'super'
        ) '::' typeArguments? Identifier
        | (classType '::' typeArguments? | arrayType '::') 'new'
    ) ('[' expression ']')*
;

// used in BRANCHES
classInstanceCreationExpression
:
    (
        'new' typeArguments? annotation* Identifier ('.' annotation* Identifier)*
        | (Identifier ('.' Identifier)* | primary) '.' 'new' typeArguments? annotation* Identifier
    ) typeArgumentsOrDiamond? '(' argumentList? ')' classBody?
;

// used in BRANCHES
classInstanceCreationExpression_lf_primary
:
    '.' 'new' typeArguments? annotation* Identifier typeArgumentsOrDiamond? '(' argumentList? ')' classBody?
;

// used in BRANCHES
classInstanceCreationExpression_lfno_primary
:
    (
        'new' typeArguments? annotation* Identifier ('.' annotation* Identifier)*
        | (Identifier '.')+ 'new' typeArguments? annotation* Identifier
    ) typeArgumentsOrDiamond? '(' argumentList? ')' classBody?
;

typeArgumentsOrDiamond
:
    typeArguments
    | '<' '>'
;

// used in BRANCHES
methodInvocation
:
    (
        Identifier
        | (
            (Identifier '.')+
            | (Identifier '.')* 'super' '.'
            | primary '.'
        ) typeArguments? Identifier
    ) '(' argumentList? ')'
;

// used in BRANCHES
methodInvocation_lf_primary
:
    '.' typeArguments? Identifier '(' argumentList? ')'
;

// used in BRANCHES
methodInvocation_lfno_primary
:
    (((Identifier '.')+ | (Identifier '.')* 'super' '.') typeArguments?)? Identifier '(' argumentList? ')'
;

argumentList
:
    expression (',' expression)*
;

// used in BRANCHES
arrayCreationExpression
:
    'new' (annotation* UnannPrimitiveType | classOrInterfaceType) ((annotation* '[' expression ']')+ dims? |  dims '{' variableInitializerList? ','? '}')
;

expression
:
    lambdaExpression
    | conditionalExpression
    | assignment
;

lambdaExpression
:
    (Identifier | '(' (formalParameterList? | Identifier (',' Identifier)*) ')') '->'
    (expression | '{' blockStatement* '}')
;

assignment
:
    (
        Identifier ('.' Identifier)* ('[' expression ']')*
        | (primary | (Identifier '.')* 'super') '.' Identifier
        | primaryNoNewArray_lfno_arrayAccess ('[' expression ']')+
    ) assignmentOperator expression
;

// used in ASSIGNMENTS
assignmentOperator
:
    '='
    | '*='
    | '/='
    | '%='
    | '+='
    | '-='
    | '<<='
    | '>>='
    | '>>>='
    | '&='
    | '^='
    | '|='
;

conditionalExpression
:
    conditionalOrExpression
    | ternaryConditionalExpression
;

// used in CONDITIONALS
ternaryConditionalExpression
:
    conditionalOrExpression '?' expression ':' (conditionalExpression | lambdaExpression)
;

conditionalOrExpression
:
    equalityExpression (('||' | '&&' | '^' | '&' | '|') equalityExpression)*
;

// used in CONDITIONALS
equalityExpression
:
    relationalExpression
    | equalityExpression ('==' | '!=') relationalExpression
;


relationalExpression
:
    comparision
    | shiftExpression
;

// used in CONDITIONALS
comparision
:
    shiftExpression (
        ('<' | '>' | '<=' | '>=') shiftExpression
        | 'instanceof' referenceType
    )
    | comparision (
        ('<' | '>' | '<=' | '>=') shiftExpression
        |'instanceof' referenceType
    )
;

shiftExpression
:
    unaryExpression (('<' '<' | '>' '>' '>'? | '+' | '-' | '*' | '/' | '%') unaryExpression)*
;

unaryExpression
:
    preIncrementDecrementExpression
    | ('+' | '-') unaryExpression
    | unaryExpressionNotPlusMinus
;

// used in ASSIGNMENTS
preIncrementDecrementExpression
:
    ('++' | '--') unaryExpression
;

unaryExpressionNotPlusMinus
:
    (primary | Identifier ('.' Identifier)*) ('++' | '--')*
    | ('~' | '!' | '(' annotation* UnannPrimitiveType ')') unaryExpression
    | '(' referenceType ('&' classType)* ')' (unaryExpressionNotPlusMinus | lambdaExpression)
;


// used in ASSIGNMENTS
postIncrementDecrementExpression
:
    (primary | Identifier ('.' Identifier)*) ('++' | '--')+
;

// LEXER

// §3.9 Keywords

ABSTRACT : 'abstract';
ASSERT : 'assert';
BOOLEAN : 'boolean';
BREAK : 'break';
BYTE : 'byte';
CASE : 'case';
CATCH : 'catch';
CHAR : 'char';
CLASS : 'class';
CONST : 'const';
CONTINUE : 'continue';
DEFAULT : 'default';
DO : 'do';
DOUBLE : 'double';
ELSE : 'else';
ENUM : 'enum';
EXTENDS : 'extends';
FINAL : 'final';
FINALLY : 'finally';
FLOAT : 'float';
FOR : 'for';
IF : 'if';
GOTO : 'goto';
IMPLEMENTS : 'implements';
IMPORT : 'import';
INSTANCEOF : 'instanceof';
INT : 'int';
INTERFACE : 'interface';
LONG : 'long';
NATIVE : 'native';
NEW : 'new';
PACKAGE : 'package';
PRIVATE : 'private';
PROTECTED : 'protected';
PUBLIC : 'public';
RETURN : 'return';
SHORT : 'short';
STATIC : 'static';
STRICTFP : 'strictfp';
SUPER : 'super';
SWITCH : 'switch';
SYNCHRONIZED : 'synchronized';
THIS : 'this';
THROW : 'throw';
THROWS : 'throws';
TRANSIENT : 'transient';
TRY : 'try';
VOID : 'void';
VOLATILE : 'volatile';
WHILE : 'while';
UNDER_SCORE : '_';//Introduced in Java 9

// §3.10.1 Integer Literals

IntegerLiteral
:
    DecimalIntegerLiteral
    | HexIntegerLiteral
    | OctalIntegerLiteral
    | BinaryIntegerLiteral
;

fragment
DecimalIntegerLiteral
:
    DecimalNumeral IntegerTypeSuffix?
;

fragment
HexIntegerLiteral
:
    HexNumeral IntegerTypeSuffix?
;

fragment
OctalIntegerLiteral
:
    OctalNumeral IntegerTypeSuffix?
;

fragment
BinaryIntegerLiteral
:
    BinaryNumeral IntegerTypeSuffix?
;

fragment
IntegerTypeSuffix
:
    [lL]
;

fragment
DecimalNumeral
:
    '0'
    | NonZeroDigit (Digits? | Underscores Digits)
;

fragment
Digits
:
    Digit (DigitsAndUnderscores? Digit)?
;

fragment
Digit
:
    '0'
    | NonZeroDigit
;

fragment
NonZeroDigit
:
    [1-9]
;

fragment
DigitsAndUnderscores
:
    DigitOrUnderscore+
;

fragment
DigitOrUnderscore
:
    Digit
    | '_'
;

fragment
Underscores
:
    '_'+
;

fragment
HexNumeral
:
    '0' [xX] HexDigits
;

fragment
HexDigits
:
    HexDigit (HexDigitsAndUnderscores? HexDigit)?
;

fragment
HexDigit
:
    [0-9a-fA-F]
;

fragment
HexDigitsAndUnderscores
:
    HexDigitOrUnderscore+
;

fragment
HexDigitOrUnderscore
:
    HexDigit
    | '_'
;

fragment
OctalNumeral
:
    '0' Underscores? OctalDigits
;

fragment
OctalDigits
:
    OctalDigit (OctalDigitsAndUnderscores? OctalDigit)?
;

fragment
OctalDigit
:
    [0-7]
;

fragment
OctalDigitsAndUnderscores
:
    OctalDigitOrUnderscore+
;

fragment
OctalDigitOrUnderscore
:
    OctalDigit
    | '_'
;

fragment
BinaryNumeral
:
    '0' [bB] BinaryDigits
;

fragment
BinaryDigits
:
    BinaryDigit (BinaryDigitsAndUnderscores? BinaryDigit)?
;

fragment
BinaryDigit
:
    [01]
;

fragment
BinaryDigitsAndUnderscores
:
    BinaryDigitOrUnderscore+
;

fragment
BinaryDigitOrUnderscore
:
    BinaryDigit
    | '_'
;

// §3.10.2 Floating-Point Literals

FloatingPointLiteral
:
    DecimalFloatingPointLiteral
    | HexadecimalFloatingPointLiteral
;

fragment
DecimalFloatingPointLiteral
:
    Digits '.' Digits? ExponentPart? FloatTypeSuffix?
    | '.' Digits ExponentPart? FloatTypeSuffix?
    | Digits ExponentPart FloatTypeSuffix?
    | Digits FloatTypeSuffix
;

fragment
ExponentPart
:
    ExponentIndicator SignedInteger
;

fragment
ExponentIndicator
:
    [eE]
;

fragment
SignedInteger
:
    Sign? Digits
;

fragment
Sign
:
    [+-]
;

fragment
FloatTypeSuffix
:
    [fFdD]
;

fragment
HexadecimalFloatingPointLiteral
:
    HexSignificand BinaryExponent FloatTypeSuffix?
;

fragment
HexSignificand
:
    HexNumeral '.'?
    | '0' [xX] HexDigits? '.' HexDigits
;

fragment
BinaryExponent
:
    BinaryExponentIndicator SignedInteger
;

fragment
BinaryExponentIndicator
:
    [pP]
;

// §3.10.3 Boolean Literals

BooleanLiteral
:
    'true'
    | 'false'
;

// §3.10.4 Character Literals

CharacterLiteral
:
    '\'' SingleCharacter '\''
    | '\'' EscapeSequence '\''
;

fragment
SingleCharacter
:
    ~['\\\r\n]
;

// §3.10.5 String Literals

StringLiteral
:
    '"' StringCharacters? '"'
;

fragment
StringCharacters
:
    StringCharacter+
;

fragment
StringCharacter
:
    ~["\\\r\n]
    | EscapeSequence
;

// §3.10.6 Escape Sequences for Character and String Literals

fragment
EscapeSequence
:
    '\\' [btnfr"'\\]
    | OctalEscape
    |   UnicodeEscape // This is not in the spec but prevents having to preprocess the input
;

fragment
OctalEscape
:
    '\\' OctalDigit
    | '\\' OctalDigit OctalDigit
    | '\\' ZeroToThree OctalDigit OctalDigit
;

fragment
ZeroToThree
:
    [0-3]
;

// This is not in the spec but prevents having to preprocess the input
fragment
UnicodeEscape
:
   '\\' 'u'+ HexDigit HexDigit HexDigit HexDigit
;

// §3.10.7 The Null Literal

NullLiteral
:
    'null'
;

// §3.11 Separators

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI : ';';
COMMA : ',';
DOT : '.';
ELLIPSIS : '...';
AT : '@';
COLONCOLON : '::';


// §3.12 Operators

ASSIGN : '=';
GT : '>';
LT : '<';
BANG : '!';
TILDE : '~';
QUESTION : '?';
COLON : ':';
ARROW : '->';
EQUAL : '==';
LE : '<=';
GE : '>=';
NOTEQUAL : '!=';
AND : '&&';
OR : '||';
INC : '++';
DEC : '--';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
BITAND : '&';
BITOR : '|';
CARET : '^';
MOD : '%';
//LSHIFT : '<<';
//RSHIFT : '>>';
//URSHIFT : '>>>';

ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MUL_ASSIGN : '*=';
DIV_ASSIGN : '/=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
MOD_ASSIGN : '%=';
LSHIFT_ASSIGN : '<<=';
RSHIFT_ASSIGN : '>>=';
URSHIFT_ASSIGN : '>>>=';

// §3.8 Identifiers (must appear after all keywords in the grammar)

Identifier
:
    JavaLetter JavaLetterOrDigit*
;

fragment
JavaLetter
:
    '_'
    | '$'
    | [A-Z]
    | [a-z]
    | '\u00AA'
    | '\u00B5'
    | '\u00BA'
    | [\u00C0-\u00D6]
    | [\u00D8-\u00F6]
    | [\u00F8-\u01BA]
    | '\u01BB'
    | [\u01BC-\u01BF]
    | [\u01C0-\u01C3]
    | [\u01C4-\u0241]
    | [\u0250-\u02AF]
    | [\u02B0-\u02C1]
    | [\u02C6-\u02D1]
    | [\u02E0-\u02E4]
    | '\u02EE'
    | '\u037A'
    | '\u0386'
    | [\u0388-\u038A]
    | '\u038C'
    | [\u038E-\u03A1]
    | [\u03A3-\u03CE]
    | [\u03D0-\u03F5]
    | [\u03F7-\u0481]
    | [\u048A-\u04CE]
    | [\u04D0-\u04F9]
    | [\u0500-\u050F]
    | [\u0531-\u0556]
    | '\u0559'
    | [\u0561-\u0587]
    | [\u05D0-\u05EA]
    | [\u05F0-\u05F2]
    | [\u0621-\u063A]
    | '\u0640'
    | [\u0641-\u064A]
    | [\u066E-\u066F]
    | [\u0671-\u06D3]
    | '\u06D5'
    | [\u06E5-\u06E6]
    | [\u06EE-\u06EF]
    | [\u06FA-\u06FC]
    | '\u06FF'
    | '\u0710'
    | [\u0712-\u072F]
    | [\u074D-\u076D]
    | [\u0780-\u07A5]
    | '\u07B1'
    | [\u0904-\u0939]
    | '\u093D'
    | '\u0950'
    | [\u0958-\u0961]
    | '\u097D'
    | [\u0985-\u098C]
    | [\u098F-\u0990]
    | [\u0993-\u09A8]
    | [\u09AA-\u09B0]
    | '\u09B2'
    | [\u09B6-\u09B9]
    | '\u09BD'
    | '\u09CE'
    | [\u09DC-\u09DD]
    | [\u09DF-\u09E1]
    | [\u09F0-\u09F1]
    | [\u0A05-\u0A0A]
    | [\u0A0F-\u0A10]
    | [\u0A13-\u0A28]
    | [\u0A2A-\u0A30]
    | [\u0A32-\u0A33]
    | [\u0A35-\u0A36]
    | [\u0A38-\u0A39]
    | [\u0A59-\u0A5C]
    | '\u0A5E'
    | [\u0A72-\u0A74]
    | [\u0A85-\u0A8D]
    | [\u0A8F-\u0A91]
    | [\u0A93-\u0AA8]
    | [\u0AAA-\u0AB0]
    | [\u0AB2-\u0AB3]
    | [\u0AB5-\u0AB9]
    | '\u0ABD'
    | '\u0AD0'
    | [\u0AE0-\u0AE1]
    | [\u0B05-\u0B0C]
    | [\u0B0F-\u0B10]
    | [\u0B13-\u0B28]
    | [\u0B2A-\u0B30]
    | [\u0B32-\u0B33]
    | [\u0B35-\u0B39]
    | '\u0B3D'
    | [\u0B5C-\u0B5D]
    | [\u0B5F-\u0B61]
    | '\u0B71'
    | '\u0B83'
    | [\u0B85-\u0B8A]
    | [\u0B8E-\u0B90]
    | [\u0B92-\u0B95]
    | [\u0B99-\u0B9A]
    | '\u0B9C'
    | [\u0B9E-\u0B9F]
    | [\u0BA3-\u0BA4]
    | [\u0BA8-\u0BAA]
    | [\u0BAE-\u0BB9]
    | [\u0C05-\u0C0C]
    | [\u0C0E-\u0C10]
    | [\u0C12-\u0C28]
    | [\u0C2A-\u0C33]
    | [\u0C35-\u0C39]
    | [\u0C60-\u0C61]
    | [\u0C85-\u0C8C]
    | [\u0C8E-\u0C90]
    | [\u0C92-\u0CA8]
    | [\u0CAA-\u0CB3]
    | [\u0CB5-\u0CB9]
    | '\u0CBD'
    | '\u0CDE'
    | [\u0CE0-\u0CE1]
    | [\u0D05-\u0D0C]
    | [\u0D0E-\u0D10]
    | [\u0D12-\u0D28]
    | [\u0D2A-\u0D39]
    | [\u0D60-\u0D61]
    | [\u0D85-\u0D96]
    | [\u0D9A-\u0DB1]
    | [\u0DB3-\u0DBB]
    | '\u0DBD'
    | [\u0DC0-\u0DC6]
    | [\u0E01-\u0E30]
    | [\u0E32-\u0E33]
    | [\u0E40-\u0E45]
    | '\u0E46'
    | [\u0E81-\u0E82]
    | '\u0E84'
    | [\u0E87-\u0E88]
    | '\u0E8A'
    | '\u0E8D'
    | [\u0E94-\u0E97]
    | [\u0E99-\u0E9F]
    | [\u0EA1-\u0EA3]
    | '\u0EA5'
    | '\u0EA7'
    | [\u0EAA-\u0EAB]
    | [\u0EAD-\u0EB0]
    | [\u0EB2-\u0EB3]
    | '\u0EBD'
    | [\u0EC0-\u0EC4]
    | '\u0EC6'
    | [\u0EDC-\u0EDD]
    | '\u0F00'
    | [\u0F40-\u0F47]
    | [\u0F49-\u0F6A]
    | [\u0F88-\u0F8B]
    | [\u1000-\u1021]
    | [\u1023-\u1027]
    | [\u1029-\u102A]
    | [\u1050-\u1055]
    | [\u10A0-\u10C5]
    | [\u10D0-\u10FA]
    | '\u10FC'
    | [\u1100-\u1159]
    | [\u115F-\u11A2]
    | [\u11A8-\u11F9]
    | [\u1200-\u1248]
    | [\u124A-\u124D]
    | [\u1250-\u1256]
    | '\u1258'
    | [\u125A-\u125D]
    | [\u1260-\u1288]
    | [\u128A-\u128D]
    | [\u1290-\u12B0]
    | [\u12B2-\u12B5]
    | [\u12B8-\u12BE]
    | '\u12C0'
    | [\u12C2-\u12C5]
    | [\u12C8-\u12D6]
    | [\u12D8-\u1310]
    | [\u1312-\u1315]
    | [\u1318-\u135A]
    | [\u1380-\u138F]
    | [\u13A0-\u13F4]
    | [\u1401-\u166C]
    | [\u166F-\u1676]
    | [\u1681-\u169A]
    | [\u16A0-\u16EA]
    | [\u16EE-\u16F0]
    | [\u1700-\u170C]
    | [\u170E-\u1711]
    | [\u1720-\u1731]
    | [\u1740-\u1751]
    | [\u1760-\u176C]
    | [\u176E-\u1770]
    | [\u1780-\u17B3]
    | '\u17D7'
    | '\u17DC'
    | [\u1820-\u1842]
    | '\u1843'
    | [\u1844-\u1877]
    | [\u1880-\u18A8]
    | [\u1900-\u191C]
    | [\u1950-\u196D]
    | [\u1970-\u1974]
    | [\u1980-\u19A9]
    | [\u19C1-\u19C7]
    | [\u1A00-\u1A16]
    | [\u1D00-\u1D2B]
    | [\u1D2C-\u1D61]
    | [\u1D62-\u1D77]
    | '\u1D78'
    | [\u1D79-\u1D9A]
    | [\u1D9B-\u1DBF]
    | [\u1E00-\u1E9B]
    | [\u1EA0-\u1EF9]
    | [\u1F00-\u1F15]
    | [\u1F18-\u1F1D]
    | [\u1F20-\u1F45]
    | [\u1F48-\u1F4D]
    | [\u1F50-\u1F57]
    | '\u1F59'
    | '\u1F5B'
    | '\u1F5D'
    | [\u1F5F-\u1F7D]
    | [\u1F80-\u1FB4]
    | [\u1FB6-\u1FBC]
    | '\u1FBE'
    | [\u1FC2-\u1FC4]
    | [\u1FC6-\u1FCC]
    | [\u1FD0-\u1FD3]
    | [\u1FD6-\u1FDB]
    | [\u1FE0-\u1FEC]
    | [\u1FF2-\u1FF4]
    | [\u1FF6-\u1FFC]
    | '\u2071'
    | '\u207F'
    | [\u2090-\u2094]
    | '\u2102'
    | '\u2107'
    | [\u210A-\u2113]
    | '\u2115'
    | '\u2118'
    | [\u2119-\u211D]
    | '\u2124'
    | '\u2126'
    | '\u2128'
    | [\u212A-\u212D]
    | '\u212E'
    | [\u212F-\u2131]
    | [\u2133-\u2134]
    | [\u2135-\u2138]
    | '\u2139'
    | [\u213C-\u213F]
    | [\u2145-\u2149]
    | [\u2160-\u2183]
    | [\u2C00-\u2C2E]
    | [\u2C30-\u2C5E]
    | [\u2C80-\u2CE4]
    | [\u2D00-\u2D25]
    | [\u2D30-\u2D65]
    | '\u2D6F'
    | [\u2D80-\u2D96]
    | [\u2DA0-\u2DA6]
    | [\u2DA8-\u2DAE]
    | [\u2DB0-\u2DB6]
    | [\u2DB8-\u2DBE]
    | [\u2DC0-\u2DC6]
    | [\u2DC8-\u2DCE]
    | [\u2DD0-\u2DD6]
    | [\u2DD8-\u2DDE]
    | '\u3005'
    | '\u3006'
    | '\u3007'
    | [\u3021-\u3029]
    | [\u3031-\u3035]
    | [\u3038-\u303A]
    | '\u303B'
    | '\u303C'
    | [\u3041-\u3096]
    | [\u309B-\u309C]
    | [\u309D-\u309E]
    | '\u309F'
    | [\u30A1-\u30FA]
    | [\u30FC-\u30FE]
    | '\u30FF'
    | [\u3105-\u312C]
    | [\u3131-\u318E]
    | [\u31A0-\u31B7]
    | [\u31F0-\u31FF]
    | [\u3400-\u4DB5]
    | [\u4E00-\u9FBB]
    | [\uA000-\uA014]
    | '\uA015'
    | [\uA016-\uA48C]
    | [\uA800-\uA801]
    | [\uA803-\uA805]
    | [\uA807-\uA80A]
    | [\uA80C-\uA822]
    | [\uAC00-\uD7A3]
    | [\uF900-\uFA2D]
    | [\uFA30-\uFA6A]
    | [\uFA70-\uFAD9]
    | [\uFB00-\uFB06]
    | [\uFB13-\uFB17]
    | '\uFB1D'
    | [\uFB1F-\uFB28]
    | [\uFB2A-\uFB36]
    | [\uFB38-\uFB3C]
    | '\uFB3E'
    | [\uFB40-\uFB41]
    | [\uFB43-\uFB44]
    | [\uFB46-\uFBB1]
    | [\uFBD3-\uFD3D]
    | [\uFD50-\uFD8F]
    | [\uFD92-\uFDC7]
    | [\uFDF0-\uFDFB]
    | [\uFE70-\uFE74]
    | [\uFE76-\uFEFC]
    | [\uFF21-\uFF3A]
    | [\uFF41-\uFF5A]
    | [\uFF66-\uFF6F]
    | '\uFF70'
    | [\uFF71-\uFF9D]
    | [\uFF9E-\uFF9F]
    | [\uFFA0-\uFFBE]
    | [\uFFC2-\uFFC7]
    | [\uFFCA-\uFFCF]
    | [\uFFD2-\uFFD7]
    | [\uFFDA-\uFFDC]
;

fragment
JavaLetterOrDigit
:
    JavaLetter
    | [0-9]
    | [\u0300-\u036F]
    | [\u0483-\u0486]
    | [\u0591-\u05B9]
    | [\u05BB-\u05BD]
    | '\u05BF'
    | [\u05C1-\u05C2]
    | [\u05C4-\u05C5]
    | '\u05C7'
    | [\u0610-\u0615]
    | [\u064B-\u065E]
    | [\u0660-\u0669]
    | '\u0670'
    | [\u06D6-\u06DC]
    | [\u06DF-\u06E4]
    | [\u06E7-\u06E8]
    | [\u06EA-\u06ED]
    | [\u06F0-\u06F9]
    | '\u0711'
    | [\u0730-\u074A]
    | [\u07A6-\u07B0]
    | [\u0901-\u0902]
    | '\u0903'
    | '\u093C'
    | [\u093E-\u0940]
    | [\u0941-\u0948]
    | [\u0949-\u094C]
    | '\u094D'
    | [\u0951-\u0954]
    | [\u0962-\u0963]
    | [\u0966-\u096F]
    | '\u0981'
    | [\u0982-\u0983]
    | '\u09BC'
    | [\u09BE-\u09C0]
    | [\u09C1-\u09C4]
    | [\u09C7-\u09C8]
    | [\u09CB-\u09CC]
    | '\u09CD'
    | '\u09D7'
    | [\u09E2-\u09E3]
    | [\u09E6-\u09EF]
    | [\u0A01-\u0A02]
    | '\u0A03'
    | '\u0A3C'
    | [\u0A3E-\u0A40]
    | [\u0A41-\u0A42]
    | [\u0A47-\u0A48]
    | [\u0A4B-\u0A4D]
    | [\u0A66-\u0A6F]
    | [\u0A70-\u0A71]
    | [\u0A81-\u0A82]
    | '\u0A83'
    | '\u0ABC'
    | [\u0ABE-\u0AC0]
    | [\u0AC1-\u0AC5]
    | [\u0AC7-\u0AC8]
    | '\u0AC9'
    | [\u0ACB-\u0ACC]
    | '\u0ACD'
    | [\u0AE2-\u0AE3]
    | [\u0AE6-\u0AEF]
    | '\u0B01'
    | [\u0B02-\u0B03]
    | '\u0B3C'
    | '\u0B3E'
    | '\u0B3F'
    | '\u0B40'
    | [\u0B41-\u0B43]
    | [\u0B47-\u0B48]
    | [\u0B4B-\u0B4C]
    | '\u0B4D'
    | '\u0B56'
    | '\u0B57'
    | [\u0B66-\u0B6F]
    | '\u0B82'
    | [\u0BBE-\u0BBF]
    | '\u0BC0'
    | [\u0BC1-\u0BC2]
    | [\u0BC6-\u0BC8]
    | [\u0BCA-\u0BCC]
    | '\u0BCD'
    | '\u0BD7'
    | [\u0BE6-\u0BEF]
    | [\u0C01-\u0C03]
    | [\u0C3E-\u0C40]
    | [\u0C41-\u0C44]
    | [\u0C46-\u0C48]
    | [\u0C4A-\u0C4D]
    | [\u0C55-\u0C56]
    | [\u0C66-\u0C6F]
    | [\u0C82-\u0C83]
    | '\u0CBC'
    | '\u0CBE'
    | '\u0CBF'
    | [\u0CC0-\u0CC4]
    | '\u0CC6'
    | [\u0CC7-\u0CC8]
    | [\u0CCA-\u0CCB]
    | [\u0CCC-\u0CCD]
    | [\u0CD5-\u0CD6]
    | [\u0CE6-\u0CEF]
    | [\u0D02-\u0D03]
    | [\u0D3E-\u0D40]
    | [\u0D41-\u0D43]
    | [\u0D46-\u0D48]
    | [\u0D4A-\u0D4C]
    | '\u0D4D'
    | '\u0D57'
    | [\u0D66-\u0D6F]
    | [\u0D82-\u0D83]
    | '\u0DCA'
    | [\u0DCF-\u0DD1]
    | [\u0DD2-\u0DD4]
    | '\u0DD6'
    | [\u0DD8-\u0DDF]
    | [\u0DF2-\u0DF3]
    | '\u0E31'
    | [\u0E34-\u0E3A]
    | [\u0E47-\u0E4E]
    | [\u0E50-\u0E59]
    | '\u0EB1'
    | [\u0EB4-\u0EB9]
    | [\u0EBB-\u0EBC]
    | [\u0EC8-\u0ECD]
    | [\u0ED0-\u0ED9]
    | [\u0F18-\u0F19]
    | [\u0F20-\u0F29]
    | '\u0F35'
    | '\u0F37'
    | '\u0F39'
    | [\u0F3E-\u0F3F]
    | [\u0F71-\u0F7E]
    | '\u0F7F'
    | [\u0F80-\u0F84]
    | [\u0F86-\u0F87]
    | [\u0F90-\u0F97]
    | [\u0F99-\u0FBC]
    | '\u0FC6'
    | '\u102C'
    | [\u102D-\u1030]
    | '\u1031'
    | '\u1032'
    | [\u1036-\u1037]
    | '\u1038'
    | '\u1039'
    | [\u1040-\u1049]
    | [\u1056-\u1057]
    | [\u1058-\u1059]
    | '\u135F'
    | [\u1369-\u1371]
    | [\u1712-\u1714]
    | [\u1732-\u1734]
    | [\u1752-\u1753]
    | [\u1772-\u1773]
    | '\u17B6'
    | [\u17B7-\u17BD]
    | [\u17BE-\u17C5]
    | '\u17C6'
    | [\u17C7-\u17C8]
    | [\u17C9-\u17D3]
    | '\u17DD'
    | [\u17E0-\u17E9]
    | [\u180B-\u180D]
    | [\u1810-\u1819]
    | '\u18A9'
    | [\u1920-\u1922]
    | [\u1923-\u1926]
    | [\u1927-\u1928]
    | [\u1929-\u192B]
    | [\u1930-\u1931]
    | '\u1932'
    | [\u1933-\u1938]
    | [\u1939-\u193B]
    | [\u1946-\u194F]
    | [\u19B0-\u19C0]
    | [\u19C8-\u19C9]
    | [\u19D0-\u19D9]
    | [\u1A17-\u1A18]
    | [\u1A19-\u1A1B]
    | [\u1DC0-\u1DC3]
    | [\u203F-\u2040]
    | '\u2054'
    | [\u20D0-\u20DC]
    | '\u20E1'
    | [\u20E5-\u20EB]
    | [\u302A-\u302F]
    | [\u3099-\u309A]
    | '\uA802'
    | '\uA806'
    | '\uA80B'
    | [\uA823-\uA824]
    | [\uA825-\uA826]
    | '\uA827'
    | '\uFB1E'
    | [\uFE00-\uFE0F]
    | [\uFE20-\uFE23]
    | [\uFE33-\uFE34]
    | [\uFE4D-\uFE4F]
    | [\uFF10-\uFF19]
    | '\uFF3F'
;

//
// Whitespace and comments
//

WS  :  [ \t\r\n\u000C]+ -> skip
;

COMMENT
:
   '/*' .*? '*/' -> channel(HIDDEN)
;

LINE_COMMENT
:
   '//' ~[\r\n]* -> channel(HIDDEN)
;
