BEGIN {nrows=0}

{
    #Save row into array

	nrows++
    #Padd $1 to make it sort properly as a number.
	#save first(padded) and last words 
	#arows[nrows]= substr("0000000000" $1, length($1))  " " substr($0, index($0,$2))
	arows[nrows]= substr("0000000000" $1, length($1))  " " $(NF)
} 

END {
    
    #After reading all row, Sort and Decode

    asort(arows)
    #for(row=1;row<=nrows;row++){print arows[row]}

	totrows=0
	row=0
	Decodestring=""
	while (totrows+row<=nrows) {
		row++
		totrows+=row #will go from  1	3	6	10	15	21	28	36	45 Fibonacci sequence 
        LastWord = substr(arows[totrows], match(arows[totrows],/\w+$/ ) )
		Decodestring = Decodestring " " LastWord
	} 	
	print Decodestring
}
