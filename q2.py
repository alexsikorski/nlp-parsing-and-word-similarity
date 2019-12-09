import nltk

# Programmed by 1603930
grammar = nltk.CFG.fromstring("""
    S -> NP VP | VP PP | NP V
    NP -> Det Nom | PropN | NP PP | N
    Nom -> Adj Nom | N
    VP -> V NP | V S | VP PP 
    PP -> P NP
    PropN -> "Bill" | "Bob"
    Det -> "the" | "a" | "an" | "An" | "The"
    N -> "bear" | "squirrel" | "park" | "river" | "dog" | "block" | "table" | "dogs" | "squirrels" | "tables"
    Adj -> "angry" | "frightened" | "furry"
    V -> "chased" | "saw" | "put" | "eats" | "eat" | "chase" | "Put"
    P -> "on" | "in" | "along"
  """)

S4 = nltk.word_tokenize("An bear eat an squirrel")
S5 = nltk.word_tokenize("The dogs eats")

S_incorrect1 = nltk.word_tokenize("The squirrel eat table")
S_incorrect2 = nltk.word_tokenize("Bob saw Bill eats a bear")
S_correct1 = nltk.word_tokenize("The squirrels eat tables")
S_correct2 = nltk.word_tokenize("Bob saw Bill eat a bear")

parser = nltk.ChartParser(grammar)

print("!!!!!!!! S4: !!!!!!!! ")
trees_S4 = parser.parse(S4)
for tree in trees_S4:
    print(tree)

print("!!!!!!!! S5: !!!!!!!! ")
trees_S5 = parser.parse(S5)
for tree in trees_S5:
    print(tree)

print("!!!!!!!! S_incorrect1: !!!!!!!! ")
trees_S_incorrect1 = parser.parse(S_incorrect1)
for tree in trees_S_incorrect1:
    print(tree)

print("!!!!!!!! S_correct1: !!!!!!!! ")
trees_S_correct1 = parser.parse(S_correct1)
for tree in trees_S_correct1:
    print(tree)

print("!!!!!!!! S_incorrect2: !!!!!!!! ")
trees_S_incorrect2 = parser.parse(S_incorrect2)
for tree in trees_S_incorrect2:
    print(tree)

print("!!!!!!!! S_correct2: !!!!!!!! ")
trees_S_correct2 = parser.parse(S_correct2)
for tree in trees_S_correct2:
    print(tree)


