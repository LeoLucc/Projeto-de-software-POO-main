class UserCreator:
    def __init__(self, user_factory):
        self.user_factory = user_factory

    def create_user(self, role, username, password, age=None, course=None, paid=None):
        if role == "student":
            return self.create_student(username, password, age, course, paid)
        elif role == "teacher":
            return self.create_teacher(username, password)
        elif role == "superuser":
            return self.create_super_user(username, password)
        else:
            print(f"[ERRO] Role '{role}' inválido!")
            return None

    def create_student(self, username, password, age, course, paid):
        return self.user_factory.create_student(username, password, age, course, paid)

    def create_teacher(self, username, password):
        return self.user_factory.create_teacher(username, password)

    def create_super_user(self, username, password):
        return self.user_factory.create_super_user(username, password)
