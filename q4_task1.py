from nltk.corpus import wordnet as wn

# programmed by 1603930
# TASK 1

SimLex = "./SimLex999-100.txt"

# open file
def openFile(filePath):
    outputList = list()
    with open(filePath, "r") as file:  # opens file
        data = file.readlines()  # reads lines
        for i in data:  # for each line
            if i != "word1\tword2\tSimLex999\n":
                outputList.append(i.split())  # split by space and append
    return outputList


# opened files
fileSimLex = openFile(SimLex)

# output list
output = []

# get words
for i in fileSimLex:
    # get individual words
    word1 = i[0]
    word2 = i[1]
    goldenStandardValue = i[2]

    word1_synsets = wn.synsets(word1)  # get sets
    word2_synsets = wn.synsets(word2)

    simList = []  # similarity text for given words

    for y in word1_synsets:  # for sense in word 1
        for z in word2_synsets:  # for sense in word 2
            sim = y.path_similarity(z)  # work out similarity between the two
            if sim is not None:  # if there is a similarity
                simList.append(sim)  # append it (otherwise appends empty list)
            else:  # if it is empty, just append 0
                simList.append(0.0)

    if not simList:  # if simList is empty do nothing
        None # this code is doing nothing because appends 0 if it is empty, however can be useful for further tasks...
    else:  # else get the max and append it
        maxSim = max(simList)
        output.append([word1, word2, goldenStandardValue, maxSim])

# this prints it out in the format (for testing purposes)
print("word1 word2 GoldSimilartiy WordNetSimilarity")
for x in output:
    print(x[0], x[1], x[2], x[3])

# this writes it to file
newFile = open("BioSim-100-predicted.txt", "w+")  # creates file if doesnt exist
newFile.write("word1 word2 GoldSimilartiy WordNetSimilarity\n")
for line in output:
    newFile.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + "\n")
newFile.close()