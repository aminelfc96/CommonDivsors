# from random import randrange
from threading import Thread
from time import time

start = time()

class Divisor:
	def CommonDivisor(n,d):
		numerator_div = []
		denominator_div = []
		def first():
			for i in range(1,n+1):
				if n % i == 0:
					numerator_div.append(i)
		def second():
			for i in range(1,d+1):
				if d % i == 0:
					denominator_div.append(i)
		t1 = Thread(target=first)
		t2 = Thread(target=second)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		common_divisors = set(numerator_div).intersection(set(denominator_div))
		return common_divisors
	def pgcd(n,d):
		r = None
		while r != 0:
			r = n % d
			n = d 
			d = r
		return n

# r1,r2 = randrange(99999999),randrange(9999999)
# print(r1,r2)
# x = Divisor.CommonDivisor(r1,r2)
# print(x)
print(f"time {time()-start}")
