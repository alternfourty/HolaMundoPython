class RoleManagement:
    def __init__(self):
        self.roles=[]
    def add_role(self,role):
        self.roles.append(role)
        print(f"Role {role} Added successfully")
    def remove_role(self,role):
        try:
            self.roles.remove(role)
        except ValueError:
            print(f"The role {role} does not exist in the list")
    def get_roles(self):
        print(f"Your Available roles are {self.roles}")
    def update_role(self,role_to_change,new_role):
        try:
            self.roles.remove(role_to_change)
            self.roles.append(new_role)
        except ValueError:
            print(f"The role {role_to_change}, was updated to {new_role}")
            