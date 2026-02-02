# Corridor #################################


intro = "Welcome to Corridor, the alien tentacles are growing! Stop them with missiles and tanks!\n"


"""
OUTLINE OF STRUCTURE (FUNCTION VIEW)


vars declared, intro
intro 5 pre-turns to start growth

showBoard
    processInteractions
	    check for player losing people after bot touches row 10

	MISSILES

        clear the corridor if a missile destroyed (big hit) it
        clear the corridor of the x if a missile missed

        missileClearCorridorSingleHit
        missilesLaunching
        missiles moving forward from invisible to visible 10s in corridors

	TANKS

        tanks moving forward in each corridor
        tanks clearing each corridor

        clearCorridor (for tanks only)
        clearTheCorridorTank 
            changeCorridorBoolValue
        tankMovingForward

playerMove 
	get input
	drop weapons onto board

botMove (random growth)

"""


# ascii art 
asciiImage1 = (r""" 
             .                     .                                       
             +:                   :=                              :::.     
             :%                  .*                       :=+=:.    :#=.   
            :%=                  -+                      **=  .+=     #*   
         =#%*:                   =*                     =*=     .:    -%=  
      :#%#-.       :=***+=-.     :#=         .:==-:     **-    :.     :%*  
     =##-        =*=::::-=**=-.   -#+.     -+*******=- .##-    =:     =@*  
    -*#:        =+.        :=*+=.  :**=.  =*++=:::-=***+*%.   .*.    =%%-  
    =#*:       .*            :*+*.   +**..#=+-       -###*:..:#=   :*%%=   
    .*%*+:.    :=             :***    *#*.%==-      .*@#***##*:..-*%@%:    
      -%%#*+:.             ..::++%=..=%%+ +#=+=   .+%#%*   ..=*%%%%%:      
       .:*%%#*+:         =#%%%%%%#***%%*. .#*=*=+#*%##: .-*#%%%%%=:.       
     .::: .:#%%*+-     :##***==**%*==-:    :%*=**##=: :+*%%%%+:. .::       
  :*#%%%%%#= :%%#*=   .%#**=.:##%%.     :+*%@%*++-. .=+*%%*-.:+**##%%%*:   
 =%##*=+#*#%*..#@#*-  -%*++.=##%%:    =*#***#%*=*:  =+*%%= .+%****#**#%%*. 
:%%#-.-::*##%* .%%**. :%#+++**%#:   .*%****-=%*=*: -***%:  *%*+*=:. .-*%%*.
=%%*.*-*#:###%: =@#*=  =%*+**%+.    ##*#*: .#%*++. ***%=  =%***: :===.:*@%=
:%%#:= =*=+*#%+ -%#*=  :#%#=*=:    -%**+   =%*+*: :**%%:  %#*#- -%+ :+ *@%=
 *%%=..*#:=*#%+ =%#*= -#%%@%**++:  =%=#-   #%*=+  :+*%%: .%***: *%= :::%@#:
  =%%%%%=.*##@- #%**::*#%%-.+#***- -%+*+   %%*+-  :**%%- .%***. :@#*+#%%%- 
   .:::. -**%% :@%*+.=*#%+   -#+**. %+**-  #@#*=  .**#%+  %*#*:  :=*##*-.  
        .**#@:.%%**: =*#%=    *+**- -****: =@%**:  =**%%. #*#+=            
""")

asciiImage2 = (r"""
%%%%%###########*********+++++++++++++++++============++++++++++++*********
%%%##########********++++++++++++*@@%+======================+++++++++******
%%#########*********++++++++====+@@%*======-------------=========++++++****
%########*******++++++++=======+%%#+===---------------------======+++++++**
#######******++++++++=========-*%%#=+%@@@%#+--::::::::::::-----*@@@*=++++++
######*****++++++=========-----*##*-#@@@@@@@*:::::::::::-+**=---#%@*===++++
#####****++#%%*+======--------:*###:*%@@@%@*#:::.....-*@@@@@@#--*%%#====+++
####****+++%@@+=*@@@%+-------::=**#%%@@@@%#:+*-......-+@@@@@#-::+@#%======+
###****+++#%%==+*@@@@@%+--::::::-=###@####*=-=-.......-#@@@@%+=+%%#%=-=====
##****++++#%#=++#@@@@@=::::::=::::***%#####@@#-.......=*#*##%@%%###+----===
##****+++++###%#@%@@%+:::::::#=::::-#@%@@@***#*:....:#%###%@%###+=::----===
##****+++===*#@%%#***#%@=::::*%#::-*%%%*#*%%**%#....**#%##%%%%#=:::::----==
##*****+*%#**#%%%%@@##%%%#=-*%#=*--%%%#%##*#+-*#-...++-*%#**#%#@-::::-----=
###****+++*##@%@%%%%+%#-:=#%%#-::-+=#%%####=--*%#=.=#+:*###*%%##:::::-----=
#####****+++++%@%%%##=*=:::=-::::=%#%%##**%#*:.*%#:*@+:-*####%%=*-:::----==
%#####*****+*%#@%%%#*-*+:::::::::+*%%%%**%%##++:+%+*%:.:#%%#*#%%==-::----==
%%%#####***##+%@%%%#*=%+------::::#%%%###%%%#+::=%++%+::##@@@##%#=::----===
%%%%%######%*#%%#%%%#*#%=--------+%%%%+::##%%#=::-::-:::*#%%#*%%%%----====+
%%%%%%%%######%%#%%@%#===========%%%%#:::+%%%%#----:::::*#%%-#%%%@=-====+++
%#*****##%###%@%#=#%%#+++*****++*%%%%#---+#%%%#===----::*%%%#+%%%%*==+++++*
%%%%%%#%#*##%%%%#*%%%#*########*#%%%%+==++*%%%%=++====--+###*=#%%%#++******
%%%%%%%%%%%%@%%%**###*++#+=--=*##%%%#*#%#*+###*****++++++###*+*#%%#########
@@@%@@@@@%%%%%%#*####+#*+=**#####%%#=####*+*##*=++++=+++**##*=-#####%%%%%%%
@@%%%%%%%%%%%%%*%##***%%%%%%%%%####***%#%##+***%%##%%%%%#+#%*#+**#*%%%%%%%@
@@@@@@@@@@@%%%#*%%%#+*%%%%%%%%%%###+%%%%%%%++*+%%%%%@%%%%+*%#%%*###%%@@@@@%
@@@@@@@@@@@@%%#%@%%**%@%%%%%%%%%@@%*%%%%*%%*#@+*#%***%@%++#%###=#%%%@%%%%@@
%@@@%%%%%%#%@#+###%%*#%%%#=-#%%#@#**##%%#%%####+:-%%#**-::-*#+-:+#%*:-=+++-
*+++++*#%%%%%#*+===--::::::::::%@@#-::::::::+%@@+:::::::::+%%%*=-=%%%%#+---
""")



