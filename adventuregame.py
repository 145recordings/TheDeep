import time
import sys


print("Welcome to the Adventure")

begin = input("Begin? (y) or (n)")

if begin == "y":
    print("You open your eyes...")
    time.sleep(1)
elif begin == "n":
    sys.exit()
    
def choose1():
    b = input("Enter the left door(1) inspect the painting(2) or enter the right door(3): ")
    if b == "1":
        print("You open the left door...")
        time.sleep(2)
        leftdoor()
    elif b == "2":
        print("You inspect the painting...")
        time.sleep(2)
        painting()
    elif b == "3":
        print("You open the right door...")
        time.sleep(2)
        rightdoor()

def leftdoor():
    print("A long brightly lit hallway stretches before you...")
    time.sleep(2)
    print("The walls and floor are a clean white")
    time.sleep(2)
    print("As you step into the hallway...")
    time.sleep(2)
    print("You see halfway up the walls on either side are long glass panels.")
    time.sleep(2)
    print("You can't control your curiosity and walk towards the left window.")
    time.sleep(2)
    print("You see hundreds of rows of... what looks like people")
    time.sleep(2)
    print("They all look the same.")
    time.sleep(2)
    print("In between each row of people is what appears to be a conveyor belt.")
    time.sleep(2)
    print("All you can do is look in horror and fascination.")
    

def painting():
    print("As you approach the painting, the smell of old coins and garbage increases")
    time.sleep(2)
    print("The barn has a very deep, dark red color")
    time.sleep(2)
    print("All around the barn are pale corn fields extending into the distance")
    time.sleep(2)
    print("The painter must have been a minimalist.")
    time.sleep(2)
    choose1()

def rightdoor():
    print("Ignoring your now sticky shoes,")
    time.sleep(2)
    print("You take a step into the room.")
    time.sleep(2)
    print("The whole room begins shaking...")
    time.sleep(2)
    print("Wait. No. That's just your knees trembling at what lies before you.")
    time.sleep(2)
    print("Dozens of body parts lay in a heap in the center of the room.")
    time.sleep(2)
    print("A head lies on top of a leg...")
    time.sleep(2)
    print("An arm on top of a foot...")
    time.sleep(2)
    print("Your then hit with the most ungodly stench you've ever experienced...")
    time.sleep(2)
    print("The smell makes your body convulse.")
    time.sleep(2)
    print("Instinctually, you back up out of the room")
    time.sleep(2)
    print("*squish* *squish*")
    time.sleep(2)
    print("Your shoes make it hard to walk they're so sticky")
    time.sleep(2)
    print("You close the door and turn around.")
    choose1()

def main():
    print("You see a large wooden door in front of you.")
    time.sleep(2)
    print("The room you are in is very dark.")
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
