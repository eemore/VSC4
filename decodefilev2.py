myfile = "tsf.txt"


with open(myfile, "r") as file1:
    LinesFromFile=file1.readlines()

ArrayOfLines=[]
for line in LinesFromFile: 
    line = line.replace("\n", "")
    ls =line.split(None,-1)
    NumberOfWords = len(ls)

    padnum = "0000000000"+ls[0]
    n = len(ls[0])
    padnum = padnum[n:]
    ArrayOfLines.append(padnum+" "+ls[NumberOfWords-1])  #substr("0000000000" $1, length($1))
    #print(line)
    #print(len(ls))

#print(content)

SortedArrayOfLines = sorted(ArrayOfLines)

#print(SortedArrayOfLines)

nrows=len(SortedArrayOfLines)
row=0
nrow=0
totrows=0
Decodestring=""

while totrows+row<nrows:
    row=row+1
    totrows=totrows+row
    LastWord = SortedArrayOfLines[totrows - 1].split()
    Decodestring = Decodestring + " " + LastWord[1] #big assumption that we have split into 2


print(Decodestring)



