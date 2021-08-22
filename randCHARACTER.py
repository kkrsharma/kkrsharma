import random, subprocess
import os
list1 = 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
list3 = '0', '0', '0', '0', '0', '0', '0'
list4 = 'F', 'F', 'F', 'F', 'F', 'F', 'F'
list5 = "cuBitCrack.exe -i "
list7 = " -o found.txt -b 30 -t 512 -p 128 --keyspace "
yy = 0
for y in range (1000000):
        for x in range (49):
            num = 0
            list1 = "".join(random.choices(list1, k=x+9))
            value1 = value = list1
            value1 = value1 + "".join(list4)
            value = value + "".join(list3)
            value3 = list5 + "x" + str(yy) + list7
            value3 = value3 + value + ":" + value1
            for num in range(124):
                print(value3)
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(value3, creationflags = CREATE_NO_WINDOW)
                if yy == 123 :
                        yy=0
                elif yy < 123 :
                        yy = yy + 1
                value3 = list5 + "x" + str(yy) + list7
                value3 = value3 + value + ":" + value1
