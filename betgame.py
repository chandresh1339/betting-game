import random

bank=int(input ("Enter the amount of money you have in bank:-"))

win=0

done ='y'

while done =='y' :
	bet=int(input ("Enter the bet amount:-"))  # type: int
	if bet>bank:
		print "You don't have sufficient amount in your bank to play..Try again!!!"
		continue
	else:
		choice=int(input("Enter your choice:0 or 1?: "))
		result=random.randint(0,2)
		if choice == result:
				bank += bet
				win += bet
				print ("You won!")
                else:
				bank=bank-bet
				win=win-bet
				print ("You lost!")

	print('Bank:',bank)
	print("\n")
done = input("Play again? (y or n):")

print("Congartulations!!!You have made", win ,"rupees")
print("Your money in  your bank account",bank ,"rupees")























