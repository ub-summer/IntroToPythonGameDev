import random

print("You see a monster. (a) attack (r) run away (t) talk")
action = input("What do you do? ")

if action == "a":
    print("You attack the monster are are eaten")
elif action == "r":
    print("You run away to safety and live to fight another day")
elif action == "t":
    print("The monster explains that they mean no harm and are misunderstood. You become quick friends and go to their place to play GTA5")
else:
    print("Invalid input. Please choose 'a', 'r' or 't'")
