from queue import Queue

# This function whether the graph is Bipartite or not since Bipartite graphs don't have odd cycles

# we implement it via a modified version of BFS

# Time Complexity of O(n+m) where n is the number of nodes and m is the number of edges in the graph

def check_odd_cycle(graph,num_inputs):
    # 0 means white
    # 1 means gray
    # 2 means black
    color = [] #color array to store the color of our nodes

    #initializing the color array with 0s
    for i in range(num_inputs+1):
        color.append(0)
    #initializing the intial state with color gray
    color[0] = 1
    #initializing an empty queue 
    g_queue = Queue() 
    g_queue.put(1)

    #we keep itreating until our queue is empty
    while not g_queue.empty():
        u = g_queue.get()
        for neighbor in graph[u]:
            if color[neighbor] == 0:
                if color[u] == 1:
                    #for all neighbors of u we assign an alternate color
                    color[neighbor] = 2
                else:
                    color[neighbor] = 1
                g_queue.put(neighbor)
            #u and its neighbor have the same color which would disqualify it as a Bipartite and it has an odd cycle 
            elif color[neighbor] == color[u]:
                return True
    #since we got here than we have a Bipartite graph and no odd cycle could exist
    return False




def main(args=None):
    #taking input
    num_inputs = int(input(''))
    items = []
    graph = {}
    for i in range(num_inputs):
        vertex = input('').split()
        for j in range(num_inputs):
            if vertex[j] == '0': #if there is no edge between the nodes we don't put it in the graph array
                continue
            elif vertex[j] == '1':#if there is an edge we add it to the graph array
                items.append(j+1)
                graph[i+1] = items
        items = []
    #calling our function to check for odd cycles
    x = check_odd_cycle(graph,num_inputs)
    if x:
        print('true',end='')
    else:
        print('false',end='')


main()