class node():
  def __init__(self):
    self.name = None
    self.parents = []
    self.T_prob = None
    self.F_prob = None
  
  def get_parents(self):
    return self.parents

  def prob(self,A,lst1,lst2):

    if len(self.parents) == 0:
      txt = self.name + ".txt"
      with open(txt, 'r') as f:
        tmp = []
        content = f.readlines()
        for line in content:
          currentline = line.strip().split(",")
          tmp.append(currentline)

        self.T_prob = float(tmp[0][1])
        self.F_prob = 1 - float(tmp[0][1])
      if A == "T":
        return self.T_prob
      elif A == "F":
        return self.F_prob

    if len(self.parents) > 0:
      txt = self.name + ".txt"
      with open(txt, 'r') as f:
        tmp = []
        content = f.readlines()
        for line in content:
          currentline = line.strip().split(",")
          tmp.append(currentline)
          parent_list = tmp[0]
      
      tmp_content = []
      tmp_content = tmp[1:]

      ind = []
      for i in lst1:
        if i in tmp[0]:
          ind.append(tmp[0].index(i))

      ind_stat = []

      for i in lst2:
        ind_stat.append(i)
    
      for i in range(len(tmp_content)):
        if ind_stat == tmp_content[i][:-1]:

          self.T_prob = float(tmp_content[i][-1])
          self.F_prob = 1 - float(tmp_content[i][-1])
          break

      if A == "T":
        return self.T_prob
      elif A == "F":
        return self.F_prob


def multiply(lst) : 
    res = 1
    for l in lst: 
         res = res * l  
    return res 

node_names = []
node_data_structures = []


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
    if currentline[0] not in node_names:
      node_names.append(currentline[0])
      y = currentline[0]
      exec(currentline[0] + " = node()")
      exec(currentline[0] + ".name" + " = y")

      node_data_structures.append(eval(currentline[0]))

    if currentline[1] not in node_names:
      node_names.append(currentline[1])
      y = currentline[1]
      exec(currentline[1] + " = node()")
      exec(currentline[1] + ".name" + " = y")
      node_data_structures.append(eval(currentline[1]))
    
    for i in node_data_structures:
      if i.name == currentline[1]:
        i.parents.append(eval(currentline[0]))
    dataset.append(currentline)



with open('Question.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  for line in content:
    currentline = line.strip().split(",")
    dataset.append(currentline)
  
  question_nodes = dataset[0]

result_multiplication_list = []

print("\nQuestion is: \nWhat is the probality of {} = ?".format(question_nodes))
for x in question_nodes:

  if len(eval(x[0]).get_parents()) == 0:
    result_multiplication_list.append(eval(x[0]).prob(x[1],[],[]))

  
  else:
    parent_list = eval(x[0]).get_parents()
    parent_list_names = []
    for a in parent_list:
      parent_list_names.append(a.name)

    parent_list_names_stat = []
    for a in question_nodes:
      if a[0] in parent_list_names:
        parent_list_names_stat.append(a[1])
    
    result_multiplication_list.append(eval(x[0]).prob(x[1],parent_list_names,parent_list_names_stat))

print("\nProbabilities to be used in calculation:")
print(result_multiplication_list)

print("\nAnswer is:\n{}".format(multiply(result_multiplication_list)))

print("\n")
