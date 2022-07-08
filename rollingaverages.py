#dice rolling programme that helps understand the average of rolling multiple throws to get a above a user defined number

import random
import os
from colorama import init, Fore, Back, Style

#clear the screen - I have to, it drives me mad otherwise
os.system('cls')
init(autoreset=True)

#wins is the number of times the desired number comes up in the dice rolled
wins = 0
runitup = 1000

#capture user input
print("This programme will give you the anticpated average of 1000 dice rolls\n")
print("- You'll be asked to enter number of dice (how many dice you'll roll for hit, wounds, or attacks for example)")
print("- You'll then be asked what the target result you're looking for (such as 3+, 4+ etc.)\n")

num = int(input(Fore.RED +"Enter the number of dice you want to roll: "))
want = int(input(Fore.RED +"What result are you looking for? "))  

#run the loop 1000 times, for user defined number of dice.  Capture matches between desired result and rolls (wins) in a list   
for r in range(runitup):
    for x in range(num):
        result = random.randint(1,6)
        if result >= want:
            wins = wins+1  

#the logic to find the probability (percent) of the matches (wins)
total = runitup * num
per = wins / total * 100
final_per = (round(per, 2))
example = num * final_per / 100
summary = (round(example))

print(Style.RESET_ALL)

print(Fore.GREEN + Style.DIM +"----------------------------------------------")
print(Fore.GREEN + Style.DIM +"You'll get {}+'s on average {}% of the time".format(want, final_per))
print(Fore.GREEN + Style.DIM +"----------------------------------------------\n")

print("In this example: If you rolled to hit {} times, {} would resolve at {}+\n".format(num, summary, want))
