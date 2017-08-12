start = '''
You wake up strapped to a chair at the bottom of a grave. Your arms are tied behind your back, and your feet are tied to the chair.
You look up and see the Riddler standing over you with a shovel in his hand.
"You have to play my games to live. It's game over once you get a riddle wrong.
Get all three right then everyone lives! If you get the first two right, you and one other person dies. If you only get the first one wrong then you and three people die.
It's game over for you and five innocents if you get them all wrong!
He stabbed the shovel into the ground and rubbed his hands together. 'Let's begin"
'''

print(start)

print("People endangered: 5")
print("'What is the beginning of eternity, the end of time and space, the beginning of every end, and every race?''")
user_input = input()
if user_input == "e":
    print("'Congrats, you just saved yourself and two others...''")
    print("People endangered: 3")
    print("'What starts with the letter 'e,' ends with 'e,' but only has one letter?''")
    user_input = input()
    if user_input == "eye":
        print("'Congrats, you saved two more people. Ready for the final round?''")
        print("People endangered: 1")
        print("'What belongs to you, but is used by others?'")
        user_input = input()
        if user_input == "your name":
            print("'Congradulations young Gothamite, you saved your butt and 5 people'")
            print("The Riddler walks away from the grave leaving you tied to the chair six feet below the ground.")
        else:
            print("'You little idiot.' He takes the shovel and buries you in dirt. 'I hope your guilty conscience can deal with killing someone... Oh wait, you're gonna be dead too!'")
            print("People killed: 1")
    else:
        print("'WHY DO YOU DO THIS?!' He angrily grabs the shovel and knocks you out with it. He begins to bury you alive.")
        print("People killed: 3")
else:
    print("The Riddler shakes his head and grabs his shovel to bury you alive.")
    print("People killed: 5")
