# while loop = a keyword that allows us to
# repeat a block of code indefinitely/ continously/
# infinitely
i= 0

while i < 1:
    print('hello')
    i+=1








# 1. Provided below is some starter code. 
# Fix this code to create a loop that will iterate
# until it gets to the number 10.

# hint: remember there are 3 parts to a loop. 
i=0
while i:
# insert missing code.
    print('insert missing value')
    # insert missing code here

# 2. Create a simple while loop that will iterate over a the following condition:
# The loop will ask the user to enter the secret number. The secret number is 3. 
# If the user enters the secret number correctly, the loop will stop and tell the user
# the can win a prize. 
# If the user puts in an incorrect secret number, the loop will ask them to enter the 
# correct secret number. 

user_number= input('what is the code.')

while user_number != '3':
    print(' not correct! please enter the correct password.')

    user_number= input('what is the code:')

    print('correct! Here is your prize')




# 3. describe the difference between a while loop and a conditional statement. 
# Try be as specific as you can

# A while loop is a code that will forever loop and it only print if the statement is correct.
# A conditional statement is a block of code that will execute if a specific condition is met

# 4. Create a while loop that will iterate over the list of names 
# and print out only the following name: William

names= ['Avery','Paige','William','Ade','Jasmyn','Crystal']


# 5. Create a loop that will ask the user to add a new string value to the list of names above.
# hint you will need use append().

# BONUS QUESTION
# Describe the differences between a FOR loop and WHILE loop. 

# The difference between a WHILE loop and a FOR loop is that a while loop prints a set of statements if 
# the condtions are true, and FOR loop iterates over a sequence like a list or string