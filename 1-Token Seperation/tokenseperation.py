import re 
tokens = [] 
input_code = 'if ( a > b ) { i = j + 2 ; else j = k - 2 ; }'.split()
for word in input_code:
   if word in ["str", "int", "bool", "float", "double", "char", "long"]:
     tokens.append(['DATATYPE', word])
   if word in["auto","break","case","catch","word","class","const","continue","delete","do","if","else","enum","false","for","goto","if","#include","namespace","not","or","private","protected","public","return","short","signed","sizeof","static","struct","switch","true","try","unsigned","void","while",]:
     tokens.append(['KEYWORD', word])
   elif re.match("[a-z]", word) or re.match("[A-Z]", word):
     tokens.append(['IDENTIFIER', word])
   elif word in ['_','`','~','!','@','#','$','^','&','"',':',';','<','>','?']:
     tokens.append(['NON-IDENTIFIER', word])
   elif word in ["+","-","*","/","%","+=","-=","*=","/=","++","--","|","&&",]:
     tokens.append(['OPERATOR', word])
   elif word in ["\t","\n","(",")","[","]","{","}","=",":",",",";","<<",">>",]:
     tokens.append(['DELIMITER', word])
   elif word in ['0','1','2','3','4','5','6','7','8','9']:
     tokens.append(["NUMERAL", word])
   elif re.match(".[0-9]", word):
     if word[len(word) - 1] == ';':
       tokens.append(["INTEGER", word[:-1]])
       tokens.append(['END_STATEMENT', ';'])
   else:
     tokens.append(["INTEGER", word])
for tkn in tokens:
  print(tkn)    
