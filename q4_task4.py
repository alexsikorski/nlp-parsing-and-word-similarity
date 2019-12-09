# programmed by 1603930
# TASK 4

# this program must have an original-text.txt generated (or placed) in the directory
# this design choice was made to save time by not having to output the same file again from q4_task2.py
# filepath for original-text.txt

text = "./original-pairs.txt"

# open file for utf-8-sig
def openFile(filePath):
    with open(filePath, encoding="utf-8-sig") as file:  # opens file
        return file.read() # returns string

data = openFile(text)
data = data.splitlines()  # splits text by lines
processedData = []
for line in data:
    newLine = line.split()  # splits line by space
    processedData.append(newLine)

processedData.pop(0)  # removes first line which is "word1 word2 Similarity"

print("word1 word2 Similarity")
counter = 0

output = []
# for printing
for line in processedData:
    if counter == 10:
        break
    if float(line[2]) == 1.0 and line[0] != line[1]:
        counter = counter + 1
        output.append(line[0] + " " + line[1] + " " + line[2])
        print(line[0] + " " + line[1] + " " + line[2])

# write file
simFile = open("top.txt", "w+")  # opens new file for similarities
simFile.write("word1 word2 Similarity1\n")

for line in output:
    simFile.write(line + "\n")
simFile.close()

