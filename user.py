class User:
    def __init__(self, username, role='guest'):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"User(username='{self.username}', role='{self.role}')"