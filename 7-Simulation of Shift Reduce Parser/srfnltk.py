import nltk
nltk.download('punkt')
from nltk.parse import ShiftReduceParser

grammar = nltk.CFG.fromstring("""

S -> NP VP
NP -> PropN | N PP | Det N
VP -> V NP | V S | VP PP | NP PP
PP -> P NP 
PropN -> 'He'| 'Utsav'
Det -> 'some' | 'the'
N -> 'compilerdesign' | 'programming'
V -> 'eats' | 'studies'
P -> 'and' | 'in' | 'is'

""")

sr = ShiftReduceParser(grammar)
sentence1 = 'Utsav studies compilerdesign and some programming'
tokens = nltk.word_tokenize(sentence1)
for x in sr.parse(tokens):
    print(x)
