
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

O = head_node(col_1[0])
A = middle_node(col_2[0])
B = middle_node(col_2[1])
C = end_node(col_2[3])

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
