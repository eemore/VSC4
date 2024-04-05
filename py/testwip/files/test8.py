import csv

with open(r"C:\Users\emoree\Downloads\PD\VSC4\py\testwip\files\weather.csv","r") as file:
    data=list(csv.reader(file))

city = input('Enter a city')
for row in data[1:]:
    if row[0]==city:
        print(row[1])
print(data[1][1])