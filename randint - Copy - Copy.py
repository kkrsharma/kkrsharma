import random, subprocess
import os
list1= 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
list3 = '0', '0', '0', '0', '0', '0', '0'
list4 = 'F', 'F', 'F', 'F', 'F', 'F', 'F'
list5 = "cuBitCrack.exe -i addressaa.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list6 = "cuBitCrack.exe -i addressab.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list7 = "cuBitCrack.exe -i addressac.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list8 = "cuBitCrack.exe -i addressad.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list9 = "cuBitCrack.exe -i addressae.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list10 = "cuBitCrack.exe -i addressaf.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list11 = "cuBitCrack.exe -i addressag.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
list17 = "cuBitCrack.exe -i sample2.txt -o found.txt -b 40 -t 512 -p 256 --keyspace "
for y in range (10000):
        for x in range (49):
            for num in range(10):
                value1 = value = "".join(random.choices(list1, k=x+9))
                value1 = value1 + "".join(list4)
                value = value + "".join(list3)
                value3 = value + ":" + value1
                sort1 = list6 + value3
                sort2 = list7 + value3
                sort3 = list8 + value3
                sort4 = list9 + value3
                sort5 = list10 + value3
                sort6 = list11 + value3
                sort11 = list17 + value3
                value3 = list5 + value3
                print(sort11, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort11, creationflags = CREATE_NO_WINDOW)
                print(value3, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(value3, creationflags = CREATE_NO_WINDOW)
                print(sort1, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort1, creationflags = CREATE_NO_WINDOW)
                print(sort2, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort2, creationflags = CREATE_NO_WINDOW)
                print(sort3, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort3, creationflags = CREATE_NO_WINDOW)
                print(sort4, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort4, creationflags = CREATE_NO_WINDOW)
                print(sort5, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort5, creationflags = CREATE_NO_WINDOW)
                print(sort6, "satoshi namkto fena")
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call(sort6, creationflags = CREATE_NO_WINDOW)
