# The time complexity of the code is O(V^2) where V is the number of vertices (nodes) in the graph 



matrix = [] #where we store the entire input
adj_matrix = [] #where we store the adjacency matrix
let_num = {} #to help us translate names to numbers
num_let = {} #to help us translate numbers to names
visted = [] #to keep track of visited nodes
path = [] #to keep track of the current path
set_path = [] #to keep track of all paths so far
distance = 0 # to keep track of the current length of the path
lengths = [] # to keep track of all paths lengths

#I took a brute force approach and used dfs to go through every possible path 
# from starting node to goal node 
# the DFS function is called from each vertext to every other vertex which takes O(V^2 )
def brute_force(vertex,parent,goal):
    global distance
    global path
    visted[vertex] = True # so we dont go in loops
    path.append(vertex) # appending the vertex to the path
    if parent != -1: # calculating the distance of each path and making sure this is not the starting point
        distance = distance + adj_matrix[parent][vertex]
        
    if vertex == goal: #if we reached the goal from a path we add the path to our set of paths and its length to our set of lengths
        set_path.append(path.copy())
        lengths.append(distance)
    else: # else we go and dfs on the rest of the vertices to get the rest of the paths
        node = 0
        for i in adj_matrix[vertex]:
            if i != 0:
                if visted[node] == False:
                   brute_force(node,vertex,goal)

            node = node + 1
            
    visted[vertex] = False #after checking all the nodes of this vertex we set it to falls so we can get diffrent paths from other nodes
    x = path.pop() # we pop it from our path since its not visited anymore
    distance = distance - adj_matrix[parent][x] # and decrease its value from our current distance



def main():
    matrix_size = 0
    global V
    global path
    global set_path
    global lengths
    global distance
    # taking input O(V^2)
    while True:
        try:
            for value in input('').split('\n') :
                row_input = []
                for num in value.split(' '):
                    if(num != ''):
                        row_input.append(num)
                matrix.append(row_input)
                matrix_size = matrix_size + 1
        except (EOFError):
            break
    #creating adjacency matrix O(v^2)
    for i in range(len(matrix[0])):
        row_input = []
        for value in matrix[i+1]:
            row_input.append(int(value))
        adj_matrix.append(row_input)
    #creating visted matrix O(V)
    for i in range(len(matrix[0])):
        visted.append(False)
    index = 0
    #creating translation from num to letter and vice versa matrix O(v)
    for item in matrix[0]:
        let_num[item] = index
        num_let[index] = item
        index = index + 1

    # calling dfs and then selecting the min path O(n*(l+p)) since its only going to repeat for the number of input n and 
    # length of the path l and number of possible paths p
    for i in range(len(matrix[0])+1,matrix_size):
        brute_force(let_num[matrix[i][0]],-1,let_num[matrix[i][1]])
        min = 999
        min_index = -1
        for z in range(len(set_path)):
            if lengths[z] < min and len(set_path[z]) <= 4:
                min = lengths[z]
                min_index = z
        if min_index != -1:
            index = 0
            for item in set_path[min_index]:
                if index < (len(set_path[min_index])-1):
                    print(num_let[item],end=' ')
                else:
                    print(num_let[item],end='\n')
                index = index + 1

           
            
        else:
            print('no path exists')
        # re intializing our variables
        set_path = []
        lengths = []
        path = []
        distance = 0
        for i in range(len(visted)):
            visted[i] = False
  
    
            

main()