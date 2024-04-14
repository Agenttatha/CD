%{
#include<stdio.h>
int count=0;
%}
op [+\-*/]
letter [a-zA-Z]
digitt [0-9]
id ({letter}+|({letter}{digitt}+))
notid ({digitt}+{letter}+)
%%
[\t\n]+
(int|float|char|case|default|if|for|printf|scanf) { printf("%s is a keyword\n", yytext); }
{id} { printf("%s is an identifier\n", yytext); count++; }
{notid} { printf("%s is not an identifier\n", yytext); }
%%

int main()
{
    FILE *fp;
    char file[10];
    printf("\nEnter the filename: ");
    scanf("%s", file);
    fp=fopen(file,"r");
    if(fp==NULL){
        printf("File not found\n");
        return 1;
    }
    yyin=fp;
    yylex();
    printf("Total identifiers are: %d\n", count);
    fclose(fp);
    return 0;
}

int yywrap() {
    return 1; // Indicate that there are no more input files
}

