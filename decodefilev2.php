<?php

$filename = 'tsf.txt';
$lines = [];

$f = fopen($filename, 'r');

if (!$f) {
    return;
}

while (!feof($f)) {
    $line = fgets($f);
    ls =line.split(None,-1)
    NumberOfWords = len(ls)

    padnum = "0000000000"+ls[0]
    n = len(ls[0])
    padnum = padnum[n:]
    ArrayOfLines.append(padnum+" "+ls[NumberOfWords-1])  #substr("0000000000" $1, length($1))

    $lines[] = $line;
}
fclose($f);

print_r($lines);


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



