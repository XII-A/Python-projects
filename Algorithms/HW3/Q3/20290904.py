#time complexity of O(N^2)

items = {} #this is where we store the input
result = [] #this is where we store the result



#to minimize our total cost we created a greedy function that would pick 
#the most expensive item each month since it will save us the most money on the following month



#our greedy function 
#in each iteration we pick the item with the highest value and append it to our result array
def greedy_algo(num_values):
    index_v = 0 #variable to store the index of the biggest value among the items
    max_v = -9999#variable to store the current biggest value among all items
    #here we are doin a form of SELECTION SORT which has a time complexity of N^2 where n is the number of items in the in the input given
    while num_values > 0:#we keep iterating in the dictionary until its empty
        for i in items.keys():#we check the value of each key(item) and compare it against our max_v
            if items[i] > max_v:#if its bigger we store its value and its index
                max_v = items[i]
                index_v = i
            items[i] = items[i]*2#we mult the value of all items by 2 for the next iteration
            
        result.append(index_v)#we add the biggest item to our result array 
                              #and it would be in the correct place since we are looking for the biggest one first 
                              #then the secound one and so on
        items.pop(index_v)   #then we remove the item from the dictionary so we dont iterate over it again
        max_v = -9999        #reset the max_v and index_v to their intial values
        index_v = 0
        num_values = num_values - 1 #decreasing the number of items we have by 1 so we know when its empty
        

    
    
def main():
    #taking input
    num_values = 0
    while True:
        try:
            values = input('').split()
            items[int(values[0])] = int(values[1])  
            num_values = num_values + 1
        except (EOFError,IndexError):
            break

    
    greedy_algo(num_values)
    # print(result)
    for i in range(len(result)-1):
        print(f"{result[i]}",end=' ')

    print(f"{result[len(result)-1]}")
    print()

        


main()

#-------------proof for the correctness--------------
# Assume there is an optimal sequence S*
# in which the items haven't been picked according to the biggest price. 
# Then there should be indices i and j such that i < j and Price j > Price i
# what happens if we picked item j first?
# the total cost of the optimal sequence S* is C containig (Price j)*(2^(i+1)) and (Price i)*(2^(i))
# Then when we buy item j first before item i and the total cost becomes C* containing (Price j)*(2^(i)) and (Price i)*(2^(i+1))
# And since j is bigger than i we can conclude that C* is smaller than C which leads to a contradiction




