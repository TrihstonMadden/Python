#First attempt at python ADG - A Dice Game

# Create dice roll function
import random
	
def diceroll():
		random.seed()
		global d1, d2, sum
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		sum = (d1 + d2)
# read in amt of money
		global cash, bet
		cash = 1000
		print ('You have ', cash, 'dollars!')
		bet = input("How much to bet: $")
		bet = int(bet)
		
if(__name__ == '__main__'):
# roll the dice
	diceroll()
# display diceroll
	print('dice d1 = ', d1, 'dice d2 = ', d2, 'sum is ', sum)
#first make a bet on the front line(pass or don't pass)

#if roll is 7 or 11 you Win!
	if (sum ==7 or sum ==11):
		cash = cash + bet
		print('You WIN and now have ', cash, ' dollars.')
#if roll is 2,3 or 12 you Lose!
	elif(sum ==2 or sum ==3 or sum ==12):
		cash = cash - bet
		print('You LOSE and now have ', cash, ' dollars.')
# any other roll (4,5,6,8,9,10) becomes the point
	else:
		print('Your POINT is ', sum, ' You must now roll ', sum, ' Before you roll a 7 ')
		print('in order to add to your $', cash, ' cash.')
	
# roll again
	input("Do You want to keep playing?\n")
   yes=("y","Y","yes","Yes")
   if answer in yes:
  
# Now point must be rolled before a 7 for pass line to win
	if ( sum >=7):
		cash = cash + bet
		print('You WIN and now have ', cash, ' dollars.')
# Now point must be rolled before a 7 for pass line to win
	if ( sum <=7):
		cash = cash - bet
		print('You LOSE and now have ', cash, ' dollars.')

# If 7 is rolled before point ... pass line loses







