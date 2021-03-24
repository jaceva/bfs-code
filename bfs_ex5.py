from tree import sample_root_node, print_path
from collections import deque

# Create bfs function, set parameters
def bfs(root_node, goal_value):

  # and initialize path_queue
  path_queue = deque()

  # add root path to the queue
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # create a while loop that continues
  # as long as there are paths in the queue
  while len(path_queue) > 0:
    current_path = path_queue.pop()
    
    # get current node and test for goal
    current_node = current_path[-1]
    print(f"Searching node with value {current_node.value}")
    if current_node.value == goal_value:
      return current_path

  # return an empty path if goal not found
  return None
    
print(sample_root_node)
goal_path = bfs(sample_root_node, "F")
print_path(goal_path)
