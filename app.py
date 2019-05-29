
from data_structure import *

with open('bn.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  x = 0
  for line in content:
    if x == 0:
      number_of_lines = int(line.strip().split(",")[0])
      x+=1
      continue
    currentline = line.strip().split(",")
    dataset.append(currentline)

col_1 = []
col_2 = []

for data in dataset:
  col_1.append(data[0])
  col_2.append(data[1])

uniq_col_1 = set(col_1)
uniq_col_2 = set(col_2)

dictionary_col1 = {}

for val in uniq_col_1:
  c = col_1.count(val)
  dictionary_col1[val] = c

dictionary_col2 = {}

for val in uniq_col_2:
  c = col_2.count(val)
  dictionary_col2[val] = c


maximum_val = 0
for key, val in dictionary_col1.items():
  if val > maximum_val:
    maximum_val = val
    maximum_key= key 


O = head_node(maximum_key)

uniq_col_1.remove(maximum_key)


A = middle_node(uniq_col_1.pop())
B = middle_node(uniq_col_1.pop())

maximum_val = 0

for key, val in dictionary_col2.items():
  if val > maximum_val:
    maximum_val = val
    maximum_key= key 

C = end_node(maximum_key)

O.first_connection = A
O.second_connection = B
A.connection = C
B.connection = C


with open('O.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  for line in content:
    currentline = line.strip().split(",")
    dataset.append(currentline)

O.T_prob = float(dataset[0][1])
O.F_prob = 1-O.T_prob

with open('A.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  for line in content:
    currentline = line.strip().split(",")
    dataset.append(currentline)

A.T_prob = float(dataset[0][1])
A.F_prob = float(dataset[1][1])

with open('B.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  for line in content:
    currentline = line.strip().split(",")
    dataset.append(currentline)

B.T_prob = float(dataset[0][1])
B.F_prob = float(dataset[1][1])

with open('C.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  for line in content:
    currentline = line.strip().split(",")
    dataset.append(currentline)

C.TT_prob = float(dataset[0][2])
C.TF_prob = float(dataset[1][2])
C.FT_prob = float(dataset[2][2])
C.FF_prob = float(dataset[3][2])

print("Probability of (O and A' and B' and C) is: ")
print( O.T_prob * A.F_prob * B.F_prob * C.FF_prob)
