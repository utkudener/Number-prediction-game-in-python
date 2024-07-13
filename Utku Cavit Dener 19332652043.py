import random
import modul

print("WELCOME TO MY NUMBER GUESSİNG GAME")
print("Which number range would you like to play?\n(From 1 to ?)")
print("If you don't enter a number.Range will be 100")
rangeNumber=int(input("Enter the range:"))
print("How do you want to play?")
playerNumber=input("2 player or 3 player\n2 player for=>2\n3 player for=>3:")
if(playerNumber=="2"):
    modul.game(rangeNumber)
elif(playerNumber=="3"):
    modul.game3(rangeNumber)
        