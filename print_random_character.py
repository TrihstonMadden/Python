from random import randint
def randlist(r):
	alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
			,"/", "!", "@", "$"]
	c = alpha[r]
	return c # this is belongs to ranlist(r)

def main():
	count = 0
	checklist = [0]*30
	while True:
		r = randint(0,29)
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
	
