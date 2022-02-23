import random
try :
    print("Welcome to the dice guess game")
    matches = int(input("Enter the number of matches you wish to play "))
    matchnum = 1
    p_won=0
    c_won=0
    if matches>0:
        while matchnum <= matches:
            print("Match number",matchnum)
            dice1 = random.randint(1,6)
            dice2 =random.randint(1,6)
            sum=dice1+dice2
            print("Enter 1 for less than 7, 2 for 7, 3 for more than 7 and 4 to end the game abruptly")
            user_input = int(input())
            if (user_input == 1 or user_input == 2 or user_input == 3):
                print("Number on 1st dice", dice1, "Number on 2nd dice", dice2, "Sum of two dices is ",sum)
                if(user_input==1 and sum<7 or user_input==2 and sum==7 or user_input==3 and sum>7):
                    print("You guessed it right and you won the game")
                    p_won = p_won + 1
                else:
                    print("You guessed it wrong , computer won the game")
                    c_won = c_won + 1
                matchnum=matchnum+1
            elif(user_input==4):
                break
            else:
                print("User input is out of bounds please enter 1,2,3 only, current match didnt count")
        print("Number of matches won by player ", p_won," Number of matches won by computer", c_won)
        if c_won>p_won:
            print("Computer won the ",matches,"match series by ",c_won," against ",p_won)
            print("Alas! you lost the series, Better luck next time")
        elif p_won>c_won:
            print("You won the ",matches," match series by ",p_won," against ",c_won)
            print("Congratulations You won!!")
        else:
            print("The series of ", matches, " match stands tied at ",p_won,"-",c_won)
            print("You missed it by a whisker, All the best for the next time")
    else:
        print("We need to play minimum 1 match to get the result you have entered a negative value or 0 ")
except:
    print("Please enter the number of matches in integers")

