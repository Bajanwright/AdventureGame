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
        print('''Well then, let's get started. Do you want to go check out Chicita's room or go to the river of and start 
            looking for her there''')
        user_input_2 = ''
        while user_input_2 != 'room' and user_input_2 != 'river':
            print("Enter 'room' or 'river'.")
            user_input_2 = input()
            if user_input_2 == "room":
                print('''You go to her bedroom and find a letter from her best friend who lives in Quack City.''')
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

            elif user_input_2 == "river":
                print ('''Once you get to the river, you'll see bear footprints, a piece of cloth and some hair.''')
                break
        # Continue code to finish story.

    elif user_input == "no":
        print('Well then, your lose, go home.') # Update to match your story.
        break
