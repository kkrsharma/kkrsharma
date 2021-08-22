import random, subprocess
import os
for y in range (10000):
        for x in range (49):
            for num in range(10):
                list1= 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                list3 = '0', '0', '0', '0', '0', '0', '0' 
                list4 = 'F', 'F', 'F', 'F', 'F', 'F', 'F' 
                list5 = "cuBitCrack.exe -i sort.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
                value1 = value = "".join(random.choices(list1, k=x+9))
                value1 = value1 + "".join(list4)
                value = value + "".join(list3)
                value3 = value + ":" + value1
                value3 = list5 + value3
                print(value3, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(value3, creationflags = CREATE_NO_WINDOW)
    
