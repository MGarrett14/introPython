# while loop

i = 1 #iterator

while i < 6: # condition/scenario we want to check for

    print(i) # instruction on what do to next 
    i += 1 # increment - the number of times we want to do it

    # conditional statemnt
    def password_code():

        user_password_attempt= input('please enter a password')
        actual_password= 'blch'

        i = 0 
        while i < 3:
                if user_password_attempt  == actual_password:
                        print('password is correct. Please enter.')
    break

else:
            print('Invalid password, try again')
password_code()