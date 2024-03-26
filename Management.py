from Role import Role
from User import User

class Management:
    def __init__(self):
        self.roles = []
        self.users = []
    
    def add_role(self, role):
        self.roles.append(role)

    def display_roles(self):
        for role in self.roles:
            print(role)

    def create_user(self, name, lastname, role_name):
        found_role = None
        index = self.get_index(self.roles,"name",role_name)
        
        if index != None:
            found_role = self.roles[index]
            user = User(name, lastname, found_role)
            self.users.append(user)
            print(f"\nUser {name} {lastname} was created succesfully with role {role_name}.")
        else:
            print(f"\nRole {role_name} not found.\n")

    def display_users(self):
        for user in self.users:
            print(user)

    def remove_role(self, role_name):
        index = self.get_index(self.roles,"name",role_name)
        try:
            self.roles.pop(index)
            print(f"\nThe role {role_name} was removed\n")
            return None                           
        except TypeError:
            print(f"\nRole {role_name} not found.\n")  

    def update_role_description(self, role_name,new_description):
        index = self.get_index(self.roles,"name",role_name)
        try:
            self.roles.pop(index)
            new_role = Role(role_name,new_description)
            self.roles.insert(index,new_role)
            print(f"\nUpdated Role {role_name} with new description\n")
            return None                           
        except TypeError:
            print(f"\nRole {role_name} not found.\n")                      
    
    def get_index(self,list,attribute,value):
        for i, obj in enumerate(list):
            try:
                if getattr(obj, attribute) == value:
                    return i
            except AttributeError:
                    pass
        return None
    
    
    