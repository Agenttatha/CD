%{
#include <stdio.h>
int char_count = 0;
int space_count = 0;
int line_count = 0;
int tab_count = 0;
%}
%option noyywrap
%%
. {
char_count++;
if(yytext[0] == ' ') space_count++;
if(yytext[0] == '\t') tab_count++;
}
\n {
line_count++;
char_count++; // Count newline character
}
%%
int main(int argc, char *argv[]) {
if (argc != 2) {
fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
return 1;
}
FILE *file = fopen(argv[1], "r");
if (file == NULL) {
fprintf(stderr, "Error: Could not open file %s\n", argv[1]);
return 1;
}
yyin = file;
yylex();
printf("Characters: %d\n", char_count);
printf("Spaces: %d\n", space_count);
printf("Lines: %d\n", line_count);
printf("Tabs: %d\n", tab_count);
fclose(file);
return 0;
}
