from src.factores.user_factory import UserFactory

if __name__ == "__main__":
    user = UserFactory.create_user("Antonio")
    print(user)
