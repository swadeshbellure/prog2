#!/usr/bin/env python

from person import Person
from numba import njit
import time

# def fib_py(n):
# 	if n <= 1:
# 		return n 
# 	else:
# 		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n 
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	n = 47

	before = time.perf_counter()
	print(f"fib_numba({n}) is {fib_numba(n)}")
	after = time.perf_counter()
	print(f"time take for fib_numba is {after-before}")

	f = Person(n)
	before = time.perf_counter()
	print(f"C++ fib is {f.fib()}")
	after = time.perf_counter()
	print(f"time take for C++ fib is {after-before}")

if __name__ == '__main__':
	main()
