#Landscaper game in python
print("hola mundo")

# You are starting a landscaping business, but all you have are your teeth.
# Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.

money = 0
tool = 0
playerchoice = 9

welcomeprompt = """
Welcome to Landscaper!
A game where you cut grass. (Watch out Baldur's Gate 3)
You can spend the day cutting grass to earn money.  
The better your tools the more money you can earn.
Use money to upgrade your tools.  
Eventually you may even earn enough money to escape this hellish gameplay loop!
"""
moneyprompt = "You have $"+str(money),"currently."

prompt1 ="""
Currently your teeth are the only tools available, you can spend the day cutting 
grass or you can go shopping for a pair of Rusty's rusty scissors $5.
1: Cut grass.
2: Go shopping.
0: Exit game.
"""

prompt2 ="""
You have a pair of rusty scissors. You can spend the day cutting lawns 
to make $5 or you can go shopping for an old-timey push mover for $25.
1: Cut grass.
2: Go shopping.
0: Exit game.
"""
prompt3 ="""
You have an old-timey push mower. You can spend the day cutting 
lawns to make $50 or you can go shopping for a LAWN DOZER 9000 for $250.
1: Cut grass.
2: Go shopping.
0: Exit game.
"""

prompt4 ="""
You have a battery mower. You can spend the day cutting 
lawns to make $50 or you can go shopping for some starving students for $500.
1: Cut grass.
2: Go shopping.
0: Exit game.
"""
prompt5 ="""
You have an army of students. You can spend the day cutting 
lawns to make $250.
1: Cut grass.
2: Go shopping.
0: Exit game.
"""

print(welcomeprompt)

while int(playerchoice) != 0:
    print("You have $"+str(money)+".")
    if tool ==0:
        playerchoice= input(prompt1)
        if int(playerchoice) ==1:
            money+=1
            print("You made $1 cutting grass.")
        elif int(playerchoice)==2 and money>=5:
            tool+=1
            money-=5
            print("You bought scissors!")
        elif int(playerchoice)==2 and money<5:
            print("You went shopping but didn't have enough money...")
        elif int(playerchoice)==0:
            print("Exiting game.")
        else:
            print("Invalid input")
    elif tool!=0:
        playerchoice= input(prompt2)




# Using the the fancy battery-powered lawnmower, you can spend the day cutting lawns and make $100. You can do this as much as you want.

# 🔴 Commit your work!
# Your commit message should read something like:
# “landscaper: user can use battery-powered lawnmower to cut grass”

# At any point, if you are currently using the fancy battery-powered lawnmower, you can hire a team of starving students for $500. You can do this once, assuming you have enough money.

# 🔴 Commit your work!
# Your commit message should read something like:
# “landscaper: user can hire a team”

# Using the the team of starving students, you can spend the day cutting lawns and make $250. You can do this as much as you want.

# 🔴 Commit your work!
# Your commit message should read something like:
# “landscaper: user can use a team to cut grass”

# You win the game when you have a team of starving students and $1000. In this situation, send a message to the user telling them, they’ve won.

# 🔴 Commit your work!
# Your commit message should read something like:
# “landscaper: win scenario”

