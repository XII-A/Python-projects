
#Time complexity of O(n)

people = []#this where we store the input
stack = [] #our stack

#function to ask if person 1 knows person 2
def do_u_know(person1,person2):
    if people[person1][person2] == '1':
        return True
    else:
        return False

#function to find out if there is a celebrity among the input
#we push all of the ids of everyone into a stack
# we pop the two two elements from the stack 
#if person 1 knows person 2 then person 1 cant be the celebrity so we don't push it back into the stack
#else if person 2 knows person 1 they can't be the celebrity so we don't push it back into the stack
#so this would lead to decrease the number of the people in out input so we would achieve a decrease and conqure type of solution 
def get_potential_C():
    could_be_C = -1 

    #pushing everyone into the stack
    for i in range(len(people)):
        stack.append(i)
    #run the loop as long as there is more than 1 person remaining in the stack
    #Time complexity of O(n)
    while len(stack) > 1:
        #pop out the top two elements of our stack
        person1 = stack.pop()
        person2 = stack.pop()
        #asking if one of them knows the other
        if do_u_know(person1,person2):
            stack.append(person2)
        else:
            stack.append(person1)
    #if no one is left in the stack that means there was no celebrity left
    if len(stack) == 0:
        print('-1')
        return -1
    #the celebrity wasn't teasted with the last two people so we make sure we got the correct celebrity here
    could_be_C = stack.pop()
    if do_u_know(could_be_C,person2):
        could_be_C = person2

    if do_u_know(could_be_C,person1):
        could_be_C = person1
    
    return could_be_C

#function to make sure that the celebrity we found is known by everyone and doesn't know anyone
def check_for_celebrity():
    
    
    could_be_C = get_potential_C()

    if could_be_C == -1:
        return
    #iterating through everone if anyone doesn't know our celebrity then there is no celebrity
    #and if our celebrity knows anyone then there is no celebrity
    #Time complexity of O(n)
    for i in range(len(people)):
        if (i!= could_be_C):
            if(do_u_know(could_be_C,i)):
                print('-1')
                return -1
            if(not do_u_know(i,could_be_C)):
                print('-1')
                return -1

    print(could_be_C)
    

def main():
    #taking input
    person = ''
    while True:
        try:
            person = input('').split()
            people.append(person)
        except EOFError:
            break
    #calling the function to find if there is any celebrity in the input
    check_for_celebrity()
    
main()