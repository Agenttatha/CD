%{
    // Program to identify octal and hexadecimal numbers
    #include <stdio.h>
%}

Oct 0[0-7]+
Hex 0[xX][0-9A-Fa-f]+

%%
{Hex} printf("This is a hexadecimal number\n");
{Oct} printf("This is an octal number\n");
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

