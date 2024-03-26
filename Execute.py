from Management import Management
from Role import Role

def execute():
    version = "0.1.1"
    run = True
    initial = True
    operation = Management()
    while(run == True):
        if initial == True:
            print(f"Welcome to Team Manager v.{version}:\nThis is your first run. The role Administrator will be set")
            role_name = "Administrator"
            role_description = "Administrator role for full management access"
            new_role = Role(role_name,role_description)
            operation.add_role(new_role)
            print("Please create a user, this will be defaulted Administrator")
            user_name = input("\nEnter the Name of the User: ")
            user_lastName = input("\nEnter the last Name of the user: ")
            operation.create_user(user_name,user_lastName,role_name)
            print("\nInitial setup completed. Main menu will be displayed")
            initial = False
        else:
            print(f"\nWelcome to Team Manager v.{version}:\nIMPORTANT: Data is not persistant in this version\nPlease choose operation number to execute: \n")
            print("1. Create New Role\n2. Create New User\n3. Remove a Role\n4. Update role description\n5. Display all Roles Available\n6. Display all Users Available\n7. Exit Program")
            option = input("\nEnter the operation number: ")
            match option:
                case "1":
                    print("\nYou selected 1. Create New Role")
                    role_name = input("\nEnter the name of the new role:")
                    role_description = input("\nPlease enter the role Description:")
                    new_role = Role(role_name,role_description)
                    operation.add_role(new_role)
                case "2":
                    print("\nYou selected 2. Create New User")
                    user_name = input("\nEnter the Name of the User: ")
                    user_lastName = input("\nEnter the last Name of the user: ")
                    user_role = input("\nEnter the role name for the user: ")
                    operation.create_user(user_name,user_lastName,user_role)
                case "3":
                    print("\nYou selected 3. Remove a Role")
                    role_name = input("\nEnter the role name to remove (CANNOT BE UNDONE): ")
                    operation.remove_role(role_name)
                case "4":
                    print("\nYou selected 4. Update role description")
                    role_name = input("\nEnter the role name to update: ")
                    role_description = input("\nEnter the new role description: ")
                    operation.update_role_description(role_name,role_description)
                case "5":
                    print("\nYou selected 5. Display all Roles Available")
                    operation.display_roles()
                case "6":
                    print("\nYou selected 6. Display all Users Available")
                    operation.display_users()
                case "7":
                    print("Thanks for Using Team Manager")
                    run = False
                case _:
                    run = False
    return None

    