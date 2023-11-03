import math 
import random
import functools
from time import perf_counter  #to keep an eye on time
import concurrent.futures as future   #to perform PP


r = 1
n = int(input("no of points: "))  # the int to take a only the interger values 
d = int(input("no of dimensions: ")) 



def calculatedist(coordinates):         # cal the distance form center and point 
    return math.sqrt(functools.reduce(lambda a,b: a+b, (map(lambda x: x**2 , coordinates))))

def hypersphere(n,d):
    count = 0 #no of time its insde the hyper sphere100
    for i in range(n):
        cd = []
        for j in range (d):
            cd.append(random.uniform(-r,r))  #generate points from uniform dist
        
        if calculatedist(cd)<1:
            count +=1

    calculated_vol = (count/n)*2**d
    ##print(f"calculated volume: {calculated_vol}")
    return calculated_vol

#print(f"formula value {(math.pi**(d/2))/(math.gamma(d/2 + 1))}")
#print(f"monte carlo value {calculated_vol}")

#PP
def parallelprocessing():
    p = []

    start = perf_counter()
    with future.ProcessPoolExecutor() as  ex:

        for _ in range(10):
            p.append(ex.submit(hypersphere,1000000,11))

        for i in range(10):
            p[i].result()
    # sum(p)/10 #same comput
    end = perf_counter()
    print(f"Process with multiprocessing took {round(end-start, 2)} seconds")

    start = perf_counter()
    hypersphere(10000000,11)
    end = perf_counter()
    print(f"Process took {round(end-start, 2)} seconds")

if __name__ == "__main__":
    parallelprocessing()