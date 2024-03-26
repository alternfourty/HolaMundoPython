from Role import Role
from User import User
from Management import Management

""" roles = Rol.RoleManagement()
roles.add_role("Administrator")
roles.add_role("System Administrator")
roles.add_role("Manager")
roles.remove_role("Manager")

team = User.TeamManagement()
team.add_member("Jhon")
team.add_member("Laura")
team.remove_member("Jhon")
team.get_members()
roles.get_roles() """

new_instance = Management()


new_role1 = Role("Administrator","Role for top Administrator. unique")
new_role2 = Role("Operator","Operators take action by orders of the administrator")
new_instance.add_role(new_role1)
new_instance.add_role(new_role2)

new_instance.display_roles()

rol_to_update = "Operator"
new_description = "Operators can be deployed as needed, can take orders or make self assesment to execute actions if no orders isseud"

new_instance.update_role(rol_to_update,new_description)

new_instance.display_roles()