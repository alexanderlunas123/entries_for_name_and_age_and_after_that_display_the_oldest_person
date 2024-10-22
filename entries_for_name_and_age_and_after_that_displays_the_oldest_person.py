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

        entry_or_entries_of_the_user_or_users[entry_name] = { 
            "Name" : entry_name,
            "Age" : entry_age
        }

        print(f'Name: {entry_or_entries_of_the_user_or_users[entry_name]["Name"]}')
        print(f'Age: {entry_or_entries_of_the_user_or_users[entry_name]["Age"]} years old')
 
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
            
for name_entry_or_entries, age_entry_or_entries in entry_or_entries_of_the_user_or_users.items():
    print(f"Name: {name_entry_or_entries}\nAge: {age_entry_or_entries['Age']} years old\n")     
