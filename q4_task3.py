import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

# programmed by 1603930
# TASK 3

#text = "./test2.txt"
text = "./text1.txt"

# open file for utf-8-sig
def openFile(filePath):
    with open(filePath, encoding="utf-8-sig") as file:  # opens file
        return file.read() # returns string

data = openFile(text)
data = data.lower()  # lowercasing
dataTokenized = nltk.word_tokenize(data)  # tokenizes
dataTokenized = [word for word in dataTokenized if word.isalpha()]  # removes punc
dataTokenized = [word for word in dataTokenized if word not in stopwords.words('english')]  # filters using stop words
dataToke_Lemm = [nltk.WordNetLemmatizer().lemmatize(word) for word in dataTokenized]  # lemmatizes words
dataToke_Lemm = set(dataToke_Lemm)  # removes dupes

# working out similarity

output = []  # output

for word1 in dataToke_Lemm:
    word1_synsets = wn.synsets(word1)
    for word2 in dataToke_Lemm:
        word2_synsets = wn.synsets(word2) # gets both words

        simList = []  # similarity text for given words

        for y in word1_synsets:  # for sense in word 1
            for z in word2_synsets:  # for sense in word 2
                sim = y.path_similarity(z)  # work out similarity between the two
                if sim is not None:  # if there is a similarity
                    simList.append(sim)  # append it (otherwise appends empty list)
                else:  # if it is empty, just append 0
                    simList.append(0.0)

        try: # tries to get a hypernym for index - if it exists
            hy_word1 = word1_synsets[0].hypernyms()
            hy_word1_output = wn.synset(hy_word1[0].name()).lemma_names()[0]
        except IndexError:
            hy_word1 = "None"
        try:
            hy_word2 = word2_synsets[0].hypernyms()
            hy_word2_output = wn.synset(hy_word2[0].name()).lemma_names()[0]
        except IndexError:
            hy_word2 = "None"
        try:
            if hy_word1 == "None" or hy_word2 == "None":
                hySim = 0.0
            else:
                hySim = hy_word1[0].path_similarity(hy_word2[0])
                if hySim == None:
                    hySim = 0.0
        except IndexError or AttributeError:
            hySim = 0.0

        if not simList:  # if simList is empty do nothing
            None
        else:  # else get the max and append it
            maxSim = max(simList)
            output.append([word1, word2, maxSim, hy_word1_output, hy_word2_output, hySim])
            print(word1, word2, maxSim, hy_word1_output, hy_word2_output, hySim)


simFile = open("original-pairs-hypernyms.txt", "w+")  # opens new file for similarities
simFile.write("word1 word2 Similarity1 hyp1 hyp2 Similarity2\n")

for line in output:
    simFile.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + " " + str(line[4]) + " " + str(line[5]) + "\n")
simFile.close()