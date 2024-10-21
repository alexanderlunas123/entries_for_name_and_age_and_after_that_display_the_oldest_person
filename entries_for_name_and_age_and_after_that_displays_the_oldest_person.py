# Make a var for an array of dictionary {} containing the entry/entries of the user/s (name/s and their age; if more than 1 entry); applying max function to the dictionary to determine the oldest person
entry_or_entries_of_the_user_or_users = {}

# A while loop that evaluates the user/s if he/she/they wants to input another entry and if not, the loop will be satisfied and be finished (the basis for the evaluation is given by the user/s inside the another while loop which is inside of this while loop); this loop goes from the 2nd Loop up to the evaluation 
    # A while loop again inside the previous while loop (1st Loop); a loop where it raises an error whenever the user/s entered an invalid input; and this loop goes from inputting the necessary datas, storing it to the our dedicated dictionary, printing the desired data, and lastly, verifying if the user/s want to input another entry
        # Error function: try (run the given algoruthm)
            # name input
            # age input 
while True:
    while True:
        try:
            entry_name = input("Enter the name (can be you or anyone): ")  
            entry_age = int(input("Enter the age (your age or their age): "))           

            # the_assigned_dictionary[name] = {"age" : age}; storing the inputted datas into the dictionary

            # print the oldest person (using the dictionary with the max function)

            # Asks the user/s if he/she/they wants to input another entry 
            # break
        # Error function: except (raises the error)
        except:
            print("Invalid input, please try again.")

    # if user_will_input_another_entry is == to the inputted string "No"
        # then print the oldest person (using the dictionary with the max function)
        # break
    # elif user_will_input_another_entry is != to "Yes"
        # then print "Invalid input, please try again."