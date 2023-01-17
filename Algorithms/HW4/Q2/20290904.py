adj_matrix = [] # to store the adjacency matrix
visted = [] # to keep track of visited node
queue = [] # so we are able to do a bfs search with priority to the node with lowest cost
sol = [] # to store our solution

# The time complexity of this code is O(V + E) where V is the number of vertices (nodes) in the graph and E is the number of edges.
# This is because the BFS algorithm visits each vertex and edge once. 
# which is better than the running time of Kruskal and Prim
# The adjacency matrix is iterated through once to create the adjacency list, which takes O(V^2) time, 
# but this is a lower order term and can be ignored when analyzing the overall time complexity of the algorithm.

def BFS(v):
    queue.append(v) # adding the nodes to the queue so we can do bfs search
    
    while queue:
        node = queue.pop(0)
        
        if visted[node] != True: #to avoid loops we check if node has been visited before
            visted[node] = True
            sol.append(node) # we add the node we visited to our solution 
            # then check the rest of the nodes
            for i in range(len(adj_matrix[node])): 
                if adj_matrix[node][i] != 0:
                    queue.append(i)
                    queue.sort()
      # printing our solution  
    index = 0            
    for item in sol:
        if index < (len(sol) - 1):
            print(item,end=' ')
        else:
            print(item,end='\n')
        index = index + 1

    

        
    







def main():
    matrix_size = 0
    # taking input O(V^2)
    while True:
        try:#we take the input row by row then add the rows to the adjacency matrix
            for value in input('').split('\n') :
                row_input = []
                for num in value.split(' '):
                    if(num != ''):
                        row_input.append(int(num))
                adj_matrix.append(row_input)
                matrix_size = matrix_size + 1
        except (EOFError):
            break
    # initializing the visited matrix O(V)
    i = 0
    while i < matrix_size:
        visted.append(False)
        i = i + 1
    BFS(0)

main()
    