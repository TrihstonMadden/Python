#hexstring.py TM

def bincon(decimal):
	print(decimal)
	print("Bin ********")
	binstr = "" # binstr is a string
	for i in range (8):
		bin = decimal % 2
		decimal = decimal // 2
		#print(bin)
		binstr = binstr + str(bin)
		#print(binstr)
	print("-----")
	print(binstr[::-1])
	
def hexcon(decimal):
	print(decimal)
	print(" HEX *******")
	# dividend/divisor=quotien
	hextr = ""
	#-----------------------------
	remainder = decimal % 16
	if (remainder == 10):
		remainder = "A"
	elif (remainder == 11):
		remainder = "B"
	elif (remainder == 12):
		remainder = "C"
	elif (remainder == 13):
		remainder = "D"	
	elif (remainder == 14):
		remainder = "E"	
	elif (remainder == 15):
		remainder = "F"	
	#-------------------------------
	quotient = decimal // 16
	if (quotient == 10):
		quotient = "A"
	if (quotient == 11):
		quotient = "B"	
	if (quotient == 12):
		quotient = "C"
	if (quotient == 13):
		quotient = "D"
	if (quotient == 14):
		quotient = "E"
	if (quotient == 15):
		quotient = "F"
	#--------------------------------
	#print(bin)
	hexstr = str(quotient)+" "+str(remainder)
	# ********************************
	print("-----")
	print(hexstr)
	
def main():
	print("INPUT -l TO EXIT THE PROGRAM")
	print("INPUT A POSITIVE INTEGER LESS THAN 256")
	done = 0
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
		hexcon(dec)
		print("done",done)
		done = dec
main()				
