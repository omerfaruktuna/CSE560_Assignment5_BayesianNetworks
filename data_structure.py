class node():
  def __init__(self,name):
    self.name = name

class head_node(node):
  def __init__(self,name):
    super().__init__(name)
    self.first_connection = None
    self.second_connection = None
    self.T_prob = None
    self.F_prob = None

class middle_node(node):
  def __init__(self,name):
    super().__init__(name)
    self.connection = None
    self.T_prob = None
    self.F_prob = None

class end_node(node):
  def __init__(self,name):
    super().__init__(name)
    self.TT_prob = None
    self.TF_prob = None
    self.FT_prob = None
    self.FF_prob = None
