from Model.User.Student import Student
from Model.User.Teacher import Teacher
from Model.User.SuperUser import SuperUser

class UserFactory:
    def create_student(self, username, password, age, course, paid):
        return Student(username, password, age, course, paid)

    def create_teacher(self, username, password):
        return Teacher(username, password)

    def create_super_user(self, username, password):
        return SuperUser(username, password)

