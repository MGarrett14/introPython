# 1. In your own words, describe what a function is
"A function is a type of abstractions that lets us simplify code "
"just a bit by being able to write code and contain a code in a certain way"
"for better molduarity and to be resuable"

# 2. What is are function parameters and arguments and describe
# the difference between the 2. 
'function parameter is a placeholder- goes in function defintion.'
'function argument is the actual data- goes in function call'
# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
def addTwo(randomNumber):
    print(randomNumber + 2)

    addTwo(2)
    addTwo(10010)



def welcome_msg(username):
    print('welcome' + 'to coding class')

    welcome_msg('Mekhi')




# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)
def calculate(randomNumber, randomNumber2, randonNumber3):
    print(randomNumber + randomNumber2 + randomNumber)

calculate('7', '100','700')
    


# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.
def userMsg():
nextClass = input('what is your next class.')
print('you have' + 'nextClass' + 'after this')

   
userMsg()



# write a condition statement for if the sun is out

if sun_is_out = True
   print( 'do nothing')

   if sun_is_out === True:
      print('do not turn on street lamps')

   else: 
       print('turn on street lamps')