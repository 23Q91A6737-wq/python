# encryption program


import random
import string

#  actual code -> chars = string.punctuation + string.digits + string.ascii_letters
#                 print(chars)



# for decoration

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)       #  convert into list . for example [ 'a' , 'b' , 'c' ]

key = chars.copy()     # Creating a key, which we will shuffle eventually  . then to create a copy of a list , you can type the original list.

random.shuffle(key)


#print(f"chars :{chars}")
#print(f"key : {key}")

#Encrypt

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")

#Decrypting

cipher_text = input("Enter a message to decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message : {cipher_text}")
print(f"original message  : {plain_text}")