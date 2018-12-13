# Update this text to match your story.
start = '''
The king of Wang City has called you to help him find his lost daughter, Chiquita. He says that she's been 
missing since yesterday. The last time King Pollo saw his daughter was yesterday when she said she was going to the river. 
Would you like to help King Pollo of Wang City to find his daughter?
'''

print(start) #Python will present this scenario to player when the code is ran.

user_input = ''
while user_input != 'yes' and user_input != 'no':
    print("Enter 'yes' or 'no'.") # Update to match your story.
    user_input = input()

    if user_input == "yes":
        print('''You decide to run out of the lab. Your co-worker reaches for you and
        his arm suddenly falls. Unsure if what to do next you''')
        user_input_2 = ''
        while user_input_2 != 'call police' and user_input_2 != 'look back':
            print("Enter 'call police' or 'look back'.")
            user_input_2 = input()
            if user_input_2 == "call police":
                print('''You walk away from the lab and take out your phone. You call
                the police and explain the situation. The police and ambulance quickly
                arrive and enter the room. They also collapse. You...''')
                user_input_3 = ''
                while user_input_3 != 'collect gas sample' and user_input_3 != 'run':
                    print ("Enter 'collect gas sample' or 'run'")
                    user_input_3 = input()
                    if user_input_3 == "collect gas sample":
                        print ('''You take a test tube out of your lab coat and collect a
                        gas sample. Suddenly all the people who fainted rose. They looked
                        dead and moved slowly. "Brainsss" They yelled in unison. You died.''')
                        break
                    elif user_input_3 == "run":
                        print ('''You sprint away as fast as you can. You leave the building
                        and look up. You left the window open. You...''')
                        user_input_4 = ''
                        while user_input_4 != "go back to close window" and user_input_4 != "go home":
                            print ("Enter 'go back to close window' or 'go home'.")
                            user_input_4 = input()
                            if user_input_4 == "go back to close window":
                                print ('''You run back into the building which is now filled
                                with smoke. You try to hold your breath. You faint. When you
                                wake up you feel a thirst for human brains. You became a zombie. THE END''')
                                break
                            elif user_input_4 == "go home":
                                print ('''You go home realizing you'll probably never get funded again. You...''')
                                user_input_5 = ''
                                while user_input_5 != 'give up' and user_input_5 != 'do research':
                                    print ("Enter 'give up' or 'do research'.")
                                    user_input_5 = input ()
                                    if user_input_5 == "give up":
                                        print ('''You turn on thr TV and start watching Grey's
                                        Anatomy and after a few episodes you smell gas. You start
                                        coughing and you faint. THE END.''')
                                        break
                                    elif user_input_5 == "do research":
                                        print ('''After researching the ingrediants in the solution you
                                        made. You realized it had a weird reaction with your co-worker's
                                        solution. You realized that it's what made them into a zombie. You...''')
                                        user_input_6 = ''
                                        while user_input_6 != 'get in your car' and user_input_6 != 'tell the police':
                                            print("Enter 'get in your car' or 'tell the police'.")
                                            user_input_6 = input()

            elif user_input_2 == "look back":
                print ('''You see your co-worker is no longer where you left him. Terrified
                and confused, you look at the door an see that you left it wide open. A group of
                human-looking monsters run after you, catch you and eat you. THE END''')
                break
        # Continue code to finish story.

    elif user_input == "risk fainting":
        print('''You choose to risk fainting to save your co-worker. You run into the room.
        Your co-worker is no longer there. You turn around and see him. He opens his mouth
        and snarls. You faint. THE END''') # Update to match your story.
        break