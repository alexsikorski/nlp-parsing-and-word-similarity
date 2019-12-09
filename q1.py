import nltk

# Programmed by 1603930
grammar = nltk.CFG.fromstring("""
    S -> NP VP | VP PP
    NP -> Det Nom | PropN | NP PP
    Nom -> Adj Nom | N
    VP -> V NP | V S | VP PP
    PP -> P NP
    PropN -> "Bill" | "Bob"
    Det -> "the" | "a" | "an"
    N -> "bear" | "squirrel" | "park" | "river" | "dog" | "block" | "table"
    Adj -> "angry" | "frightened" | "furry"
    V -> "chased" | "saw" | "put" | "eats" | "eat" | "chase" | "Put"
    P -> "on" | "in" | "along"
  """)

S1 = nltk.word_tokenize("Put the block on the table")
S2 = nltk.word_tokenize("Bob chased a bear in the park along the river")
S3 = nltk.word_tokenize("Bill saw Bob chase the angry furry dog")

# S1_tagged = nltk.pos_tag(S1)
# S2_tagged = nltk.pos_tag(S2)
# S3_tagged = nltk.pos_tag(S3)
# print(S1_tagged)
# print(S2_tagged)
# print(S3_tagged)

parser = nltk.ChartParser(grammar)

print("!!!!!!!! S1: !!!!!!!! ")
trees_S1 = parser.parse(S1)
for tree in trees_S1:
    print(tree)

print("!!!!!!!! S2: !!!!!!!!")
trees_S2 = parser.parse(S2)
for tree in trees_S2:
    print(tree)

print("!!!!!!!! S3: !!!!!!!!")
trees_S3 = parser.parse(S3)
for tree in trees_S3:
    print(tree)
