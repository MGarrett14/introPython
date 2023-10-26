# 1. In your own words, describe what a for loop is?
'a for loop is a loop that iterates over a sequence like list, dictionary, set, or a string'

# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 
'the difference between a FOr loop and a WHILE loop is that a WHILE loop executes a loop of code for' 
'a indefinetely amount of times and a FOR Loop that loops a block of code for a specific amount of times'


# for loop
def fruitFunction():
    fruits = {'oranges', 'grapes', 'pineapple', 'watermelon','kiwi'}
    for x in fruits:
        print(x)

# while loop
i=0
copies= int(input('how many copies do you want?'))

while i < copies:

    print('heres your document')
    break



# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']
for firstletter in names:

    if firstletter[0] !== 'R':
        print(firstletter)