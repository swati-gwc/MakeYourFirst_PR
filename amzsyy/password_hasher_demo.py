import os                                                                           #Importing required libraries
import hashlib

people = {}                                                                         #Storage for usernames and passwords

username = input("Please input a new username: ")                                   #UI for uname
password = input("Please input a new password: ")                                   #UI for pswd

salt = os.urandom(32)                                                               #Generating a random salt for a user
key = hashlib.pbkdf2_hmac(                                                          #Hashing using pbkdf2_hmac
    'sha256',                                                                       #Using SHA-256 hash digest algorithm since no key length was provided
    password.encode('utf-8'),                                                       #Converting password to bytes
    salt,                                                                           #Providing the salt
    100000                                                                          #Number of SHA-256 iterations
)
storage = salt + key                                                                #Storing salt and hashed_key in storage

salt_from_storage = storage[:32]                                                    #Retriving salt
key_from_storage = storage[32:]                                                     #Retriving hashed key

people[username] = {
    'salt': salt,
    'key': key
}

username = input("Please input old username: ")                                     #UI for old uname
password = input("Please input old password: ")                                     #UI for old pswd

salt = people[username]['salt']                                                     #Getting the salt
key = people[username]['key']                                                       #Getting to correct key
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)     #Hashing new key

if key == new_key:
    print("Authentication successful")                                              #Comparing new key to user's key
    print("The users salt is: ", salt_from_storage)                                 #Printing salt
    print("The users hashed key is:", key_from_storage)                             #Printing hashed key
else:
    print("Authentication failed")
