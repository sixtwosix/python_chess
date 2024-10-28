# graph = {  
#   '0' : ['1','2','3','4'],
#   '1' : ['5'],
#   '2' : ['6'],
#   '3' : ['7'],
#   '4' : ['8'],
#   '5' : ['9'],
#   '6' : ['10'],
#   '7' : ['11'],
#   '8' : ['12'],
#   '9' : ['13'],
#   '10' : [],
#   '11' : [],
#   '12' : ['14'],
#   '13' : [],
#   '14' : [],
  
# }

# graph = {
#   (4,0) : [],
#   (4,1) : [(4,0)],
#   (4,2) : [(4,1)],
#   (4,3) : [(4,2)],
#   (4,4) : [(3,4),(5,4),(4,3),(4,5)],
#   (4,5) : [(4,6)],
#   (4,6) : [(4,7)],
#   (4,7) : [],
#   (0,4) : [],
#   (1,4) : [(0,4)],
#   (2,4) : [(1,4)],
#   (3,4) : [(2,4)],
#   (5,4) : [(6,4)],
#   (6,4) : [(7,4)],
#   (7,4) : []
# }

graph = {(4, 0): [], (4, 1): [(4, 0)], (4, 2): [(4, 1)], (4, 3): [(4, 2)], (4, 4): [(4, 5), (4, 3), (5, 4), (3, 4)], (4, 5): [(4, 6)], (4, 6): [(4, 7)], (4, 7): [], (0, 4): [], (1, 4): [(0, 4)], (2, 4): [(1, 4)], (3, 4): [(2, 4)], (5, 4): [(6, 4)], (6, 4): [(7, 4)], (7, 4): []}



def bfs(graph, node): #function for BFS
  visited = [] # List for visited nodes.
  queue = []     #Initialize a queue
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    # print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        # TODO : Add logic to check if piece can be taken or is open or is allied piece
        # if neighbour is movable
        # if(neighbour in ['9','3','2']):
        #   visited.append(neighbour)
        # else:       
        visited.append(neighbour)
        queue.append(neighbour)
  
  print(visited)

# Driver Code
print("Following is the Breadth-First Search")
bfs(graph,(4,4))    # function calling