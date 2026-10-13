import os, sys
from pathlib import Path
from cryptography.fernet import Fernet


#encrypting and decrypting
"Plaintext + Encryption algorithm + key = Ciphertext"
"Ciphertext + Decryption algorithm + key = Plaintext"
"Yeah, i agree that it also can be 'Ciphertext - Encryption algorithm - key = Plaintext', But the value: (-encryption algorithm its = decryption algorithm) AND (-key its = likewise, just +key because there is no oposite meaning of 'key' so that all i wanned to express,maboy.)"


logn: str = input("What's your name(login) ").lower().rstrip()
pwd1: str = input("What's your password? ").lower().rstrip()

file =  Path('passwords.txt')

with open(file, mode='a') as f:
        if logn == '':
            logn = 'Empty'
            if pwd1 == '':
                pwd1 = 'Empty'
        f.write(f"(.) {logn}#{pwd1}\n")

def view() -> None:
    with open(file, mode='r') as f:
        for lines in f.readlines():
            our_data: str = lines.rstrip()
            if '#' in our_data:
                user, password  = our_data.split(sep="#")
                print(f"user: {user} and Password: {password}")
            elif file.exists() and file.stat().st_size == 0:
                print("File is empty.")
                

def clear() -> None:
    with open(file='passwords.txt', mode='w', encoding='utf-8') as f:
        pass

            

def add() -> None:
    name: str = input("Account Name : ")
    pwd: str = input("Password: ")
    
    with open(file, mode='a') as f:
        f.write(f"{name}#{pwd}\n")
     
while True:
    mode: str = input("Would you like to add a new password or view existin' ones (view/add) or 'q' to quit or 'c' to clear datas? ").lower().rstrip()
    if mode == 'q':
        break
    
    elif mode == 'view':
        try:
            view()
        except FileNotFoundError:
            print('Sorry, you have not writen any name and password into')
            break
    elif mode == 'add':
        add()
    elif mode == 'c':
        clear()
    else:
        print('Invalid mode.')
        continue
    
    
    
list_of_your_path: list[str] = os.listdir()


sys.exit()