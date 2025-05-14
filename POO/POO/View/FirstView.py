from colorama import Fore
from View.loginInProcessing.RegisterView import RegisterView
from .BaseView import View
from .shared import user_manager, course_manager
from .afterLogin.StudentView import StudentView
from .afterLogin.TeacherView import TeacherView
from .afterLogin.SuperUserView import SuperUserView
import os
from getpass import getpass

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    
"""Adição de dados padrão"""
course_manager.add_course("Java", "Davi", 100, True)
course_manager.add_course("Python", "Davi", 100, False)
user_manager.add_user("student", "Davi", "estudante", "00", "Java", True)
user_manager.add_user("student", "Mariana", "1234", "00", "Python", False)
user_manager.add_user("teacher", "Davi", "professor")
user_manager.add_user("superuser", "adm", "adm")

user_manager.update_progress("Mariana", "100")
clear_terminal()

# Mapeia os tipos de usuário para as classes correspondentes
USER_TYPE_MAPPING = {
    "student": StudentView(),
    "teacher": TeacherView(),
    "superUser": SuperUserView(),
}

class FirstView(View):
    def EnterView(self):
        print(Fore.CYAN + "Welcome to E-Learning Platform login!")
        username = input(Fore.YELLOW + "Enter your name: ")
        password = getpass(Fore.YELLOW + "Enter your password: ")
        user = user_manager.check_password(username, password)
        
        if user:
            # Agora usamos o get_user_type para determinar o tipo do usuário
            user_type = user_manager.get_user_type(user)
            if user_type:
                USER_TYPE_MAPPING.get(user_type).view(user._id)  # Passa o ID para a view correspondente
            else:
                print(Fore.RED + "Invalid user type!")
                self.view()  # Volta para a tela de login ou outra ação
        else:
            choice = input(Fore.RED + "Incorrect password!\n1 - Try again.\n2 - Back\n>>> ")
            match choice:
                case "1":
                    self.EnterView() 
                case "2":
                    self.view()  
                case _:
                    print(Fore.RED + "Invalid option! Please try again\n")
                    self.EnterView()


    def view(self):
        while True:
            print(Fore.CYAN + "Welcome to E-Learning Platform!\nWhat do you want to do?")
            choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Enter.\n2 - Register.\n>>> ")
            match choice:
                case "1":
                    self.EnterView() 
                    break
                case "2":
                    RegisterView().view() 
                    break
                case "0":
                    exit()
                case _:
                    print(Fore.RED + "Invalid option! Please try again\n")