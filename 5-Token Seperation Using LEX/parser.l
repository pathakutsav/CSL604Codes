%{
#include<stdio.h>
int uc=0,lc=0,digit=0;
%}
%%
[A-Z] uc++;
[a-z] lc++;
[0-9] digit++;
%%
int main(void)
{
yylex();
printf("\n\t%d Uppercase Letters",uc);
printf("\n\t%d Lowercase Letters",lc);
printf("\n\t%d Digits",digit);
}
int yywrap()
{
return(1);
}
