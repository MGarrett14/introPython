# 1. Create a function that will multiply two (2) values that are passed into the function as arguments. 
# Your function should print out the result of the two numbers that have been multiplied.
list_numbers=[2,6]

def multiplier():
    list_numbers=[2,6]
    for n in list_numbers:
        print(n*2)

multiplier()

# 2. Creat a function that will do the following calculation. Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided by the third argument. 
# Your function should then print the result. 
list_numbers=[2,6]

def addition():
    list_numbers=[2,6]
    for n in list_numbers:
        print(n+2)

        addition()




# 3. Create a elevator function that will run specific lines of code based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, if the input doesnt match any of the values provided, tell the user that floor doesn't exist and to please
# enter a valid floor number.

def elevator():
    elevator_floor= imput('what floor do you want to go to?')
if elevator_floor== 203:

    print('you are going to the gym')

elif elevator_floor== 'g'
print('You are going to the lobby')
# hint you will need to look into using conditional statements

# 4. Write a simple conditional statement that uses a boolean that will print if it is daytime or nighttime.
sunIsout= True

if sunIsout= True:
    print('The sun is out')

else:
    print('It is night time')

# 5. What function would you use if you wanted to add and element/ value to a list data type? Explain why you would use it.
'You would use append if you wanted to add a element/value to a list of data types.' 
'You would use it '

                                  

# 6. Do some research and find the correct built-in python function that will reverse the order of the following list.
# then print your list in the reverse order.

random_number_list = [0,1,2,3,4,5,6,7,8]
random_number_list.reverse()
print(random_number_list)


# 7.Do some research and find the correcrt built-in python function that will allow you to find the largest number in the following list.
# then print the largest number
ranom_number_list2 = [100,230,40,39403,19]

largest_number= max(random_number_list)
print(largest_number)

# 8. A security company has hired you as an engineer to help them develop a program that will only let users into the building 
# if they enter a specific password. They given you the following information to use to build this program.
# - they want users to be able to enter a series of codes to get access
# - they want the user to enter an initial password value which is 0001
# - if they get this correct, they then want them to enter another value, which is 3039
# - if this is correct they will get access to the building
# - if they have the wrong answer in either scenario they will get a message saying access denied.
def building_code():
    code = int(input('What is the code to enter the building'))

    if code== 1920:
        print('great! please enter second code.')
    code2== int(input('What is the second code?'))
    
    if code2==30309:
        print('cot, please try again')

    else:
        print('You may now enter the building')


        building_code()

# 9. What does it mean to call a function? Why do we call functions. 
# you can use the variable below to enter you ansewer. 
answer9='To call a function is to put the function name again with the round brackets at the end of our code.'
'We call functions so our code will work, if we dont call the function the code will have an error'

# 10. Find and print each value at the specific indexes provided in the list.
# find and print the values/words at index 3, 4, and 6 

shopping_cart = ['apples','water','chicken','ice cream','ground beef','string beans','oranges']

print(shopping_cart[3])

print(shopping_cart[4])

print(shopping_cart[6])