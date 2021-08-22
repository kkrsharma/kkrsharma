import random, subprocess, secrets
import os
from bitcoin import *
list3 = '0', '0', '0', '0', '0', '0', '0'
list4 = 'F', 'F', 'F', 'F', 'F', 'F', 'F'
list5 = "cuBitCrack.exe -i "
list7 = " -o found.txt -b 30 -t 512 -p 128 --keyspace "
yy = 0
for y in range (1000000):
        for x in range (49):
            num = 0
            #list1 = secrets.token_hex(32).upper()
            list1 = random_key().upper()
            list1 = list1[:57]
            value1 = value = list1
            value1 = value1 + "".join(list4)
            value = value + "".join(list3)
            value3 = list5 + "x" + str(yy) + list7
            print(value1, value)
            value3 = value3 + value + ":" + value1
            for num in range(124):
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(value3, creationflags = CREATE_NO_WINDOW)
                if yy == 123 :
                        yy=0
                elif yy < 123 :
                        yy = yy + 1
                value3 = list5 + "x" + str(yy) + list7
                value3 = value3 + value + ":" + value1
