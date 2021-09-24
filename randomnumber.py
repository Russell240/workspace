import random 
generatedNumber = random.randrange(1,20,8) 
userGuess = int(input("Enter your Choice between 1 to 20: ")) 
if generatedNumber == userGuess: 
 print("You have got it right") 
elif userGuess<generatedNumber: 
 diff1= generatedNumber-userGuess
 print("Your guess is too low your guess was",str(diff1),
 'lower than random number the random number was', str(generatedNumber) ) 
else: 
 diff2=userGuess-generatedNumber   
 print("Your guess is too high your was ", str(diff2),
 'higher than random number the random number was', str(generatedNumber)) 
