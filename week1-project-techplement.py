import time

chars = ''
pswrd = ''
mod = 2**32

while (True) :
    print("")
    print("Random Password Generator")
    print("     1 - Generate new password")
    print("     2 - Revisit last password")
    print("     3 - Exit")
    inp = input("Enter your choice (1/2/3): ")
    seed = int(str(time.time() % 17).replace('.',''))
    
    if (inp == "3"): 
        print("Thank you for using Random Password Generator")
        print("")
        break
    elif (inp == '2'): 
        if (pswrd == ''): print("No previous password generated")
        else: print(pswrd)
    elif (inp == '1'):
        pswrd = ''
        
#customize length
        while (True) :
            length = int(input("Enter length for new password: "))
            if (length > 0 and length <= 20): break
            else: 
                print("Please enter valid length between 0 to 20 characters")
                print("")

#customize charset
        choice = input("Do you want to include Uppercase Letters in the password? (Y/n)")
        if (choice.lower() == 'y' or choice.lower() == 'yes'): chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        choice = input("Do you want to include Lowercase Letters in the password? (Y/n)")
        if (choice.lower() == 'y' or choice.lower() == 'yes'): chars += 'abcdefghijklmnopqrstuvwxyz'
        choice = input("Do you want to include numeric characters in the password? (Y/n)")
        if (choice.lower() == 'y' or choice.lower() == 'yes'): chars += '0123456789'
        choice = input("Do you want to include special characters in the password? (Y/n)")
        if (choice.lower() == 'y' or choice.lower() == 'yes'): chars += '`~!@#$%^&*()?'
        print("")

        if (len(chars) == 0): 
            print("You've selected an empty character set! Try again!")
            continue
        
#generate password
        print("...generating...password...")
        for _ in range(length):
            seed = (1664525 * seed + 1013904223) % mod   
            index = seed % len(chars)
            pswrd += chars[index]

        print(pswrd)
        #print(len(pswrd))

    else : 
        print("Inappropriate choice, try again!")


    