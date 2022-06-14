import os
import hashlib

salt = os.urandom(32)                                   #Generating a random salt 
password = 'AVeryNotSecurePassword111'


hashed_key = hashlib.pbkdf2_hmac(                       #Hashing using pbkdf2_hmac
	'sha256', 											#Using SHA-256 hash digest algorithm since no key length was provided
	password.encode('utf-8'),							#Converting password to bytes
	salt,												#Providing the salt
	1000000												#Number of SHA-256 iterations
)

storage = salt + hashed_key                             #Storing salt and hashed_key in storage

salt_from_storage = storage[:32]                        #Retriving salt
hashed_key_from_storage = storage[32:]                  #Retriving hashed key


print("salt", salt_from_storage)                        #Printing salt
print("hashed key", hashed_key_from_storage)            #Printing hashed keys