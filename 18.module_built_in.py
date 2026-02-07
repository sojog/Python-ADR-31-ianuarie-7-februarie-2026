# Module Built - in (vin instalate cu Python)
import math # Folosit pentru matematica

print(math.pi)
print(math.sqrt(49))
print(math.pow(6, 3))

## Modulul random
import random

print("Un numar random intre 0 si 1 : ",  random.random())
print("Un numar random intre 2 intre : ",  random.randint(10, 100))
print("Alege dintr-o colectie ",  random.choice(["alb", "verde", "albastru", "gri"]))


## Modulul time
import time

print("Timestamp:", time.time()) # Numarul de secunde scurse de la 1 ianuarie 1970
time.sleep(2) # blockcheaza executia pentru un numar de secunde
print("Timestamp:", time.time()) # Numarul de secunde scurse de la 1 ianuarie 1970


import datetime


print("Acum:", datetime.datetime.now()) # 
print("O data oarecare:", datetime.datetime(2027, 3,29))
print("Diferenta: ", datetime.datetime(2027, 3,29) - datetime.datetime.now())