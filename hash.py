import hashlib
import os 
import sys

os.system("clear")

print ("=================")
print ("=    HashFuck   =")
print ("=================")
print ("")
print ("Create By Ghost")
print ("")

flag = 0

pass_hash = input("ENTER MD5 HASH > ")

wordlist = input("FILE NAME > ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No Found password")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest == pass_hash:
      print("password found")
      print("password is " + word)
      flag = 1
      break

if flag == 0:
    print("password/passhrase is not in the list ")