# corridor wall
x = "|"
border = "-"*50

# vars      
# unused characters: § ¥ * ≋    https://tools.w3cub.com/html-entities


a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = a11 = " "
b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b10 = b11 = " "
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = " "
d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = d9 = d10 = d11 = " "
e1 = e2 = e3 = e4 = e5 = e6 = e7 = e8 = e9 = e10 = e11 = " "

peopleA = peopleB = peopleC = peopleD = peopleE = "♀"

clearA = clearB = clearC = clearD = clearE = False



#turn iterator
i = 0

# amount of tanks left counter
tC = 3

# amount of missiles left counter
mC = 12

    # turn missiles int into visual icons
    # mC = 10 
    #missilesShown = mC * "↟" 



incomingMessage = "Sir, what are your orders?"


def showBoard():
 
    global i,tC,mC,incomingMessage
    
    #process interactions 
    processInteractions()
    
    # round counter
    i = i + 1


    # colonies left counter
    cLc = 5
    if peopleA == "x":
        cLc = cLc - 1
    if peopleB == "x":
        cLc = cLc - 1
    if peopleC == "x":
        cLc = cLc - 1
    if peopleD == "x":
        cLc = cLc - 1
    if peopleE == "x":
        cLc = cLc - 1
    else:
        pass


    # turn tanks int into visual icons
    if tC == 3:
        tanksShown = "≙ ≙ ≙"
    elif tC == 2:
        tanksShown = "≙ ≙"
    elif tC == 1:
        tanksShown = "≙"
    elif tC == 0:
        tanksShown = "0"
    else:
        #print(":: ERROR 98")
        pass



    # trying to get beter vertical spacing during gameplay
    print("\n" * 1)






    # check if game is over and end it if so
    if i > 10:
        if peopleA == peopleB == peopleC == peopleD == peopleE == "x":
            incomingMessage = ("The last of the fighters have fallen, and the aliens have won!")
            
        elif a1 == b1 == c1 == d1 == e1 == " ":
            incomingMessage = ("The aliens have been exterminated, long live the fighters!")
            
    else:
        pass


    print("\n\n",

    border,"\n",
    "     "+"A B C D E"+"\n\n",

    "    "+x+a1+x+b1+x+c1+x+d1+x+e1+x+"\n",
    "    "+x+a2+x+b2+x+c2+x+d2+x+e2+x+"\n",
    "    "+x+a3+x+b3+x+c3+x+d3+x+e3+x+"\n",
    "    "+x+a4+x+b4+x+c4+x+d4+x+e4+x+"\n",
    "    "+x+a5+x+b5+x+c5+x+d5+x+e5+x+"\n",
    "    "+x+a6+x+b6+x+c6+x+d6+x+e6+x+"\n",
    "    "+x+a7+x+b7+x+c7+x+d7+x+e7+x+"\n",
    "    "+x+a8+x+b8+x+c8+x+d8+x+e8+x+"\n",
    "    "+x+a9+x+b9+x+c9+x+d9+x+e9+x+"\n",
    "    "+x+a10+x+b10+x+c10+x+d10+x+e10+x+"\n",

    "     "+peopleA,peopleB,peopleC,peopleD,peopleE,"\n","\n",
    
    f"Round {i}","\n",
    "Missiles ↟",mC,"\n",    
    "Tanks",tanksShown,"\n", 
    f"Colonies {cLc}","\n","\n",
    "Incoming Message:",incomingMessage,"\n",

    
    border

    )


    clearA = clearB = clearC = clearD = clearE = False


    # check if game is over and end it if so
    if i > 10:
        if peopleA == peopleB == peopleC == peopleD == peopleE == "x":
            print(asciiImage1) # loss image

            # Pause execution for 30 seconds
            import time
            print("...program will exit in 30 secs...") 
            time.sleep(30) 

            exit()
        elif a1 == b1 == c1 == d1 == e1 == " ":            
            print(asciiImage2) # victory image

            # Pause execution for 30 seconds
            import time
            print("...program will exit in 30 secs...") 
            time.sleep(30) 

            exit()

            
    else:
        pass
        
        
    # important loop structure func here
    playerMove()





