entry_or_entries_of_the_user_or_users = {}

allowed_special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" 

while True:    
        while True:
            entry_name = input("Enter the name (can be you or anyone): ").strip()
            replacing_spaced_names = entry_name.replace(" ", "")
            if all(char.isalnum() or char in allowed_special_characters for char in replacing_spaced_names):
                break   
            else:
                print("The inputted character(s) is/are invalid.")  
                print("Please try again")
        while True:          
            try:             
                entry_age = int(input("Enter the age (your age or their age): "))
                break  
            except:
                print("Invalid input, must be a number.")   

        print("Submitted successfully to the database.\n")        

        entry_or_entries_of_the_user_or_users[entry_name] = { 
            "Name" : entry_name,
            "Age" : entry_age
        }
 
        while True:
            another_entry = input("Would you like to submit another entry? (Yes/No): ").capitalize()      
            if another_entry == "No":
                break
            elif another_entry == "Yes":
                break
            else: 
                print("Invalid input, 'Yes' or 'No' only.")
                print("Please try again.")

        if another_entry == "No":
            break       

oldest_person_among_the_entries = None
maximum_age = -1

for name_entry_or_entries, age_entry_or_entries in entry_or_entries_of_the_user_or_users.items():
    if age_entry_or_entries["Age"] > maximum_age:
        maximum_age = age_entry_or_entries["Age"]
        oldest_person_among_the_entries = name_entry_or_entries

print(f"\nThe oldest person is '{oldest_person_among_the_entries}' with an age of {maximum_age} years old.\n")       
