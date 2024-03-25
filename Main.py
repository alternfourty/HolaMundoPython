import RoleManagement, TeamManagement

roles = RoleManagement.RoleManagement()
roles.add_role("Administrator")
roles.add_role("System Administrator")
roles.add_role("Manager")
roles.remove_role("Manager")

team = TeamManagement.TeamManagement()
team.add_member("Jhon")
team.add_member("Laura")
team.remove_member("Jhon")
team.get_members()
roles.get_roles()