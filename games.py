start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and you see a troll in front of you 'You may not pass unless you correctly answer this riddle. If you fail, you will become my lunch. What starts with an e, ends with an e, but only has one letter?'")
    user_input = input()
    if user_input == "eye":
        print ("'Darn, you ruined my lunch hour.' The troll moves to the side and you continue your way down the path.")
    else print("HAHA free food. You are now dead. Play again.")
elif user_input == "right":
    print("You choose to go right and ...") # finished the story writing what happens
