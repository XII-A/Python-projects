#time complexity of O((N^2)*M) where N is the number of floors and M is the number of snooker balls 


values = [] # here we store our input
memoization = [] # here is our database to store the result of overlapping subproblems


# here is our dynamic algorithm
# it has a time complexity O((N^2)*M) since we reenter each floor twice with each ball it lead to N^2 where N is the number of floors and M is the number of snooker balls
# Bottom up approach
def Dynamic_algo(N, M):
	# our base cases
	# 1) if the number of floors left is just 1 or 0 then we don't need to check further and just return the value of the floors left
	# and it's gonna be the amount of snooker balls drops we have to do
	# 2) if the number of snooker balls left is just 1 then the min amount of snooker balls we have to drop
	#  is going to be N since we have to throw the ball from floor 1 till N
	if ((N == 1 or N == 0) or (M == 1)):
		return N

	# in case we already solved the same subproblem before we check in our database instead of solving it again
	elif (memoization[M][N] != -9999):
		return memoization[M][N]
	# if the problem wasn't in our database nor it's one of our base cases we solve it via top down approach 
	else:
		minValue = 99999 # creating a variable to store the current min amount of snooker balls drops we have to do
		#iterating through each floor
		for i in range(1 , N+1):
			# in each floor i there is two possible cases
			# 1) the ball breaks so we have to check all the floors from i-1 till 1
			# 2) the ball doesn't break so we check all the floors left above i
			# and
			result = 1 + min( (max(Dynamic_algo(i - 1 , M - 1), Dynamic_algo(N - i,M))) # we choose the max since we want to calculate the min amount of ball drops we need to do among all worst cases
			if (minValue > result):
				minValue = result + 1 # if the result is less than our current min we assign it to our current min 
									  # and we are adding one to the result to account for the ball drop we did at floor i 
		memoization[M][N] = minValue # storing the result of the subproblem in our database so we don't solve it again
		return minValue	




def main():
    global memoization
    global values
	#taking input
    while True:
        try:
            for value in input('').split() :
             values.append(int(value))
        except (EOFError):
            break
		
	#initializing our data base with the number of floors and snooker balls
    memoization = [[-9999]*(values[0]+1) for i in range(values[1]+1)]
    print(Dynamic_algo(values[0], values[1]))
    print()

main()

