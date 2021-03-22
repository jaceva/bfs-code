from collections import deque

class TreeNode:
  def __init__(self, value):
   self.value = value
   self.children = []

  def __repr__(self):
    stack = deque()
    stack.append([self, 0])
    level_str = "\n"
    while len(stack) > 0:
      node, level = stack.pop()
      
      if level > 0:
        level_str += "| "*(level-1)+ "|-"
      level_str += str(node.value)
      level_str += "\n"
      level+=1
      for child in node.children:
        stack.append([child, level])

    return level_str


def print_path(path):
  # If path is None, no path was found
  if path == None:
    print("No paths found!")

  # If a path was found, print path
  else:  
    print("Path found:")
    for node in path:
      print(node.value)


sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]