# bot move input
def botMove():
    
    #bot grows randomly

    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    global i    
    import random    

    
    #print(":: botmove has begun!")

    #botTurnPossibleIndexes = ["a1","b1","c1","d1","e1"]
    botTurnPossibleGrowth = ["ζ","ζ"," "," "," "," "]

    #botChoice = random.choice(botTurnPossibleIndexes)


    if a1 == a2 == a3 == a4 == a5 == a6 == a7 == a8 == a9 == "ζ" and a10 == " ":
        a10 = random.choice(botTurnPossibleGrowth)
        #print(":: a10 rando triggered!")
    if b1 == b2 == b3 == b4 == b5 == b6 == b7 == b8 == b9 == "ζ" and b10 == " ":
        b10 = random.choice(botTurnPossibleGrowth)
        #print(":: b10 rando triggered!") 
    if c1 == c2 == c3 == c4 == c5 == c6 == c7 == c8 == c9 == "ζ" and c10 == " ":
        c10 = random.choice(botTurnPossibleGrowth)
        #print(":: c10 rando triggered!") 
    if d1 == d2 == d3 == d4 == d5 == d6 == d7 == d8 == d9 == "ζ" and d10 == " ":
        d10 = random.choice(botTurnPossibleGrowth) 
        #print(":: d10 rando triggered!")
    if e1 == e2 == e3 == e4 == e5 == e6 == e7 == e8 == e9 == "ζ" and e10 == " ":
        e10 = random.choice(botTurnPossibleGrowth)
        #print(":: e10 rando triggered!")

    if a1 == a2 == a3 == a4 == a5 == a6 == a7 == a8 == "ζ" and a9 == " ":
        a9 = random.choice(botTurnPossibleGrowth)
        #print(":: a9 rando triggered!")
    if b1 == b2 == b3 == b4 == b5 == b6 == b7 == b8 == "ζ" and b9 == " ":
        b9 = random.choice(botTurnPossibleGrowth)
        #print(":: b9 rando triggered!") 
    if c1 == c2 == c3 == c4 == c5 == c6 == c7 == c8 == "ζ" and c9 == " ":
        c9 = random.choice(botTurnPossibleGrowth)
        #print(":: c9 rando triggered!") 
    if d1 == d2 == d3 == d4 == d5 == d6 == d7 == d8 == "ζ" and d9 == " ":
        d9 = random.choice(botTurnPossibleGrowth) 
        #print(":: d9 rando triggered!")
    if e1 == e2 == e3 == e4 == e5 == e6 == e7 == e8 == "ζ" and e9 == " ":
        e9 = random.choice(botTurnPossibleGrowth)
        #print(":: e9 rando triggered!")

    if a1 == a2 == a3 == a4 == a5 == a6 == a7 == "ζ" and a8 == " ":
        a8 = random.choice(botTurnPossibleGrowth)
        #print(":: a8 rando triggered!")
    if b1 == b2 == b3 == b4 == b5 == b6 == b7 == "ζ" and b8 == " ":
        b8 = random.choice(botTurnPossibleGrowth)
        #print(":: b8 rando triggered!") 
    if c1 == c2 == c3 == c4 == c5 == c6 == c7 == "ζ" and c8 == " ":
        c8 = random.choice(botTurnPossibleGrowth)
        #print(":: c8 rando triggered!") 
    if d1 == d2 == d3 == d4 == d5 == d6 == d7 == "ζ" and d8 == " ":
        d8 = random.choice(botTurnPossibleGrowth) 
        #print(":: d8 rando triggered!")
    if e1 == e2 == e3 == e4 == e5 == e6 == e7 == "ζ" and e8 == " ":
        e8 = random.choice(botTurnPossibleGrowth)
        #print(":: e8 rando triggered!")

    if a1 == a2 == a3 == a4 == a5 == a6 == "ζ" and a7 == " ":
        a7 = random.choice(botTurnPossibleGrowth)
        #print(":: a7 rando triggered!")
    if b1 == b2 == b3 == b4 == b5 == b6 == "ζ" and b7 == " ":
        b7 = random.choice(botTurnPossibleGrowth)
        #print(":: b7 rando triggered!") 
    if c1 == c2 == c3 == c4 == c5 == c6 == "ζ" and c7 == " ":
        c7 = random.choice(botTurnPossibleGrowth)
        #print(":: c7 rando triggered!") 
    if d1 == d2 == d3 == d4 == d5 == d6 == "ζ" and d7 == " ":
        d7 = random.choice(botTurnPossibleGrowth) 
        #print(":: d7 rando triggered!")
    if e1 == e2 == e3 == e4 == e5 == e6 == "ζ" and e7 == " ":
        e7 = random.choice(botTurnPossibleGrowth)
        #print(":: e7 rando triggered!")

    if a1 == a2 == a3 == a4 == a5 == "ζ" and a6 == " ":
        a6 = random.choice(botTurnPossibleGrowth)
        #print(":: a6 rando triggered!")
    if b1 == b2 == b3 == b4 == b5 == "ζ" and b6 == " ":
        b6 = random.choice(botTurnPossibleGrowth)
        #print(":: b6 rando triggered!") 
    if c1 == c2 == c3 == c4 == c5 == "ζ" and c6 == " ":
        c6 = random.choice(botTurnPossibleGrowth)
        #print(":: c6 rando triggered!") 
    if d1 == d2 == d3 == d4 == d5 == "ζ" and d6 == " ":
        d6 = random.choice(botTurnPossibleGrowth) 
        #print(":: d6 rando triggered!")
    if e1 == e2 == e3 == e4 == e5 == "ζ" and e6 == " ":
        e6 = random.choice(botTurnPossibleGrowth)
        #print(":: e6 rando triggered!")

    if a1 == a2 == a3 == a4 == "ζ" and a5 == " ":
        a5 = random.choice(botTurnPossibleGrowth)
        #print(":: a5 rando triggered!")
    if b1 == b2 == b3 == b4 == "ζ" and b5 == " ":
        b5 = random.choice(botTurnPossibleGrowth)
        #print(":: b5 rando triggered!") 
    if c1 == c2 == c3 == c4 == "ζ" and c5 == " ":
        c5 = random.choice(botTurnPossibleGrowth)
        #print(":: c5 rando triggered!") 
    if d1 == d2 == d3 == d4 == "ζ" and d5 == " ":
        d5 = random.choice(botTurnPossibleGrowth) 
        #print(":: d5 rando triggered!")
    if e1 == e2 == e3 == e4 == "ζ" and e5 == " ":
        e5 = random.choice(botTurnPossibleGrowth)
        #print(":: e5 rando triggered!")

    if a1 == a2 == a3 == "ζ" and a4 == " ":
        a4 = random.choice(botTurnPossibleGrowth)
        #print(":: a4 rando triggered!")
    if b1 == b2 == b3 == "ζ" and b4 == " ":
        b4 = random.choice(botTurnPossibleGrowth)
        #print(":: b4 rando triggered!") 
    if c1 == c2 == c3 == "ζ" and c4 == " ":
        c4 = random.choice(botTurnPossibleGrowth)
        #print(":: c4 rando triggered!") 
    if d1 == d2 == d3 == "ζ" and d4 == " ":
        d4 = random.choice(botTurnPossibleGrowth) 
        #print(":: d4 rando triggered!")
    if e1 == e2 == e3 == "ζ" and e4 == " ":
        e4 = random.choice(botTurnPossibleGrowth)
        #print(":: e4 rando triggered!")
        
    if a1 == a2 == "ζ" and a3 == " ":
        a3 = random.choice(botTurnPossibleGrowth)
        #print(":: a3 rando triggered!")
    if b1 == b2 == "ζ" and b3 == " ":
        b3 = random.choice(botTurnPossibleGrowth) 
        #print(":: b3 rando triggered!")
    if c1 == c2 == "ζ" and c3 == " ":
        c3 = random.choice(botTurnPossibleGrowth) 
        #print(":: c3 rando triggered!")
    if d1 == d2 == "ζ" and d3 == " ":
        d3 = random.choice(botTurnPossibleGrowth) 
        #print(":: d3 rando triggered!")
    if e1 == e2 == "ζ" and e3 == " ":
        e3 = random.choice(botTurnPossibleGrowth)
        #print(":: e3 rando triggered!")
        
    if a1 == "ζ" and a2 == " ":
        a2 = random.choice(botTurnPossibleGrowth)
        #print(":: a2 rando triggered!")
    if b1 == "ζ" and b2 == " ":
        b2 = random.choice(botTurnPossibleGrowth)
        #print(":: b2 rando triggered!") 
    if c1 == "ζ" and c2 == " ":
        c2 = random.choice(botTurnPossibleGrowth) 
        #print(":: c2 rando triggered!")
    if d1 == "ζ" and d2 == " ":
        d2 = random.choice(botTurnPossibleGrowth)
        #print(":: d2 rando triggered!") 
    if e1 == "ζ" and e2 == " ":
        e2 = random.choice(botTurnPossibleGrowth)
        #print(":: e2 rando triggered!")

    # the tentacles stop growing back after a while (20 rounds)
    if a1 == " " and i < 20 and peopleA != "x":        
        a1 = random.choice(botTurnPossibleGrowth)
        #print(":: a1 rando triggered!")
    if b1 == " " and i < 20 and peopleB != "x": 
        b1 = random.choice(botTurnPossibleGrowth)
        #print(":: b1 rando triggered!")
    if c1 == " " and i < 20 and peopleC != "x": 
        c1 = random.choice(botTurnPossibleGrowth)
        #print(":: c1 rando triggered!")
    if d1 == " " and i < 20 and peopleD != "x": 
        d1 = random.choice(botTurnPossibleGrowth)
        #print(":: d1 rando triggered!")
    if e1 == " " and i < 20 and peopleE != "x": 
        e1 = random.choice(botTurnPossibleGrowth)
        #print(":: e1 rando triggered!")

    
    else:
        #print(":: ERROR 317 random growth else triggered")
        pass


    #print("\n:: growth this turn:",x+a1+x+b1+x+c1+x+d1+x+e1+x)
    #print(":: botChoice is:"+botChoice)
    #print(":: botGrowth is:"+botGrowth)
    if i > 1:
        #print("The creature has grown!")
        pass
    else:
        pass

    


