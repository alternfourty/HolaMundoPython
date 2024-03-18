class TeamManagement:
    def __init__(self):
        self.team=[]
    def add_member(self,member,role,role_list):
        role_list.check_role(role)
        self.team.append({"name":member,"role":role})
        print(f"{member} Was Added as a New Member with the role {role}")
    def remove_member(self,member):
        try:
            index = next (i for i, memberCard in self.team if memberCard["name"] == member)
            self.team.remove(index)
        except ValueError:
            print(f"The member {member} does not exist in the list")
    def get_members(self):
        print(f"Your Available team members are {self.team}")
    def update_member(self,member_to_change,new_member):
        try:
            self.team.remove(member_to_change)
            self.team.append(new_member)
        except ValueError:
            print(f"The member {member_to_change}, was updated to {new_member}")