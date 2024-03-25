class TeamManagement:
    def __init__(self):
        self.team=[]
    def add_member(self,member):
        self.team.append(member)
        print(f"{member} Was Added as a New Member of the team")
    def remove_member(self,member):
        try:
            self.team.remove(member)
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