import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

# programmed by 1603930
# TASK 2

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

        if not simList:  # if simList is empty do nothing
            None
        else:  # else get the max and append it
            maxSim = max(simList)
            output.append([word1, word2, maxSim])
            print(word1, word2, maxSim)


simFile = open("original-pairs.txt", "w+")  # opens new file for similarities
simFile.write("word1 word2 Similarity\n")

for line in output:
    simFile.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + "\n")
simFile.close()