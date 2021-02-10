import time
import sys


x = 0

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
    elif b != 1 or 2 or 3:
        print("You must type 1 or 2 or 3.")
        choose1()
#shoutBool resides here
def choose2():
    global x
    x = x + 1
    if x == 1:
        global shoutBool
        shoutBool = False

    bb = input("Continue looking(1) walk down the hallway(2) or shout at the people below(3) ?:")
    if bb == "1":
        print("You look on in horror and fascination.")
        time.sleep(2)
        print("You notice the people don't just appear to be the same...")
        time.sleep(2)
        print("They are the same...")
        time.sleep(2)
        print("Same face...")
        time.sleep(2)
        print("Same height...")
        time.sleep(2)
        print("Same hair...")
        time.sleep(2)
        print("And they're all wearing the same white gowns.")
        time.sleep(2)
        choose2()
    elif bb == "2":
        print("")
    elif bb == "3" and shoutBool == False:
        shout = input("What do you shout? ")
        shoutBool = True
        print(f"You take a deep breath and shout {shout}!")
        time.sleep(2)
        print("Suddenly, every single head turns towards you at the same time.")
        time.sleep(2)
        print("The sound echoed in the hallway.")
        time.sleep(2)
        print("A few seconds pass of absolute silence.")
        time.sleep(2)
        print("A chill crawls down your spine.")
        time.sleep(2)
        print("Before you even realize it,")
        time.sleep(2)
        print("All the people run towards the edges of the room they're in.")
        time.sleep(2)
        print("You feel a sinking feeling in your stomach.")
        time.sleep(2)
        print("Slowly the room empties out to leave only the empty conveyor belts")
        time.sleep(2)
        print("You hear a low rumble of scuffling for a few minutes until it stops.")
        choose2()
    elif bb == "3" and shoutBool == True:
        print("They're all gone.")
        choose2()



    elif bb != 1 or 2 or 3:
        print("You must choose 1 or 2 or 3.")
        choose2()

#transfer to thedeepthree with option 2 from choose2
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
    choose2()
    

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