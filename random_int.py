# save this file as random int.py
from random import randint
def randlist(r):
	alpha = ["a", "b", "c", "d", "e", 
	c = alpha[r]
	return c # this is belongs to ranlist(r)

def main():
	count = 0
	checklist = [0,0,0,0,0]
	while True:
		r = randint(0,4)
		print(checklist)
		checklist[r] = 1
		c = randlist(r)
		print(c,end="")
		if (count == 26):
			break
		count = count + 1
	print()
	
if(__name__=="__main__"):
	main()
	
