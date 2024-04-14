#include <stdio.h>
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
int char_count = 0;
int space_count = 0;
int line_count = 0;
int tab_count = 0;
int ch;
while ((ch = fgetc(file)) != EOF) {
char_count++;
if (ch == ' ') space_count++;
if (ch == '\n') line_count++;
if (ch == '\t') tab_count++;
}
fclose(file);
printf("Characters: %d\n", char_count);
printf("Spaces: %d\n", space_count);
printf("Lines: %d\n", line_count);
printf("Tabs: %d\n", tab_count);
return 0;
}
