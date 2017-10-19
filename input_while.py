#save file as input3_while.py
print("INPUT THREE NUMBERS")
A = float(input("A:   "))
B = float(input("B:   "))
C = float(input("C:   "))
x = 2
	while True:
	y = A*x*x + B*x + C
	print (x,y)
	x = x + 1
	if(x > 5):
		break
