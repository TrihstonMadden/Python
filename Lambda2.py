#file 2 : Lambda2.py
def myfunc(n):
	return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
dub = mydoubler(11)

print(mydoubler(11))
print(mytripler(11))
