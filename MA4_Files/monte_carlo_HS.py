import math 
import random
import functools

r = 1
n = int(input("no of points: "))  # the int to take a only the interger values 
d = int(input("no of dimensions: ")) 

count = 0 #no of time its insde the hyper sphere

def calculatedist(coordinates):         # cal the distance form center and point 
    return math.sqrt(functools.reduce(lambda a,b: a+b, (map(lambda x: x**2 , coordinates))))

for i in range(n):
    cd = []
    for j in range (d):
        cd.append(random.uniform(-r,r))
    
    if calculatedist(cd)<1:
        count +=1

calculated_vol = (count/n)*2**d


print(f"formula value {(math.pi**(d/2))/(math.gamma(d/2 + 1))}")
print(f"monte carlo value {calculated_vol}")