# player move input
def playerMove():

    global playerMoveInput1,playerMoveInput2
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    global i,incomingMessage,tC,mC    
    



    #reset these vars so they dont carry over turns and mess things up
    playerMoveInput = "reset"
    playerMoveInput1 = "reset"
    playerMoveInput2 = "reset"
    
    # ask player which corridor to defend and which weapon to use?
    while True: 
        playerMoveInput = input("Defend which corridor? (A,B,C,D,E) \nMissile or Tank? (M,T) \nSkip your turn (Enter) \n").upper() 
        
        
        # sceanrios
        if playerMoveInput == "":
            break

        if "A" in playerMoveInput:
            playerMoveInput1 = "A"
            
            if "M" in playerMoveInput and mC > 0:
                playerMoveInput2 = "missile"
                break
            elif mC == 0:
                print("--> No missiles left!\n") 
                pass
        
            elif "T" in playerMoveInput and tC > 0:
                playerMoveInput2 = "tank"
                break 
            elif tC == 0:
                print("--> No tanks left!\n") 
                pass
            else:
                print("That's not an option, try again.\n")


        elif "B" in playerMoveInput:
            playerMoveInput1 = "B"

            if "M" in playerMoveInput and mC > 0:
                playerMoveInput2 = "missile"
                break
            elif mC == 0:
                print("--> No missiles left!\n") 
                pass
        
            if "T" in playerMoveInput and tC > 0:
                playerMoveInput2 = "tank"
                break 
            elif tC == 0:
                print("--> No tanks left!\n") 
                pass
            else:
                print("That's not an option, try again.\n")

        elif "C" in playerMoveInput:
            playerMoveInput1 = "C"

            if "M" in playerMoveInput and mC > 0:
                playerMoveInput2 = "missile"
                break
            elif mC == 0:
                print("--> No missiles left!\n") 
                pass
        
            if "T" in playerMoveInput and tC > 0:
                playerMoveInput2 = "tank"
                break 
            elif tC == 0:
                print("--> No tanks left!\n") 
                pass
            else:
                print("That's not an option, try again.\n")

        elif "D" in playerMoveInput:
            playerMoveInput1 = "D"

            if "M" in playerMoveInput and mC > 0:
                playerMoveInput2 = "missile"
                break
            elif mC == 0:
                print("--> No missiles left!\n") 
                pass
        
            if "T" in playerMoveInput and tC > 0:
                playerMoveInput2 = "tank"
                break 
            elif tC == 0:
                print("--> No tanks left!\n") 
                pass
            else:
                print("That's not an option, try again.\n")

        elif "E" in playerMoveInput:
            playerMoveInput1 = "E"

            if "M" in playerMoveInput and mC > 0:
                playerMoveInput2 = "missile"
                break
            elif mC == 0:
                print("--> No missiles left!\n") 
                pass
        
            if "T" in playerMoveInput and tC > 0:
                playerMoveInput2 = "tank"
                break 
            elif tC == 0:
                print("--> No tanks left!\n") 
                pass
            else:
                print("That's not an option, try again.\n")


        else:
            print("That's not an option, try again.\n")





        
        

               
    # This code updates the player with all of the occurences in the game  
    if "M" in playerMoveInput and mC > 0 or "T" in playerMoveInput and tC > 0:
        incomingMessage = (f"We are defending corridor {playerMoveInput1} with a {playerMoveInput2} attack!")
    elif 20 < i < 28:
        incomingMessage = ("Sir, reports are coming in that the tentacle attacks are slowing down. We are winning this fight!")
    
    elif playerMoveInput == "":        
        incomingMessage = ("The battle continues sir...")

    if mC == tC == 0:        
        incomingMessage = ("Sir, our weapons have been exhausted, all we can do now is pray.")

    else:    
        incomingMessage = ("The creatures are advancing sir...")
        pass
    





    # convert the text into character icons for the game board
    if playerMoveInput2 == "missile":
        playerMoveInput2 = "↟"
    elif playerMoveInput2 == "tank":
        playerMoveInput2 = "≙" #¥
        tC = tC - 1
    else:
        #print(":: ERROR 392")
        pass
    

    if playerMoveInput1 == "A":
        a11 = playerMoveInput2
    elif playerMoveInput1 == "B":
        b11 = playerMoveInput2
    elif playerMoveInput1 == "C":
        c11 = playerMoveInput2
    elif playerMoveInput1 == "D":
        d11 = playerMoveInput2
    elif playerMoveInput1 == "E":
        e11 = playerMoveInput2

    else:
        #print(":: ERROR 407")
        pass

    #print(":: player move is over.")
    


    # the whole game structure loops from these 2 funcs
    botMove()
    showBoard()

        
        
            
            
