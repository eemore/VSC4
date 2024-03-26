def get_average():
    with open('files/data.txt') as file:
        data=file.readlines()
    
    values = data[1:]
    values = [float(i) for i in values]

    avg2 = sum(values)/len(values)
    return avg2
def parse(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return feet,inches

avg = get_average()
print(avg)

a=parse('1 2')
print(a)