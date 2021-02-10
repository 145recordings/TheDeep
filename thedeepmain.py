import time
import sys
from thedeeptwo import choose1



print("Welcome to the Adventure")

begin = input("Begin? (y) or (n)")

if begin == "y":
    print("You open your eyes...")
    time.sleep(1)
elif begin == "n":
    sys.exit()
    


def main():
    print("You see a large wooden door in front of you.")
    time.sleep(2)
    print("The room you are in is very dark.")
    time.sleep(2)
    print("You have no idea how you got there.")
    time.sleep(2)
    print("You see nothing but the door.")
    time.sleep(2)
    a = input("Do you enter?(y) or (n)")

    if a == "n":
        print("You're eyes have adjusted to the room.")
        time.sleep(2)
        print("You now see an old wooden chest behind you.")
        aa = input("Open the chest? (y) or (n)")
        if aa == "y":
            print("As you bend down to open the chest")
            time.sleep(2)
            print("for a brief second you think you hear someone...")
            time.sleep(2)
            print("or something... breathing.")
            time.sleep(2)
            print("As soon as you open the chest slightly")
            time.sleep(2)
            print("it opens itself to reveal a long wet tongue")
            time.sleep(2)
            print("surrounded by rows of sharp yellow stained teeth.")
            time.sleep(2)
            print("You don't even have a chance to scream.")
            time.sleep(2)
            print("All you see is the tongue and teeth fill your vision and suddenly...")
            time.sleep(4)
            print("Darkness. All you see is darkness.")
            time.sleep(2)
            play = input("Play again? (y) or (n)")
            if play == "y":
                main()
            else:
                sys.exit()
        elif aa == "n":
            print("You don't open the chest.")
            time.sleep(2)
            print("You stand for what seems to be an eternity until you realize...")
            time.sleep(2)
            print("You can't see anything anymore...")
            time.sleep(2)
            print("Or feel anything...")
            time.sleep(2)
            print("You stood too long and died without noticing.")
            time.sleep(10)
            sys.exit()
    elif a == "y":
        print("The door creaks as you open it.")
        time.sleep(2)
        print("You enter a small square room.")
        time.sleep(2)
        print("The wall opposite of you has a painting of a red barn.")
        time.sleep(2)
        print("To your left is an average looking door.")
        time.sleep(2)
        print("To your right is a door with a red puddle extending out from under it.")
        time.sleep(2)

        choose1()
        
    
    


main()
