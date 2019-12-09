import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det Nom | PropN | NP PP
    Nom -> Adj Nom | N
    VP -> V NP | V S | VP PP
    PP -> P NP
    PropN -> "Bill"
    Det -> "the" | "a" | an
    N -> "bear" | "squirrel" | "park" | "block" | "table"
    Adj -> "angry" | "frightened"
    V -> "chased" | "saw" | "put" | "eats" | "eat"
    P -> "on" | "Put"
  """)

S1 = nltk.word_tokenize("Put the block on the table")
S2 = nltk.word_tokenize("Bob chased a bear in the park along the river")
S3 = nltk.word_tokenize("Bill saw Bob chase the angry furry dog")

rd_parser = nltk.RecursiveDescentParser(grammar, trace=1)

for tree in rd_parser.parse(S1):
    print(tree)

