# Lets load configuration

from config import CONFIG

VERSION = CONFIG["version"]
print(f"Running system in {VERSION} mode...")

if VERSION == "v1":
    from version1 import *
elif VERSION == "v2":
    from version2 import *
elif VERSION == "v3":
    from version3 import *
else:
    raise ValueError(f"Unsupported version: {VERSION}")

# Lets create a display menu

def display_menu():
    
    """Display the main menu options"""
    
    print("\n" + "="*50)
    print("    ADVANTRA AUTHENTICATION SYSTEM")
    print("="*50)
    print("1. Register New User")
    print("2. Login User")
    print("3. List All Users")
    print("4. Remove User")
    print("5. Update Password")
    print("0. Quit")
    print("-"*50)

def register_user():
   
    print("\n--- USER REGISTRATION ---")
    name = input("Enter full name: ").strip()
    email = input("Enter email address: ").strip()
    password = input("Enter password: ").strip()
    
    if not name:
        print("Name cannot be empty")
        return
    
    result = register(email, name, password)
    
    if result["Status"] == "success":
        print(f"{result['Message']}")
        print(f"Your User ID is: {result['User_id']}")
    else:
        print(f"{result['Message']}")

def user_login():
   
    print("\n--- USER LOGIN ---")
    email = input("Enter email address: ").strip()
    password = input("Enter password: ").strip()
    
    result = login(email, password)
    
    if result["Status"] == "success":
        print(f"{result['Message']}")
        print(f"Welcome! Your User ID is: {result['User_id']}")
    else:
        print(f"{result['Message']}")

def list_all_users():
    
    try:
        print("\n--- ALL REGISTERED USERS ---")
        users_list = list_users()
        if not users_list:
            print("No users registered yet!")
            return users_list
    
        print(f"Total Users: {len(users_list)}")
        print("-" * 50)
        print(f"{'ID':<5} {'Name':<20} {'Email':<30}")
        print("-" * 50)
        
        for user in users_list:
            print(f"{user['id']:<5} {user['name']:<20} {user['email']:<30}")
       
    except:
         print("\n--- ALL REGISTERED USERS ---")
         users_list = list_users()

def remove_a_user():
   
    print("\n--- REMOVE USER ---")
    
    
    users_list = list_users()
    if not users_list:
        print("No users to remove!")
        return
    
    print("Current users:")
    for user in users_list:
        print(f"ID: {user['id']} - {user['name']} ({user['email']})")
    
    try:
        user_id = int(input("\nEnter User ID to remove: "))
        result = remove_user(user_id)
        
        if result["Status"] == "success":
            print(f"{result['Message']}")
        else:
            print(f"{result['Message']}")
            
    except ValueError:
        print("Please enter a valid number!")

def update_user_password():
   
    print("\n--- UPDATE PASSWORD ---")
    
  
    users_list = list_users()
    if not users_list:
        print("No users found!")
        return
    
    print("Current users:")
    for user in users_list:
        print(f"ID: {user['id']} - {user['name']}")
    
    try:
        user_id = int(input("\nEnter your User ID: "))
        old_password = input("Enter your current password: ").strip()
        new_password = input("Enter your new password: ").strip()
        
        result = update_password(user_id, old_password, new_password)
        
        if result["Status"] == "success":
            print(f"{result['Message']}")
        else:
            print(f"{result['Message']}")
            
    except ValueError:
        print("Please enter a valid User ID!")


def main():
    """Main program loop"""
    print(" Starting Advantra Authentication System...")
    
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (0-6): ").strip()
            
            if choice == "1":
                register_user()
            elif choice == "2":
                user_login()
            elif choice == "3":
                list_all_users()
            elif choice == "4":
                remove_a_user()
            elif choice == "5":
                update_user_password()
            elif choice == "0":
                print("\nThank you for using Advantra Authentication System!")
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please select a number between 0-6.")
                
        except KeyboardInterrupt:
            print("\n\nSystem interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")




if __name__ == "__main__":
    main()