def processInteractions():


    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    global i,incomingMessage
    global peopleA,peopleB,peopleC,peopleD,peopleE,clearA,clearB,clearC,clearD,clearE  
    
    import random    
    
    
    # player losing people after bot touches row 10
    if a10 == "ζ":
        peopleA = "x"
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = a11 = " "
        #print(f":: peopleA has been triggered! var is now: {peopleA}")
        incomingMessage = ("Sir, we have lost a colony to the alien invasion, we must avenge them!")
    if b10 == "ζ":
        peopleB = "x"        
        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b10 = b11 = " "
        #print(f":: peopleB has been triggered! var is now: {peopleB}")
        incomingMessage = ("Sir, we have lost a entire colony to the alien invasion, they will be remembered for their sacrifice.")
    if c10 == "ζ":
        peopleC = "x"
        c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = " "
        #print(f":: peopleC has been triggered! var is now: {peopleC}")
        incomingMessage = ("The aliens have taken a colony, many women and children have been lost.")
    if d10 == "ζ":
        peopleD = "x"
        d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = d9 = d10 = d11 = " "
        #print(f":: peopleD has been triggered! var is now: {peopleD}")
        incomingMessage = ("Colony destroyed sir, we can't afford anymore losses to the base.")
    if e10 == "ζ":
        peopleE = "x"
        e1 = e2 = e3 = e4 = e5 = e6 = e7 = e8 = e9 = e10 = e11 = " "
        #print(f":: peopleE has been triggered! var is now: {peopleE}")
        incomingMessage = ("Regret to inform that a colony has been overtaken. No known survivors.")

    else:
        #print(":: ERROR 441! No corridor people were lost!")
        pass

    
    
    # MISSILE SECTION =======================================================================

     
    # clear the corridor if a missile destroyed (big hit) it
    if a1 == "x":
        #print(":: corridor A cleared by a missile big hit")
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = " "
    elif b1 == "x":
        #print(":: corridor B cleared by a missile big hit")
        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b10 = " "
    elif c1 == "x":
        #print(":: corridor C cleared by a missile big hit")
        c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = " "
    elif d1 == "x":
        #print(":: corridor D cleared by a missile big hit")
        d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = d9 = d10 = " "
    elif e1 == "x":
        #print(":: corridor E cleared by a missile big hit")
        e1 = e2 = e3 = e4 = e5 = e6 = e7 = e8 = e9 = e10 = " "
    else:
        #print(":: ERROR 472 clear corridor A else")
        pass


    # clear the corridor of the x if a missile missed
    if a10 == "x":
        a10 = " "
    elif b10 == "x":
        b10 = " "
    elif c10 == "x":
        c10 = " "
    elif d10 == "x":
        d10 = " "
    elif e10 == "x":
        e10 = " "
    else:
        #print(":: ERROR 487 missile miss clearing (no missile missed)")
        pass


    # clear the corridor if a missile hit a single square x of it
    missileClearCorridorSingleHit(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,"A")
    missileClearCorridorSingleHit(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,"B")
    missileClearCorridorSingleHit(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,"C")
    missileClearCorridorSingleHit(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,"D")
    missileClearCorridorSingleHit(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,"E")


    # missiles launching and then hitting, missing or big hitting
    missilesLaunching(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,"A")
    missilesLaunching(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,"B")
    missilesLaunching(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,"C")
    missilesLaunching(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,"D")
    missilesLaunching(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,"E")



    # missiles moving forward from invisible to visible 10s in corridors
    # the invisible a11 is just a holding space to make the display work nicely
    if a11 == "↟" and a10 == " ": 
        a10 = "↟"
        a11 = " "

    elif b11 == "↟" and b10 == " ": 
        b10 = "↟"
        b11 = " "

    elif c11 == "↟" and c10 == " ": 
        c10 = "↟"
        c11 = " "

    elif d11 == "↟" and d10 == " ": 
        d10 = "↟"
        d11 = " "

    elif e11 == "↟" and e10 == " ": 
        e10 = "↟"
        e11 = " "

    else:
        #print(":: else ERROR 638")
        pass



    # TANKS SECTION =======================================================================



    # tanks moving forward in each corridor
    tankMovingForward(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,"A")
    tankMovingForward(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,"B")
    tankMovingForward(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,"C")
    tankMovingForward(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,"D")
    tankMovingForward(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,"E")
  

    # tanks clearing each corridor
    clearTheCorridorTank1(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,clearA,"A")
    clearTheCorridorTank1(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,clearB,"B")
    clearTheCorridorTank1(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,clearC,"C")
    clearTheCorridorTank1(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,clearD,"D")
    clearTheCorridorTank1(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,clearE,"E")





