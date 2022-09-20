import pandas as pd
from random import randint

# mengimport file dengan library pandas
df = pd.read_excel('Data Populasi.xlsx')
print(df)

# mengekstrak data dari excel
data = [ ]
for x in df.index:
    data.append(df.loc[x, '2022 Population'])
# menguji perulangan
print(data)

# membuat fungsi tukar dan menukar data pada list
def swap(list, a, b):
    list[a], list[b] = list[b], list[a]

for i in range(len(data)):
    x = randint(0, 9)
    y = randint(0, 9)
    swap(data, x, y)

print(data)

# membuat class dengan berbagai fungsi sorting
class sort:

    # membuat fungsi buuble sort
    def bubble(list):
        n = len(list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if list[j] > list[j + 1]:
                    swapped = True
                    list[j], list[j + 1] = list[j + 1], list[j]
            if not swapped:
                return
    # membuat fungsi insertion sort
    def insertion(list):
        for i in range(1, len(list)):
            key = list[i]
            j = i-1
            while j >=0 and key < list[j] :
                list[j], list[j + 1] = list[j + 1], list[j]
                j -= 1
            list[j+1] = key
    # membuat fungsi selection sort
    def selection(list):
        for i in range(len(list)):
            min_idx = i
            for j in range(i+1, len(list)):
                if list[min_idx] > list[j]:
                    min_idx = j
            list[i], list[min_idx] = list[min_idx], list[i]


sort.selection(data)
print(data)



