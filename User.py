class User:
    def __init__(self, name, lastname, role):
        self.name = name
        self.lastname = lastname
        self.role = role

    def __str__(self):
        return f"User: {self.name} {self.lastname}\nRole: {self.role.name}"