def get_average():
    with open('files/data.txt') as file:
        data=file.readlines()
    
    values = data[1:]
    values = [float(i) for i in values]

    avg2 = sum(values)/len(values)
    return avg2

avg = get_average()
print(avg)