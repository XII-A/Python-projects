from math import *

# Tn()=2T(n/2)+n
# Time Complexity = O(nlogn)


#here we store the value of our product
product_r = []

def product_Ak_v(k,product_r,vector,A_k):
    #the base case to stop the recursion
    if k == 0:
        return
    
    i = 0
    j = 0
    n = int(pow(2,k))
    middle = int(pow(2,k-1))
    #finding (Akv)1 = Ak−1v1 + Ak−1v2 = Ak−1(v1 +v2)
    for i in range(j,middle,1):
        product_r.append(vector[i] + vector[i+middle])
    # finding the subtraction, (Hkv)2 = Hk−1v1 −Hk−1v2 = Hk−1(v1 −v2)
    for i in range(middle + j, n , 1):
        product_r.append(vector[i - middle] - vector[i])
    #sending the result to our next function call
    for i in range(0,n,1):
        vector[i] = product_r[i]
    
    product_Ak_v(k-1,product_r,vector,A_k)
    product_Ak_v(k-1,product_r[middle:],vector[middle:],A_k)




def main():

    #taking input
    vector = []
    value = ''
    while True:
        try:
            value = input('').split()
            vector.append(int(value[0]))
        except EOFError:
            break
    n = len(vector)
    k = log2(n)

    A_k = [[]]
    #my result
    product_Ak_v(k,product_r,vector,A_k)
    #printing the output
    for i in range(len(product_r)-1):
        print(product_r[i])
    print(product_r[len(product_r)-1],end='')
        
    

    

main()