# SUPPORTING FUNCTIONS SECTION =======================================================================


def clearTheCorridorTank2(): #this works for tanks so far

    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    global i,clearVar,tC,incomingMessage


    #print(f":: at least the clearTheCorridorTank2 func started, here's clearVar:{clearA}")


    if clearA == True:
        a1 = "x"
        a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = " " # corridor A is clear
        #tC = tC - 1 # the board shows one less tank available
        #print(":: Corridor A is clear!")
        incomingMessage = ("Corridor A has been cleared by our tanks!")
    elif clearB == True:
        b1 = "x"
        b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b10 =" " # corridor B is clear
        #tC = tC - 1
        #print(":: Corridor B is clear!")
        incomingMessage = ("Corridor B has been cleared by our tanks!")
    elif clearC == True:
        c1 = "x"
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = " " # corridor C is clear
        #tC = tC - 1
        #print(":: Corridor C is clear!")
        incomingMessage = ("Corridor C has been cleared by our tanks!")
    elif clearD == True:
        d1 = "x"
        d2 = d3 = d4 = d5 = d6 = d7 = d8 = d9 = d10 = " " # corridor D is clear
        #tC = tC - 1
        #print(":: Corridor D is clear!")
        incomingMessage = ("Corridor D has been cleared by our tanks!")
    elif clearE == True:
        e1 = "x"
        e2 = e3 = e4 = e5 = e6 = e7 = e8 = e9 = e10 = " " # corridor E is clear
        #tC = tC - 1
        #print(":: Corridor E is clear!")
        incomingMessage = ("Corridor E has been cleared by our tanks!")
    else:
        #print(":: ERROR 1043 - clearTheCorridorTank2 is not working")
        pass




# learning how to make functions with arguments
def clearTheCorridorTank1(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,clearVar,corridorLabel):

    global clearA,clearB,clearC,clearD,clearE
    
    #clearTheCorridorTank1(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,clearA,"A")
    #clearTheCorridorTank1(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,clearB,"B")
    #clearTheCorridorTank1(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,clearC,"C")
    #clearTheCorridorTank1(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,clearD,"D")
    #clearTheCorridorTank1(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,clearE,"E")

    #print(f":: at least the arg func started. clearX values before processing:{clearA,clearB,clearC,clearD,clearE}")
    #print(f"corridorLabel:{corridorLabel}")


    # my first effective use of shorthand python to clean up my messy beginner style
    # also my first function inside a function :)
    def changeCorridorBoolValue():

        global clearA,clearB,clearC,clearD,clearE

        clearA = True if corridorLabel == "A" else False
        clearB = True if corridorLabel == "B" else False
        clearC = True if corridorLabel == "C" else False
        clearD = True if corridorLabel == "D" else False
        clearE = True if corridorLabel == "E" else False  



    # Tank clears corridor (a,b,c,d,e)
    if var1 == "ζ" and var2 == "≙":        
        
        changeCorridorBoolValue()
        clearTheCorridorTank2()         
        #print(f":: var1 explosion")

    elif var2 == "ζ" and var3 == "≙":

        changeCorridorBoolValue() 
        clearTheCorridorTank2()         
        #print(f":: var2 explosion")

    elif var3 == "ζ" and var4 == "≙":  

        changeCorridorBoolValue() 
        clearTheCorridorTank2()       
        #print(f":: var3 explosion")

    elif var4 == "ζ" and var5 == "≙":  
      
        changeCorridorBoolValue() 
        clearTheCorridorTank2()       
        #print(f":: var4 explosion")

    elif var5 == "ζ" and var6 == "≙":
      
        changeCorridorBoolValue() 
        clearTheCorridorTank2()         
        #print(f":: var5 explosion")

    elif var6 == "ζ" and var7 == "≙": 
      
        changeCorridorBoolValue() 
        clearTheCorridorTank2()        
        #print(f":: var6 explosion")

    elif var7 == "ζ" and var8 == "≙": 
       
        changeCorridorBoolValue() 
        clearTheCorridorTank2()        
        #print(f":: var7 explosion")

    elif var8 == "ζ" and var9 == "≙": 

        changeCorridorBoolValue() 
        clearTheCorridorTank2()        
        #print(f":: var8 explosion")

    elif var9 == "ζ" and var10 == "≙": 
    
        changeCorridorBoolValue() 
        clearTheCorridorTank2()        
        #print(f":: var9 explosion")

    else:
        #print(":: ERROR 665 else? no Tank corridor clearning rn.")
        pass


    # do any of the local function vars need to be reset at this point to avoid value issues?
       
  



