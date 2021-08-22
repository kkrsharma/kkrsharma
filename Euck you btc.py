import random, subprocess, secrets
import os
list5 = "cuBitCrack.exe 1PWABE7oUahG2AFFQhhvViQovnCr4rEv7Q 16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN -o found.txt -b 40 -t 512 -p 128 -c -u --continue save4.txt --keyspace "
for y in range (100000000000000):
        #list1 = secrets.token_hex(32).upper()
        list5 = list5 + "8064D7E980000000:FFFFFFFFFFFFFFFF"
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call(list5, creationflags = CREATE_NO_WINDOW)
        
