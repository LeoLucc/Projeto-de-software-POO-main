# shared.py
import os
from Controller.UserController.UserManager import UserManager
from Controller.UserController.UserCreator import UserCreator
from Controller.UserController.UserStorage import UserStorage
from Model.User.factory import UserFactory
from Controller.CourseController import CourseManager

# Criando instâncias dos componentes necessários
user_factory = UserFactory()
user_creator = UserCreator(user_factory)
user_storage = UserStorage()

# Instanciando o UserManager e o CourseManager
user_manager = UserManager(user_creator, user_storage)
course_manager = CourseManager()

# Função para limpar o terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
