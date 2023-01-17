#using brute force we sorted the tasks via selection sort with 
#and then iterating till the last unit of time in the deadline and finding maximum profit in each deadline
#TIME EFFICIENCY O(n^2) 

# Taking input------------------------------
num_inputs = int(input(''))

tasks = []
for i in range(num_inputs):
    task = input('').split()
    tasks.append([int(num) for num in task])
#-------------------------------------------


# task[i][0] = id
# task[i][1] = deadline
# task[i][2] = profit

#A function so we can move the task from one index to another index in the array
def switch(i,j):
    values = [tasks[i][0],tasks[i][1],tasks[i][2]] 
    tasks[i][0] = tasks[j][0]
    tasks[i][1] = tasks[j][1]
    tasks[i][2] = tasks[j][2]

    tasks[j][0] = values[0]
    tasks[j][1] = values[1]
    tasks[j][2] = values[2]


#sorting the jobs in decreasing order of deadline 
#Selection Sort with time efficiency of O(n^2) where n is the number of tasks
for i in range(num_inputs):
    current_min = 9999
    current_min_i = 99999
    for j in range(i,num_inputs):
        if tasks[j][1] < current_min:
            current_min = tasks[j][1]
            current_min_i = j

    if current_min_i != 99999:
        switch(i,current_min_i)



result = [] #an array to store the result in
current_time = 1 # a variable to keep the track of the time

#we look for the maximum profit in each deadline by checking the whole list of tasks
#time efficiency of O(n*m) where n is the number of tasks and m is the value of the last deadline with a task
for i in range(tasks[num_inputs-1][1]):# iterating till the last unit of time in the deadline 
    current_max = -9999
    current_max_i = -9999
    for j in range(num_inputs):# iterating through the tasks
        if current_time == tasks[j][1]:
            if tasks[j][2] > current_max: #looking for the task with the highest profit
                current_max = tasks[j][2]
                current_max_i = j
        
    if current_max_i != -9999:
        result.append(tasks[current_max_i])

    current_time = current_time + 1
    

#printing the output

for i in range(len(result)-1):
    print(result[i][0], end =' ')

print(result[len(result)-1][0],end = '')





    