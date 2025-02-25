import random as r
from time import *

p=["hello my name is afroj and you name","python is high level interprated programming langiage"]
s=r.choice(p)
print("--------typing speed---------")

print(s)
print()
print()
time1=time()
user=input("Enter")
time2=time()
def mistake(para,ui):
    error=0
    for i in range(len(para)):
        try:
            if para[i]!=ui[i]:
                error+=1
        except:
            error+=1
    return error

def t(times,timee,userinput):
    time_delay=timee-times
    timer=round(time_delay,2)
    speed=len(userinput)/timer
    return round(speed,2)

print("Speed:",t(time1,time2,user),"w/sec")
print("Error",mistake(s,user))