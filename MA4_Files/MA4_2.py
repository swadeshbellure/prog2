#!/usr/bin/env python

from person import Person
from numba import njit
import time
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n 
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n 
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

labels = ["python", "numba", "c++"]

def create_figure(nvalues, times, figurename):
	plt.figure()
	for i in range(len(times)):
		plt.plot(nvalues, times[i], label=labels[i])
	plt.ylabel("seconds")
	plt.legend()
	plt.savefig(figurename)
	plt.close()

def main():
	first_n = range(30, 46) # find the values for n = 30, ... , 45

	py_times = []
	numba_times = []
	cpp_times = []

	for n in first_n:
		# measure python
		before = time.perf_counter()
		fib_py(n)
		after = time.perf_counter()
		py_times.append(after-before)

		# measure numba
		before = time.perf_counter()
		fib_numba(n)
		after = time.perf_counter()
		numba_times.append(after-before)

		# measure c++
		f = Person(n)
		before = time.perf_counter()
		fib_numba(n)
		f.fib()
		after = time.perf_counter()
		cpp_times.append(after-before)

	create_figure(first_n, [py_times, numba_times, cpp_times], "first.png")

	second_n = range(20, 30) # find the values for n = 20, ... , 30

	py_times = []
	numba_times = []

	for n in second_n:
		# measure python
		before = time.perf_counter()
		fib_py(n)
		after = time.perf_counter()
		py_times.append(after-before)

		# measure numba
		before = time.perf_counter()
		fib_numba(n)
		after = time.perf_counter()
		numba_times.append(after-before)

	create_figure(second_n, [py_times, numba_times], "second.png")

if __name__ == '__main__':
	main()
