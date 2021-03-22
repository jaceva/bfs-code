from tree import sample_root_node, print_path
from collections import deque

# Create bfs function, set parameters
def bfs(root_node, goal_value):

  # and initialize path_queue
  path_queue = deque()

  # add root path to the queue
  path_queue.appendleft([root_node])
  
  # create a while loop that continues
  # as long as there are paths in the queue
  while len(path_queue) > 0:
    current_path = path_queue.pop()
    
    # get current node and test for goal
    current_node = current_path[-1]
    if current_node.value == goal_value:
      return current_path

    # iterate through the current nodes children
    # copy the current path and add a child to it
    # then push the path to the frontier
    for child in current_node.children:
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None
    
print(sample_root_node)
path = bfs(sample_root_node, "F")
print_path(path)
