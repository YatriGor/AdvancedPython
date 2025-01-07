import csv
import matplotlib.pyplot as plt

filePath = './file.csv'

categories = []
values = []

with open(filePath, mode='r', newline='') as file:
    file_reader = csv.reader(file)

    for i in range(10):
        row = next(file_reader)
        print(row)
        categories.append(row[5])
        values.append(float(row[4]))

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='brown')
plt.xlabel('Beverage')
plt.ylabel('money')
plt.title('Bar Graph for First Ten Entries for Coffee Shop Dataset')
plt.show()
        