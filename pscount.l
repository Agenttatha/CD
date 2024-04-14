%{
int printf_count = 0;
int scanf_count = 0;
%}
%%
"printf" { printf_count++; }
"scanf" { scanf_count++; }
. ;
%%
int yywrap() {
return 1;
}
int main(int argc, char *argv[]) {
if (argc != 2) {
printf("Usage: %s <input_file>\n", argv[0]);
return 1;
}
FILE *fp = fopen(argv[1], "r");
if (fp == NULL) {
printf("Error opening file.\n");
return 1;
}
yyin = fp;
yylex();
printf("Number of printf statements: %d\n", printf_count);
printf("Number of scanf statements: %d\n", scanf_count);
fclose(fp);
return 0;
}
