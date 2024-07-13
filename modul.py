import random

def game(rangeNumber=100,guess=0,repsCounter1=0,repsCounter2=0,winPoint1=0,winPoint2=0,againChoice1="yes",againChoice2="yes",gameCounter=0):
    while againChoice1 == "yes" and againChoice2=="yes":
        repsCounter1=0
        repsCounter2=0
        
        number=random.randint(1,rangeNumber)
        while number!=guess:
            guess=int(input("Player one enter a number:"))
            repsCounter1 += 1
            if guess == number:
                print("Hit!")
            elif guess < number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")
                
        number=random.randint(1,rangeNumber)
        while number!=guess:
            guess=int(input("Player two enter a number:"))
            repsCounter2 += 1
            if guess == number:
                print("Hit!")
            elif guess < number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")
                
        if repsCounter1<repsCounter2:
            winPoint1 += 1
            print("Player 1 ")
        elif repsCounter1>repsCounter2:
            winPoint2 += 1
            print("Player 2")
        elif repsCounter1==repsCounter2:
            print("Guys ı am sorry but no point")   
        gameCounter += 1
        againChoice1=input("Player 1 do you want play again:")
        againChoice2=input("Player 2 do you want play again:")
        if againChoice1 != "yes" or againChoice2!="yes":
            if gameCounter<=5:
                print("Player 1 - Player 2")
                print("-------------------")
                print("   ",winPoint1*5,"       ",winPoint2*5)
                if winPoint1 > winPoint2:
                    print("Player 1:Winner")
                elif winPoint2 > winPoint1:
                    print("Player 2:Winner")
                elif winPoint1==winPoint2:
                    print("There is no winner")
                    
            elif gameCounter>5 and gameCounter%2==0:
                print("You played ",gameCounter," game.You have to play last game")
                print("That game give you 15 point")
                repsCounter1=0
                repsCounter2=0
                number=random.randint(1,rangeNumber)
                while number!=guess:
                    guess=int(input("Player one enter a number:"))
                    repsCounter1 += 1
                    if guess == number:
                        print("Hit!")
                    elif guess < number:
                        print("Your guess is too low")
                    else:
                        print("Your guess is too high")
                number=random.randint(1,rangeNumber)
                while number!=guess:
                    guess=int(input("Player two enter a number:"))
                    repsCounter2 += 1
                    if guess == number:
                        print("Hit!")
                    elif guess < number:
                        print("Your guess is too low")
                    else:
                        print("Your guess is too high")
                gameCounter+=1
                if repsCounter1<repsCounter2:
                    float(winPoint1)
                    winPoint1 += 1.5
                    print("Player 1 ")
                elif repsCounter1>repsCounter2:
                    float(winPoint2)
                    winPoint2 += 1.5
                    print("Player 2")
                elif repsCounter1==repsCounter2:
                    print("Guys ı am sorry but no point")  
                
                print("Player 1 - Player 2")
                print("-------------------")
                print("   ",winPoint1*10,"       ",winPoint2*10)
                if winPoint1 > winPoint2:
                    print("Player 1:Winner")
                elif winPoint2 > winPoint1:
                    print("Player 2:Winner") 
                elif winPoint1==winPoint2:
                    print("There is no winner")
                
            elif gameCounter>5 and gameCounter%2==1:
                print("Player 1 - Player 2")
                print("-------------------")
                print("   ",winPoint1*10,"       ",winPoint2*10)
                if winPoint1 > winPoint2:
                    print("Player 1:Winner")
                elif winPoint2 > winPoint1:
                    print("Player 2:Winner") 
                elif winPoint1==winPoint2:
                    print("There is no winner")
                    
def game3(rangeNumber=100,guess=0,repsCounter1=0,repsCounter2=0,repsCounter3=0,winPoint1=0,winPoint2=0,winPoint3=0,againChoice1="yes",againChoice2="yes",againChoice3="yes"):
    while againChoice1 == "yes" and againChoice2=="yes" and againChoice3=="yes":
        repsCounter1=0
        repsCounter2=0
        repsCounter3=0
        number=random.randint(1,rangeNumber)
        while number!=guess:
            guess=int(input("Player one enter a number:"))
            repsCounter1 += 1
            if guess == number:
                print("Hit!")
            elif guess < number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")
                
        number=random.randint(1,rangeNumber)
        while number!=guess:
            guess=int(input("Player two enter a number:"))
            repsCounter2 += 1
            if guess == number:
                print("Hit!")
            elif guess < number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")
                
        number=random.randint(1,rangeNumber)
        while number!=guess:
            guess=int(input("Player three enter a number:"))
            repsCounter3 += 1
            if guess == number:
                print("Hit!")
            elif guess < number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")
                
        if repsCounter1<repsCounter2 and repsCounter1<repsCounter3:
            winPoint1 += 1
            print("Player 1 ")
        elif repsCounter2<repsCounter1 and repsCounter2<repsCounter3:
            winPoint2 += 1
            print("Player 2")
        elif repsCounter3<repsCounter1 and repsCounter3<repsCounter2:
            winPoint3 += 1
            print("Player 3")  
        elif repsCounter1==repsCounter2 and repsCounter2<repsCounter3:
            winPoint1 += 1
            winPoint2 += 1
            print("Player 1 and Player 2")
        elif repsCounter1==repsCounter3 and repsCounter1<repsCounter2:
            winPoint1 += 1
            winPoint3 += 1
            print("Player 1 and Player 3")
        elif repsCounter2==repsCounter3 and repsCounter2<repsCounter1:
            winPoint2 += 1
            winPoint3 += 1
            print("Player 2 and Player 3")
        elif repsCounter1==repsCounter2 and repsCounter1==repsCounter3:
            print("Guys ı am sorry but no point")   
            
        againChoice1=input("Player 1 do you want play again:")
        againChoice2=input("Player 2 do you want play again:")
        againChoice3=input("Player 3 do you want play again:")
        
        if againChoice1 != "yes" or againChoice2!="yes" or againChoice3!="yes":
            print("Player 1 - Player 2 - Player 3")
            print("------------------------------")
            print("   ",winPoint1*5,"       ",winPoint2*5,"       ",winPoint3*5)
            if winPoint1 > winPoint2 and winPoint1>winPoint3:
                print("Player 1:Winner")
            elif winPoint2 > winPoint1 and winPoint2>winPoint3:
                print("Player 2:Winner")
            elif winPoint3 > winPoint1 and winPoint3 > winPoint2:
                print("Player 3:Winner")
            elif winPoint1==winPoint2 and winPoint1>winPoint3:
                print("Player 1 and Player 2:Winner")
            elif winPoint1==winPoint3 and winPoint1>winPoint2:
                print("Player 1 and Player 2:Winner")
            elif winPoint2==winPoint3 and winPoint2>winPoint1:
                print("Player 1 and Player 2:Winner")
            elif winPoint1==winPoint2 and winPoint1==winPoint3:
                print("There is no winner")
                
            
            
            



    