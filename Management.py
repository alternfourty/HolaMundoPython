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
        for role in self.roles:
            if role.name == role_name:
                found_role = role
                break

        if found_role:
            user = User(name, lastname, found_role)
            self.users.append(user)
            print(f"User {name} {lastname} created succesfully.")
        else:
            print(f"Role {role_name} not found.")

    def display_users(self):
        for user in self.users:
            print(user)

    def remove_role(self, role_name):
        for role in self.roles:
            if role.name == role_name:
                self.roles.remove(role)
                print(f"Role {role_name} was removed.")
                break
        else:
            print(f"Role {role_name} not found.")

    def update_role(self, role_name, new_roleName = None,new_description = None):
        if new_roleName or new_description != None:
            index = self.get_index(self.roles,"name",role_name)
            try:
                role = self.roles(index)
                role_description = role.description
                if new_roleName != None and new_description != None:
                    self.roles.pop(index)
                    new_role = Role(new_roleName,new_description)
                    self.roles.insert(index,new_role)
                    print(f"Updated Role Name and Description")
                    return None
                if new_roleName != None and new_description == None:
                    self.roles.pop(index)
                    new_role = Role(new_roleName,new_description)
                    self.roles.insert(index,new_role)
                    print(f"Updated Role Name and Description")
                    return None                             
            except ValueError:
                print(f"Role {role_name} not found.")
        else:
            print(f"Any values entered for update, Operation Cancelled")
        
        
        
            
        
            
        for role in self.roles:
            if Role.name == role_name:
                role.descripcion = new_description
                print(f"Role {role_name} updated succesfully.")
                break
        else:
            print(f"Role {role_name} not found.")
            
    
    def get_index(self,list,attribute,value):
        for i, obj in enumerate(list):
            try:
                if getattr(obj, attribute) == value:
                    return i
            except AttributeError:
                    pass
        return None
