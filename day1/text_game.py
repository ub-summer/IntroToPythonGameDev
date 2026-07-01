print("You are a plant with the power to shoot")
print("your pollen. You see a zombie. What are")
print("you ganna do?? You can...")
print()

print("shoot: Fire your pollen at the zombie")
print("leaf: Get outa there")
print("leave: Get out of there")
print("talk: strike up a conversation")
print()

choice = input("What do you want to do? ")

print("You entered: " + choice)
print()

if choice == "shoot":
    print("You shoot the zombie")
    print("Zombie get angry and eats you.")
    print("You lose sucka")
elif choice == "leaf":
    print("You realize you're a plant, and")
    print("can't walk away")
elif choice == "leave":
    print("You leave with your leaves in tact")
elif choice == "talk":
    print("The zombie gets angry and replies, ")
    print('"brains, Brains, BRAINS!!!".. and')
    print("eats you")
else:
    print("You didn't take a valid action")
    print("You sit there and get eaten without")
    print("putting up a fight :(")
    
print()
print("Great choice!.. unless you died")
