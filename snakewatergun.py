import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("computer turn:Snake(S) Water(W) or Gun(G)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("Your turn:Snake(S) Water(W) or Gun(G) ")
print(f"computer chose {comp}")
print(f"You chose {you}")
a = gameWin(comp, you)
if a == None:
    print("The Game is tie!")
elif a == True:
    print("You won")
else:
    print("You lost")
