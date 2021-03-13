import math
import csv
with open('Pro105Data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

total = 0
total_entries = len(data)
for b in data:
    total += int(b)

    mean = total/total_entries






sq= []
for number in data:
    x = int(number) - mean
    x = x**2
    sq.append(x)


sum =0
for i in sq:
    sum =sum + i


result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)