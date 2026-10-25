from io import BufferedReader
import os, sys
import base64, hashlib
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken


#encrypting and decrypting
"Plaintext + Encryption algorithm + key = Ciphertext"
"Ciphertext + Decryption algorithm + key = Plaintext"
"Yeah, i agree that it also can be 'Ciphertext - Encryption algorithm - key = Plaintext', But the value: (-encryption algorithm its = decryption algorithm) AND (-key its = likewise, just +key because there is no oposite meaning of 'key' so that all i wanned to express,maboy.)"


def write_key() -> None:
    if not os.path.exists(path="key.key"):
        key: bytes = Fernet.generate_key()
        with open(file="key.key", mode="wb") as key_file:
            key_file.write(key)

write_key()
        
        
def read_key() -> bytes:
    with open(file="key.key", mode="rb") as file:
        key: bytes = file.read()
        return key


logn: str = input("What's your name(login) ").lower().rstrip()
pwd1: str = input("What's your password? ").lower().rstrip()

file =  Path('passwords.txt')
 

# our data_key
key: bytes = read_key() + pwd1.encode()

# Magic fixing : Hashing into a 32-bytes
hashed_key: bytes = hashlib.sha256(data=key).digest()

# Encoding into a format, which requires a Fernet
fernet_key: bytes = base64.urlsafe_b64encode(hashed_key)

fer = Fernet(fernet_key)


if not file.exists():
    file.touch()


if logn == '':
    logn = 'Empty'
if pwd1 == '':
    pwd1 = 'Empty'
    
encrypted_master_pwd: str = fer.encrypt(data=pwd1.encode()).decode()
with open(file, mode='a') as f:         
        f.write(f"(.) {logn}#{encrypted_master_pwd}\n")

def view() -> None:
    if os.path.getsize(filename=file) == 0:
        print('A File is absolutely empty.')
        return
    
    with open(file, mode='r') as f:
        for lines in f.readlines():
            our_data: str = lines.rstrip()
            if '#' in our_data:
                user, password  = our_data.split(sep="#", maxsplit=1)
                try:
                    decrypted_password: str = fer.decrypt(token=password.encode()).decode()
                    print(f"user: {user} and Password: {decrypted_password}")
                except InvalidToken:
                    print(f"user: {user} and Password: [Error: Invalid Master Password or Corrupted Data]")
        
                 

def clear() -> None:
    with open(file='passwords.txt', mode='w', encoding='utf-8') as f:
        pass
 
            
def add() -> None:
    name: str = input("Account Name : ")
    pwd: str = input("Password: ")
    
    encrypted_pwd: str= fer.encrypt(data=pwd.encode()).decode()

    with open(file="passwords.txt", mode="a") as f:
        f.write(f"{name}#{encrypted_pwd}\n")

     
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