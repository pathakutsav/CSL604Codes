%{
#include<stdio.h>
int vc=0;
int cc=0;
%}
%%
[aeiouAEIOU] vc++;
[a-zA-Z] cc++;
%%
int yywrap(void)
{
}
int main()
{
printf("Enter the string of vowels and consonants:");
yylex();
printf("Number of vowels are:  %d\n", vc);
printf("Number of consonants are:  %d\n", cc);
return 0;
}