def tankMovingForward(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,corridorLabel):


    #tankMovingForward(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,"A")
    #tankMovingForward(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,"B")
    #tankMovingForward(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,"C")
    #tankMovingForward(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,"D")
    #tankMovingForward(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,"E")

    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    
    
    
    # Tank moving forward in corridor A
    # note: the invisible a11 is just a holding space to make the display work nicely
    if var11 == "≙" and var10 == " ": 
        var10 = "≙"
        var11 = " "
    elif var10 == "≙" and var9 == " ":
        var9 = "≙"
        var10 = " "
    elif var9 == "≙" and var8 == " ":
        var8 = "≙"
        var9 = " "
    elif var8 == "≙" and var7 == " ":
        var7 = "≙"
        var8 = " "
    elif var7 == "≙" and var6 == " ":
        var6 = "≙"
        var7 = " "
    elif var6 == "≙" and var5 == " ":
        var5 = "≙"
        var6 = " "
    elif var5 == "≙" and var4 == " ":
        var4 = "≙"
        var5 = " "
    elif var4 == "≙" and var3 == " ":
        var3 = "≙"
        var4 = " "
    elif var3 == "≙" and var2 == " ":
        var2 = "≙"
        var3 = " "
    elif var2 == "≙" and var1 == " ":
        var1 = "≙"
        var2 = " "


    else:
        #print(":: ERROR 989 else! the Tank is not moving.")
        pass

    
    
    # after the processing is done, we assign the new values to the actual vars
    if corridorLabel == "A":
        a11 = var11
        a10 = var10
        a9 = var9
        a8 = var8
        a7 = var7
        a6 = var6
        a5 = var5
        a4 = var4
        a3 = var3
        a2 = var2
        a1 = var1
        #print(f":: A vars:{a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11}")

    elif corridorLabel == "B":
        b11 = var11
        b10 = var10
        b9 = var9
        b8 = var8
        b7 = var7
        b6 = var6
        b5 = var5
        b4 = var4
        b3 = var3
        b2 = var2
        b1 = var1

    elif corridorLabel == "C":
        c11 = var11
        c10 = var10
        c9 = var9
        c8 = var8
        c7 = var7
        c6 = var6
        c5 = var5
        c4 = var4
        c3 = var3
        c2 = var2
        c1 = var1

    elif corridorLabel == "D":
        d11 = var11
        d10 = var10
        d9 = var9
        d8 = var8
        d7 = var7
        d6 = var6
        d5 = var5
        d4 = var4
        d3 = var3
        d2 = var2
        d1 = var1

    elif corridorLabel == "E":
        e11 = var11
        e10 = var10
        e9 = var9
        e8 = var8
        e7 = var7
        e6 = var6
        e5 = var5
        e4 = var4
        e3 = var3
        e2 = var2
        e1 = var1

    else:
        #print(":: ERROR 877 - else, new values to tank moving forward")
        pass

    


def missileClearCorridorSingleHit(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,corridorLabel):

    #missileClearCorridorSingleHit(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,"A")
    #missileClearCorridorSingleHit(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,"B")
    #missileClearCorridorSingleHit(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,"C")
    #missileClearCorridorSingleHit(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,"D")
    #missileClearCorridorSingleHit(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,"E")

    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11





    # clear the corridor if a missile hit a single square x of it
    if var10 == "↟":
        if var1 == "x" or var2 == "x" or var3 == "x" or var4 == "x" or var5 == "x" or var6 == "x" or var7 == "x" or var8 == "x" or var9 == "x":
                        
            var10 = " "
         
            var1 = "ζ" if var1 == "ζ" else " "
            var2 = "ζ" if var2 == "ζ" else " "
            var3 = "ζ" if var3 == "ζ" else " "
            var4 = "ζ" if var4 == "ζ" else " "
            var5 = "ζ" if var5 == "ζ" else " "
            var6 = "ζ" if var6 == "ζ" else " "
            var7 = "ζ" if var7 == "ζ" else " "
            var8 = "ζ" if var8 == "ζ" else " "
            var9 = "ζ" if var9 == "ζ" else " "   

            #print(f":: missile hit single square clearing {corridorLabel}")

        else:
            #print(f":: ERROR 502 - missile hit square clearing {corridorLabel}")
            pass
    else:
        #print(f":: ERROR 504 - missile hit square clearing {corridorLabel}")
        pass


    # after the processing is done, we assign the new values to the actual vars
    if corridorLabel == "A":
        a11 = var11
        a10 = var10
        a9 = var9
        a8 = var8
        a7 = var7
        a6 = var6
        a5 = var5
        a4 = var4
        a3 = var3
        a2 = var2
        a1 = var1

    elif corridorLabel == "B":
        b11 = var11
        b10 = var10
        b9 = var9
        b8 = var8
        b7 = var7
        b6 = var6
        b5 = var5
        b4 = var4
        b3 = var3
        b2 = var2
        b1 = var1

    elif corridorLabel == "C":
        c11 = var11
        c10 = var10
        c9 = var9
        c8 = var8
        c7 = var7
        c6 = var6
        c5 = var5
        c4 = var4
        c3 = var3
        c2 = var2
        c1 = var1

    elif corridorLabel == "D":
        d11 = var11
        d10 = var10
        d9 = var9
        d8 = var8
        d7 = var7
        d6 = var6
        d5 = var5
        d4 = var4
        d3 = var3
        d2 = var2
        d1 = var1

    elif corridorLabel == "E":
        e11 = var11
        e10 = var10
        e9 = var9
        e8 = var8
        e7 = var7
        e6 = var6
        e5 = var5
        e4 = var4
        e3 = var3
        e2 = var2
        e1 = var1

    else:
        #print(":: ERROR 988 - else, new values to missile clearing corridor after single hit")
        pass





