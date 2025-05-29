from src.user import User

class UserFactory:
    @staticmethod
    def create_user(username: str, role: str = 'guest') -> User:
        return User(username, role)
