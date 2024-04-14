%{
#include <stdio.h>
%}
%option noyywrap
/* Regular expressions for tokens */
DIGIT [0-9]
LETTER [a-zA-Z]
ID {LETTER}({LETTER}|{DIGIT})*
INT_CONST {DIGIT}+
FLOAT_CONST {DIGIT}+"."{DIGIT}+
WS [ \t\n\r]+
COMMENT ("//"(.)*)
%%
"int" { printf("Keyword: int\n"); }
"float" { printf("Keyword: float\n"); }
"char" { printf("Keyword: char\n"); }
"if" { printf("Keyword: if\n"); }
"else" { printf("Keyword: else\n"); }
"for" { printf("Keyword: for\n"); }
"while" { printf("Keyword: while\n"); }
"return" { printf("Keyword: return\n"); }
{ID} { printf("Identifier: %s\n", yytext); }
{INT_CONST} { printf("Integer Constant: %s\n", yytext); }
{FLOAT_CONST} { printf("Float Constant: %s\n", yytext); }
"+" { printf("Operator: +\n"); }
"-" { printf("Operator: -\n"); }
"*" { printf("Operator: *\n"); }
"/" { printf("Operator: /\n"); }
"=" { printf("Operator: =\n"); }
"(" { printf("Operator: (\n"); }
")" { printf("Operator: )\n"); }
"<" { printf("Operator: <\n"); }
">" { printf("Operator: >\n"); }
{WS} ; /* Ignore whitespace */
{COMMENT} ; /* Ignore comments */
"#"([^\n])*\n { printf("Preprocessor Directive: %s\n", yytext); } /* Recognize preprocessor
directives */
. { printf("Unrecognized token: %s\n", yytext); }
%%
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s input_file\n", argv[0]);
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }
    yyin = file;
    yylex();
    fclose(file);
    return 0;
}