def missilesLaunching(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,corridorLabel):

    # missiles looking for contact with the aliens and then hitting, missing or big hitting

    #missilesLaunching(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,"A")
    #missilesLaunching(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,"B")
    #missilesLaunching(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,"C")
    #missilesLaunching(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,"D")
    #missilesLaunching(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,"E")

    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11
    global mC,incomingMessage


    import random
    
    if var10 == "↟": 
        
        # show 1 less missile in the board display area
        mC = mC - 1
        #print(":: mC:",mC)
        
        
        # Missile Attack Random
        missileAttackRandom = ["hit","hit","hit","miss","miss","bigHit","bigHit","bigHit"]
        attackResults = random.choice(missileAttackRandom)
        #print(":: missile rando attack triggered!")

        if attackResults == "hit":
            #print(":: hit")
            incomingMessage = (f"That missile damaged the alien tentacles in corridor {corridorLabel}!")

            if var1 == var2 == var3 == var4 == var5 == var6 == var7 == var8 == var9 == "ζ" and var10 == "↟":
                var9 = "x"
                #print(":: var9 x expression triggered")
            elif var1 == var2 == var3 == var4 == var5 == var6 == var7 == var8 == "ζ" and var9 == " ":
                var8 = "x"
                #print(":: var8 x expression triggered")
            elif var1 == var2 == var3 == var4 == var5 == var6 == var7 == "ζ" and var8 == " ":
                var7 = "x"
                #print(":: var7 x expression triggered")
            elif var1 == var2 == var3 == var4 == var5 == var6 == "ζ" and var7 == " ":
                var6 = "x"
                #print(":: var6 x expression triggered")
            elif var1 == var2 == var3 == var4 == var5 == "ζ" and var6 == " ":
                var5 = "x"
                #print(":: var5 x expression triggered")
            elif var1 == var2 == var3 == var4 == "ζ" and var5 == " ":
                var4 = "x"
                #print(":: var4 x expression triggered")
            elif var1 == var2 == var3 == "ζ" and var4 == " ":
                var3 = "x"
                #print(":: var3 x expression triggered")
            elif var1 == var2 == "ζ" and var3 == " ":
                var2 = "x"
                #print(":: var2 x expression triggered")
            elif var1 == "ζ" and var2 == " ":
                var1 = "x"
                #print(":: var1 x expression triggered")

            else:
                #print("ERROR 498 else missile hit")
                pass

        elif attackResults == "miss":
            #print(":: miss")
            incomingMessage = (f"That missile missed its target in corridor {corridorLabel}!")
            var10 = "x"

        elif attackResults == "bigHit":
            #print(":: bigHit")
            incomingMessage = (f"That missile completely destroyed the enemy in corridor {corridorLabel}!")

            # daisy chain var assigning of value to save space
            var2 = var3 = var4 = var5 = var6 = var7 = var8 = var9 = var10 = "↟"
            var1 = "x"

        else:
            #print(":: else ERROR 1096")
            pass

    else:
        #print(":: else ERROR 1099")
        pass


    # after the processing is done, we assign the new values to the actual vars
    if corridorLabel == "A":
        a11 = var11
        a10 = var10
        a9 = var9
        a8 = var8
        a7 = var7
        a6 = var6
        a5 = var5
        a4 = var4
        a3 = var3
        a2 = var2
        a1 = var1
        #print(f":: A vars:{a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11}")

    elif corridorLabel == "B":
        b11 = var11
        b10 = var10
        b9 = var9
        b8 = var8
        b7 = var7
        b6 = var6
        b5 = var5
        b4 = var4
        b3 = var3
        b2 = var2
        b1 = var1

    elif corridorLabel == "C":
        c11 = var11
        c10 = var10
        c9 = var9
        c8 = var8
        c7 = var7
        c6 = var6
        c5 = var5
        c4 = var4
        c3 = var3
        c2 = var2
        c1 = var1

    elif corridorLabel == "D":
        d11 = var11
        d10 = var10
        d9 = var9
        d8 = var8
        d7 = var7
        d6 = var6
        d5 = var5
        d4 = var4
        d3 = var3
        d2 = var2
        d1 = var1

    elif corridorLabel == "E":
        e11 = var11
        e10 = var10
        e9 = var9
        e8 = var8
        e7 = var7
        e6 = var6
        e5 = var5
        e4 = var4
        e3 = var3
        e2 = var2
        e1 = var1

    else:
        #print(":: ERROR 1170 - else, new values to missile clearing.")
        pass











# begin #####################################################################


# intro
print(intro)

# image
print(asciiImage1)


# bot moves first 5 times (pre turn 1 though) to show the situation
botMove()
botMove()
botMove()
botMove()
botMove()

# process interactions runs through showBoard
showBoard()

playerMove()









