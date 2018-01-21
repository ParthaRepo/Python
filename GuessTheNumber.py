import random

#Generate the random number
randomNumber = random.randint(0,10)
#print(randomNumber)
for i in range(5):
    print("Guess the Number :")
    enteredNumber = int(input())
    if enteredNumber<randomNumber:
        print("Guessed number is low")
    elif enteredNumber>randomNumber:
        print("Guessed number is high")
    else:
        break
if enteredNumber == randomNumber:
    print("Great, you have guessed it right!!!")
else:
    print("Random number is :", randomNumber)
    print("Exceeds the number of attempts, Better luck next time !!!")
