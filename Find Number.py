import random

rank=1       #This variable determine to who will play.
playerScore1=0
playerScore2=0
gameNumber=0
Flag=False   #İf the flag is True game over.
lowerBase=0  #If the user does not want to change the range , it is played between 0-100 by default.
upperBase=100

def giveName():
#this function allows players to name themselves
    print("Let's name the players")    
    global name1
    global name2
    name1=input("Enter the name of player 1--> ")
    name2=input("Enter the name of player 2--> ")

def changePlayer(rank):
#this function is allows change the player.
#In addition, when each player turns to 1, the number of games increases by 1, so we find out how many games were played.
    global gameNumber
    if rank==1:        
        gameNumber+=1
        return 2
    if rank==2:
        return 1
  
def rangeChooser():
 #This function ask the user what numbers they want to play between.
 #This function is optional .
    print("Between which numbers do you want to play ?")
    global lowerBase
    global upperBase
    lowerBase = int(input("Enter the lower limit of the game range: "))  
    upperBase = int(input("Enter the upper limit of the game range: "))  
    if lowerBase>upperBase:   #If the user enters the lower value more than the upper value, it will automatically replace the values ​​(To prevent error)
        temp=lowerBase
        lowerBase=upperBase
        upperBase=temp
    
    return lowerBase,upperBase

def wantToContinue():
#This function checks whether the game will continue or not.
#if the first user wants to leave the game, the second player also plays, then the game is over.
#If the second user wants to leave the game, the game will be terminated directly.
    global Flag   
    status=input("if you want to quit game press 0--> ")
    if status=="0":
        Flag=True
        
def game(lowerBase,upperBase):
#This function enables the game to be played.
    x = int(random.randint(lowerBase,upperBase))   
    #print(x)   #Prints the result that the computer keeps in memory (Turn it off during gameplay)
    global count
    count=0     #Memorizes how many times the user guessed
    while True:                
        count += 1             
        guess = int(input("{}. Make the guess: ".format(count)))      
        #Evaluates the user's guess hıgh or low.
        if x == guess:     
            print("congratulations you guessed it in" ,count," times")   
            return count   #Returns the number of attempts the user found the correct result        
            break            
        elif x > guess:
            print("please enter a hıgher number!")
        elif x < guess:
            print("please enter a lower number!")
    
def determineTheWinner(predictCounter1, predictCounter2,gameNumber):   
#This function allows us to rate players
#If less than 5 game are played, the games will be worth 5 points.
#10 points per game if 5 or more games are played     
    print("**********")
    if gameNumber<=6:
        if predictCounter1<predictCounter2: 
            print("This round {} is win".format(name1))
            global playerScore1
            playerScore1=playerScore1+5
        elif predictCounter2<predictCounter1:
            print("This round {} is win".format(name2))
            global playerScore2
            playerScore2=playerScore2+5
    if gameNumber ==6:     #If the number of matches played is more than 5, 10 points are awarded per game.
        playerScore1*=2
        playerScore2*=2
    if gameNumber >6:
        if predictCounter1<predictCounter2:
            playerScore1= playerScore1+10
            print("{} is win".format(name1))
        elif predictCounter2<predictCounter1:
            playerScore2=playerScore2+10
            print("{} is win".format(name1))
    if predictCounter1==predictCounter2:
        print("This round is a draw")
            
def final():
#This function asks the player if they want a final match, and according to the decision, a 15-point final match is played..    
    situation=input("You have a chance "
                    "If you want to play the final match press 1\n"
                    "all other number entries will cause the final not to be played\n")
    if situation=="1":                    
        print("The final match is 15 points")
        print("****")
        print("\n{}'s turn".format(name1))
        predictCounter1=game(lowerBase,upperBase) 
        print("\n{}'s turn".format(name2))
        predictCounter2=game(lowerBase,upperBase)                    
        if predictCounter1<predictCounter2:
            global  playerScore1
            playerScore1 = playerScore1+15
        elif predictCounter2<predictCounter1:
            global playerScore2
            playerScore2=playerScore2+15
        elif predictCounter1==predictCounter2:
            print("Final round is Draw")
    else:
        print("You did not want to play the final match, the game ends")
        
def printResult( playerScore1,playerScore2,gameNumber):
#This Function after the game is completely completed, it prints the result on the screen
    print("\n\n++++++ SCOR TABLE ++++++\n")
    if  playerScore1>playerScore2:
        print("{} Won".format(name1))
    elif playerScore2>playerScore1:
        print("{} Won".format(name2))
        
    print("\n{}'s Score {}".format(name1,playerScore1))
    print("{}'s Score {}".format(name2,playerScore2))
    print("number of games played = {}".format(gameNumber))

def saveTheFile(playerScore1,playerScore2,gameNumber):
#With this function, the end game screen is saved in a file.
#Ekleme modunu kullanıyorum çünkü eski kaydı silmek istemedim
    F=open("Score Table.txt", "a")
    F.write("++++++ SCOR TABLE ++++++\n")
    if  playerScore1>playerScore2:
        F.write("{} Won\n".format(name1))
    elif playerScore2>playerScore1:
        F.write("{} Won\n".format(name2))
    elif playerScore2==playerScore1:
        F.write("Game is draw")
        
    F.write("\n{}'s Score {}\n".format(name1,playerScore1))
    F.write("{}'s Score {}\n".format(name2,playerScore2))
    F.write("number of games played = {}\n\n".format(gameNumber))
    F.close()

print("\n**WELCOME TO GUESS THE NUMBER GAME**")

i=input("if you want to select game interval press 1\n"
            "if you choose different number you will play between 0-100\n")
if i=="1":
#If the user wants to select the interval to play, the  rangechooser() function is called and the interval the user wants to play is retrieved
    a=rangeChooser()  
    lowerBase=a[0]
    upperBase=a[1]
else:
    print("The number you are trying to guess will be between 0 and 100")

giveName()   

while True:
#this loop allows the game to be played until one of the Players wants to quit.
#İf someone want to quit Flag is True end the game is over.    
    count=0        
    print("")  #I used it to avoid confusion on the screen
    if rank==1:                                
        print("\n{}'Turn".format(name1))
        predictCounter1=game(lowerBase,upperBase)
        wantToContinue()               
    elif rank==2:
        print("\n{}'s Turn".format(name2))
        predictCounter2=game(lowerBase,upperBase)
        determineTheWinner(predictCounter1, predictCounter2,gameNumber) 
        print(gameNumber," Rounds completed so far") #Displays the current game number in each game  it is optional
        print("**********")
        wantToContinue()          
        if Flag==True:  #I provided the exit here to ensure that the second user is given another chance even if the first user wants to exit.
            break
        print("**********")
    rank=changePlayer(rank)    #It is ensured that the player changes in each round.
    
       
#When the number of matches is more than 5 and they are even, it questions whether to play a final match..
if ((gameNumber>5) and (gameNumber % 2==0)):
    print("**********")
    print("THE SCORE TABLE BEFORE THE FINAL MATCH")
    printResult( playerScore1,playerScore2,gameNumber)
    print("**********")
    final()
    
# After the game is completely over, it prints the final score status and the number of games played on the screen.         
printResult(playerScore1,playerScore2,gameNumber)
saveTheFile(playerScore1,playerScore2,gameNumber)