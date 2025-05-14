from Model.User.Student import Student
from Model.User.Teacher import Teacher
from Model.User.SuperUser import SuperUser
from Model.User.factory import UserFactory
from Controller.UserController.UserCreator import UserCreator
from Controller.UserController.UserStorage import UserStorage



class UserManager:
    def __init__(self, creator, storage):
        self.creator = creator   # Injeção de dependência para o criador de usuários
        self.storage = storage   # Injeção de dependência para o armazenamento de usuários

    def add_user(self, role, username, password, age=None, course=None, paid=None):
        # Criando o usuário com base no papel (role)
        user = self.creator.create_user(role, username, password, age, course, paid)
        if user:
            self.storage.add(user)  # Salva o usuário criado
        else:
            print(f"[ERRO] Falha ao criar usuário com role '{role}'. Verifique os dados.")

    def add_student(self, username, password, age, course, paid):
        # Adiciona um estudante
        student = self.creator.create_student(username, password, age, course, paid)
        if student:
            self.storage.add(student)
        else:
            print("[ERRO] Falha ao criar estudante.")

    

    def add_teacher(self, username, password):
        # Adiciona um professor
        teacher = self.creator.create_teacher(username, password)
        if teacher:
            self.storage.add(teacher)
        else:
            print("[ERRO] Falha ao criar professor.")

    def add_super_user(self, username, password):
        # Adiciona um superusuário
        super_user = self.creator.create_super_user(username, password)
        if super_user:
            self.storage.add(super_user)
        else:
            print("[ERRO] Falha ao criar superusuário.")

    def delete_user(self, username, password):
        # Deleta o usuário com base nas credenciais
        if self.storage.remove(username, password):
            print(f"Usuário {username} removido com sucesso.")
        else:
            print(f"[ERRO] Falha ao remover usuário {username}.")

    def check_password(self, username, password):
        # Verifica a senha
        return self.storage.find_by_credentials(username, password)

    def get_user(self, username, password):
        # Retorna o usuário com base nas credenciais
        return self.check_password(username, password)
    
    def get_user_type(self, user):
        if isinstance(user, Student):
            return "student"
        elif isinstance(user, Teacher):
            return "teacher"
        elif isinstance(user, SuperUser):
            return "superuser"
        else:
            return "unknown"


    def get_user_by_id(self, user_id):
        # Retorna um usuário com base no ID
        return self.storage.find_by_id(user_id)

    def list_users(self):
        # Lista todos os usuários
        for user in self.storage.list_all():
            print(user)

    def update_progress(self, username, progress):
        user = next((u for u in self.storage.list_all() if u.username == username), None)
        if user and hasattr(user, "progress"):
            user.progress = progress
            print(f"[INFO] Progresso do usuário '{username}' atualizado para {progress}.")
        else:
            print(f"[ERRO] Usuário '{username}' não encontrado ou não possui atributo 'progress'.")

