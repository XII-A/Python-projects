# The time complexity of the dfs_Cycle function is O(V+E), 
# where V is the number of nodes in the graph and E is the number of edges in the graph. 
# This is because the function iterates through the rows of the adjacency matrix, which is O(V), and for each row, 
# it iterates through the elements of the row, which is O(E).
# The time complexity of the dfs_output function is also O(V+E), for the same reason as above.

# Which makes the totoal time complexity as O(V+E) which is better than the running time of Kruskal and Prim

adj_matrix = [] # to store the adjacency matrix
visted = [] # to keep track of visited node
current_max = -9999 # to keep track of the heaviest node value
max_node = -1; # to keep trakc of the heaviest node
final_node = -1; #to mark where our loop is
result = [] # to stroe the result



#detectting the cycle and getting the heaviest edge in the cycle
def dfs_Cycle(vertex,parent):
    visted[vertex] = True
    node = 0
    global max_node
    global final_node
    global current_max
    # going through each neighbor of the vertex 
    for i in adj_matrix[vertex]:
        if i != 0:
            if visted[node] == False:
                if(dfs_Cycle(node,vertex)): #if true is returned true
                                            #this means we are going back from the final node to the starting node of the cycle to find the heaviest edge
                    if vertex != final_node:
                        if i > current_max:
                            current_max = i
                            max_node = vertex
                        return True
                    if vertex == final_node: # if we reached the final node we stop looking for the heaviest edge and let the dfs function complete as normal
                        if i > current_max:
                            current_max = i
                            max_node = vertex
                        return False
                    
            elif visted[node] == True and node != parent: #if we reach a node that has been visited before and its not our parent then we found the cycle 
              
                current_max = i
                max_node = vertex
                final_node = node
                adj_matrix[vertex][node] = 0;#marking it as the final node
                adj_matrix[node][vertex] = 0;
                return True
        node = node + 1
    return False
    
# here we do a dfs traversal of the nodes but we select the lightest node first
def dfs_output(v,parent):
    visted[v] = True
    node = 0
    order_of_R = [] # to store the order of nodes we are going in
    # going through each neighbor of vertex v 
    for i in adj_matrix[v]:
        if i != 0:
            if visted[node] == False:
              
                order_of_R.append(node)
               
            elif visted[node] == True and node != parent:
                pass
                
        node = node + 1
    # selection sort O(n^2) where n is the number of neighbors of v
    for j in range(len(order_of_R)):
        min_index = j
        for k in range(j+1 , len(order_of_R)):
            node_min = order_of_R[min_index]
            node = order_of_R[k]
            if adj_matrix[v][node_min] > adj_matrix[v][node]:
                min_index = k
        temp = order_of_R[j] 
        order_of_R[j] = order_of_R[min_index]
        order_of_R[min_index] = temp

    # adding the node we are going to traverse to our output and then continuing our dfs traversal
    for z in range(len(order_of_R)):
        result.append(order_of_R[z])
        dfs_output(order_of_R[z],v)
    
    return False

    





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
    
    
    dfs_Cycle(0,-1) # starting our search 
    

    # initializing the visited matrix again before getting the output O(V)
    i = 0
    while i < matrix_size:
        visted[i] = False
        i = i + 1
    result.append(0)
    dfs_output(0,-1)
    #printing the result
    index = 0
    for item in result:
        if(index < len(result) - 1):
            print(item,end=" ")
        else:
            print(item)
        index = index + 1



main()
		
    