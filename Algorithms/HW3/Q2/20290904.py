#Time complexity of O(MN) where M is the number of leafs frog A wishes to visit and N is the number of leafes frog B wishes to visit

#Where we store our input
frog1 = [] #frog A
frog2 = [] #frog B



# Helper function to help us calculate the distance between the two frogs
def distance(x,y):
    if x > y:
        return (x - y)
    else:
        return (y - x)

# here is our dynamic algorithm it will help us determin if there 
# exists an order of jumps that satisfies the given restrictions
# Bottom up approach

#it will iterate through each leaf from both frogs making its time complexity O(MN)
def dynamic_algo():
    ind_A = 0 # to store which leaf is frog A currently at
    ind_B = 0 # to store which leaf is frog B currently at

    while not((ind_A+1) == len(frog1) and (ind_B+1) == len(frog2)): # we continue iterating until both frogs reach their final leaf or both are unable to can

        if ((ind_A+1) != len(frog1) and distance(frog1[ind_A + 1],frog2[ind_B]) <= 100 ): # we continue to iterate through Frog A leafs 
                                                                                          # as long as we aren't further than 100cm than frog B 
            ind_A = ind_A + 1                                                             # or there is no leafs left  

        elif((ind_B+1) != len(frog2) and distance(frog1[ind_A],frog2[ind_B + 1]) <= 100): # if we can't move frog A then we move in frog B following the same conditions
            ind_B = ind_B + 1
        else: # and if both reach their final leaf or unable to reach it we break the loop
            break
    if ((ind_B+1) == len(frog2) and (ind_A+1) == len(frog1)): # if they reached the final leaf we print True 
        print("true")
    else: # if not we print false
        print('false')



def main():
    #taking input
    global frog1
    global frog2
    # O(M+N)
    while True:
        try:
            frog1 = [int(value) for value in input('').split()]
            frog2 = [int(value) for value in input('').split()]
            
        except (EOFError):
            break
    dynamic_algo()


    


main()
    


