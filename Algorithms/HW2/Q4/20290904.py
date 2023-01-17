#sources for append and extend time complexity
#1- https://www.geeksforgeeks.org/append-extend-python/ at the end of the page for the mentioned time complexities
#2- https://wiki.python.org/moin/TimeComplexity


string = input(''); 
# The .append method in python has the time complexity of 1 so this will allow our for loop time complexity to stay as O(n)
# So we will iterate through the array and add each element to the array it belongs in via .append()
B_list = []
M_list = []
W_list = []
merged_list = []
for c in string:
    if c == 'B':
        B_list.append(c)
    if c == 'M':
        M_list.append(c)
    if c == 'W':
        W_list.append(c)
#after adding all the elements to their arrays we merge them all in one array via the .extend() method which has the time complexity 
# of O(k) where k is the length of the list which needs to be added 
merged_list.extend(B_list)
merged_list.extend(M_list)
merged_list.extend(W_list)

#Time complexity O(n) Linear time

print(''.join(merged_list),end='')

