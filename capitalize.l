%{
#include<stdio.h>
#include<ctype.h>
%}

%%
[a-z]+ {
    int i;
    for(i=0; yytext[i]!='\0'; i++){
        yytext[i] = toupper(yytext[i]);
    }
    printf("%s", yytext);
    yyterminate();
}
.|\n { printf("%s", yytext); }
%%

int yywrap() {
    return 1; // Indicate to Flex that there are no more input files
}

int main() {
    yylex();
    return 0;
}

