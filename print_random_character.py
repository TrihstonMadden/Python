from random import randint
def randlist(r):
	alpha = []
	for i in range(32,127):
		alpha.append(chr(i))
	c = alpha[r]
	return c # this is belongs to ranlist(r)

def main():
	count = 0
	while True:
		r = randint(0,96)
		print(chr(r),end="")
		if (count == 95):
			break
		count = count + 1
	print()
	
if(__name__=="__main__"):
	main()
	
