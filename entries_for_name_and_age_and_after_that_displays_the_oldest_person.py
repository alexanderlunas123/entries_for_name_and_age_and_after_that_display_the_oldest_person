# variable for the dictionary which will contain the entry/entries of names and their age as key-values pair
entry_or_entries_of_the_user_or_users = {}

# variable for special characters that is valid or allowed in the name input
allowed_special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" 

# loop 1 for each entries
while True:   
        # loop 2-a for the evaluation of name input 
        while True:
            # input function with .strip() method to eliminate trailing spaces on the external part of the inputted name
            entry_name = input("Enter the name (can be you or anyone): ").strip()
            # made a variable for handling the spaces internally with the utilzation of the .replace() method; this eliminates the spaces within for a readily evaluation in the next line
            replacing_spaced_names = entry_name.replace(" ", "")
            # evaluates using the if-else statements; evaluates all characters from the inputted names, if it satiesfies the .isalnum() method and special characters
            if all(char.isalnum() or char in allowed_special_characters for char in replacing_spaced_names):
                # just a break so that the loop would be finished
                break  
            # else statement 
            else:
                # print the contextual error or warning
                print("The inputted character(s) is/are invalid.")  
                # noticed the user/s to redo
                print("Please try again")

        # loop 2-b for the evaluation of age input        
        while True:
            # now I use here the try-except error handling so that integers is only the true value          
            try: 
                # input function for age that automatically converts the digits to integers for correct evaluation on the latter part (essentially in identifying the oldest)            
                entry_age = int(input("Enter the age (your age or their age): "))
                # break again to finishes this loop
                break  
            # except error handling; raises error after the try error handling came-out false value
            except:
                # print the error
                print("Invalid input, must be a number.")  

        # notice the user/s that the entry is processed succesfully; the inputted datas is stored now in the dictionary
        print("Submitted successfully to the database.\n")    

        # format of storing the values inside the dictionary, which is key-values pair ('the identifier' and the 'details')
        entry_or_entries_of_the_user_or_users[entry_name] = { 
            "Age" : entry_age
        }
 
        # loop 2-c for the evaluation of the technicalities to the respond of the user/s; if it is a 'No', 'Yes', or the invalid inputs
        while True:
            # input function for responding 'Yes' or 'No', with a .capitalize() method (this capitalized the first letter so it address the case where the user/s inputted a lowercase characters)
            another_entry = input("Would you like to submit another entry? (Yes/No): ").capitalize()    
            # if statement evaluating if the response is == to 'No'  
            if another_entry == "No":
                # break if returned true
                break
            # elif statement evaluating if or else the respond is == to 'Yes'
            elif another_entry == "Yes":
                # break if returned true
                break
            # else statement; raises the error
            else: 
                # print invalid
                print("Invalid input, 'Yes' or 'No' only.")
                # notice the user/s to redo
                print("Please try again.")

        # if statement that is looped inside the loop 1; after the first evaluation for 'No' response, this will be the final decider to finished the main loop (loop 1), if this returned false, the main loop will start again; only means that the user/s respond with a 'Yes'
        if another_entry == "No":
            # break the main loop (loop 1)
            break 

# var for the oldest persons; stored in a list array
oldest_people_among_the_entries = []
# var assigned to -1 which is impossible to be a thing to an age, so that we a starting point for comparing the datas inside the dictionary
maximum_age = -1

# for loop which iterates each key-values pair inside the dictionary with the help of .items() method (this method will define how the for loop will behave inside the dictionary)
for name_entry_or_entries, age_entry_or_entries in entry_or_entries_of_the_user_or_users.items():
    # evaluates each entry to find the highest value; compared to the -1
    if age_entry_or_entries["Age"] > maximum_age:
        # this is where the oldest age will be determined after evaluating together with the for loop inside the dictionary
        maximum_age = age_entry_or_entries["Age"]
        # also the corresponding pair of the determined oldest age is also addressed (stored on the list since we will also address a case where more than one entry shares th oldest age)
        oldest_people_among_the_entries = [name_entry_or_entries]  
    # after determining the oldest age, the for loop will run again inside the dictionary to confirm this else-if statement, this will determined and accepts true that aligns to the determined oldest age    
    elif age_entry_or_entries["Age"] == maximum_age:
        # with the else-if evaluation, we will append the corresponding pair of those truth oldest age that aligns to the determined oldest age
        oldest_people_among_the_entries.append(name_entry_or_entries)  

# print the context of the result
print("\nBased on the entry/entries:")
# print the result (utilize the .join() method so that if the else-if statement returned true, the evaluation will be added to the output), together with this of course the oldest age itself
print(f"'{'; '.join(oldest_people_among_the_entries)}' is/are the oldest person/s with an age of {maximum_age} years old.\n")

# just print the entry/entries (for tracking the datas), utilized the for loop and the .items() method to iterate the key-values pair inside the dictionary
print("Entry/Entries:")
for name_entry_or_entries, age_entry_or_entries in entry_or_entries_of_the_user_or_users.items():
    print(f"Name: {name_entry_or_entries}\nAge: {age_entry_or_entries['Age']} years old""\n")
