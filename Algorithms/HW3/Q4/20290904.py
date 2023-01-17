#time complexity of O(N^2) where N is the number of items given in the input

values = [] #this is where I store the input
result = [] #this is where I store the result

# to save as much money as possible we pick the most two expensive items 
# on each iteration in our greedy algorithm and pair them together

# our greedy algo
# on each iteration we look for the two most expensive items and pair them
def greedy_algo():
    #here we are doing a form of selection sort with time complexity of 2N^2 which is O(N^2) where N is the number of items given in the input
    while len(values) != 0:
        pair = [] # here we store our pair
        pair_v1 = 0 # we store the first item of the pair
        pair_v2 = 0  # we store the secound item of the pair
        max_v = -9999 # we store the current biggest value
        for i in range(len(values)): # iterating through each value and checking wether it's the biggest value
            if values[i] > max_v:
                max_v = values[i] # if it is we store its value
                pair_v1 = i # and we store its index
        pair.append(values[pair_v1]) # we add it to our pair list
        values.pop(pair_v1) # and remove it from the list of items so we don't check it again
        max_v = -9999 # reseting the current max before looking for the secound item in the pair
        for i in range(len(values)): #looking for the secound biggest value to store in the pair
            if values[i] > max_v:
                max_v = values[i]
                pair_v2 = i
        pair.append(values[pair_v2]) # we add it to the pair
        values.pop(pair_v2) # we remove it so we don't check it again
        result.append(pair) # append the pair to our result list

        
        




def main():
    #taking input
    global values
    # time complexity of O(n) where n is the number of items given
    while True:
        try:
            for value in input('').split() :
             values.append(int(value))
        except (EOFError):
            break
		
    #calling our function
    greedy_algo()
    #printing our result
    # time complexity of O(n) where n is the number of items given
    for item in result:
        print(f"{item[0]} {item[1]}")

    print()

main()


#-------------proof for the correctness--------------
# Assume there is an optimal sequence of pairs S*
# in which items haven't been paired according to the biggest value
# then there should be item i and j such that Price j > Price i and they are not paired together 
# assume the total cost of S* is C where j is paired with x and price j > price x and price i > price x 
# and i is paired with y and price i > price y and price y < price x
# then what would happen if we pair j with i and pair x with y?
# when we pair item j and i the total cost is C* and C - C* = price i - price y (the amount of money we saved more)
# which leads to a contradiction