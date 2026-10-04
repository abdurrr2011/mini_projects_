import os, sys


#encrypt and decrypt the password

pwd = input("What's your password? ").lower()

def view():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():
            our_data = lines.rstrip()
            if '#' in our_data:
                user, password = our_data.split("#")
                print(f"User: {user} and Password: {password}")
            

def add():
    name = input("Account Name : ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(f"{name}#{pwd}\n")
     
while True:
    mode = input("Would you like to add a new password or view existin' ones (view/add) or 'q' to quit? ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue
    
    
    
list_of_your_ = os.listdir()


sys.exit()