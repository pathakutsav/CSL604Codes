%{
#include<stdio.h>
%}
%%
[0-9]+[.][0-9]+ printf("%s is a floating point number\n",yytext);
int|float|char|double|void printf("%s is a datatype\n",yytext);
[0-9]+ printf("%s is an integer number\n",yytext);
[a-z]+[()] printf("%s is a function\n",yytext);
[a-z]+ printf("%s is an identifier\n",yytext);
[+=*/-] printf("%s is an operator\n",yytext);
; printf("%s is an delimiter\n",yytext);
, printf("%s is a separator\n",yytext);
[#][a-z\.h]+ printf("%s is a preprocessor\n",yytext);
%%
COMPILER DESIGN LAB RECORD 18030141CSE033
Page | 18
int yywrap(void)
{
 return 1;
}
int main(void)
{
yylex();
return 0;
}