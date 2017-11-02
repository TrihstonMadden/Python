from random import randint
def randlist(r,alpha,used):
	c = alpha[r]
	used[r] = 1
	#print(alpha)
	#print(used)
	return c # this is belongs to ranlist(r)

def main():
	count = 0
	used = [0] * 94
	alpha = []
	for i in range(33,127):
		alpha.append(chr(i))
	#print(alpha)
	#print(used)
	while True:
		r = randint(0,93)
		if used[r] == 0:
			c = randlist(r,alpha,used)
			count = count + 1
			print(c,end="")
			if (count == 94):
				break
	print()
	
if(__name__=="__main__"):
	main()
	
