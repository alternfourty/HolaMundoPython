class Role:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Rol: {self.name}\nDescription: {self.description}"