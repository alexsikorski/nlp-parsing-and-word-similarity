import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP | VP PP
    NP -> Det Nom | PropN | NP PP | PRP | N
    Nom -> Adj Nom | N | NNS
    VP -> V NP | V S | VP PP | VBZ NP PP
    PP -> P NP
    PropN -> "Bill" | "Bob"
    Det -> "the" | "a" | "an" | "some"
    N -> "bear" | "squirrel" | "park" | "river" | "dog" | "block" | "table" | "restaurant" | "pasta" | "fork"
    Adj -> "angry" | "frightened" | "furry"
    V -> "chased" | "saw" | "put" | "eats" | "eat" | "chase" | "Put"
    P -> "on" | "in" | "along" | "with" 
    PRP -> "He"
    VBZ -> "eats"
    NNS -> "anchovies"
  """)

S6 = nltk.word_tokenize("He eats pasta with some anchovies in the restaurant")
S7 = nltk.word_tokenize("He eats pasta with a fork in the restaurant")

parser = nltk.ShiftReduceParser(grammar, trace=2)

print("!!!!!!!! S6: !!!!!!!! ")
trees_S6 = parser.parse(S6)
for tree in trees_S6:
    print(tree)

print("!!!!!!!! S7: !!!!!!!! ")
trees_S7 = parser.parse(S7)
for tree in trees_S7:
    print(tree)