---

### **Factory Method**

O **Factory Method** é um padrão de design criacional que permite a criação de objetos de uma classe sem especificar a classe exata do objeto que será criado. Esse padrão ajuda a delegar a criação de objetos para subclasses ou classes auxiliares, tornando o código mais flexível e fácil de manter.

#### **Implementação do Factory Method no projeto:**

1. **Classe `UserFactory` (Factory):**
   A classe `UserFactory` é responsável por criar diferentes tipos de usuários (`Student`, `Teacher`, `SuperUser`) dependendo do papel fornecido. Ela centraliza a criação dos objetos, garantindo que o tipo correto de usuário seja instanciado sem expor a lógica de criação para o restante do código.

   **Exemplo de implementação:**

   ```python
   class UserFactory:
       @staticmethod
       def create_user(role, username, password, age=None, course=None, paid=None):
           role = role.lower()
           if role == "student":
               return Student(username, password, age, course, paid)
           elif role == "teacher":
               return Teacher(username, password)
           elif role == "superuser":
               return SuperUser(username, password)
           else:
               print(f"[ERRO] Tipo de usuário inválido: {role}")
               return None
   ```

   Aqui, o método `create_user` cria um tipo específico de usuário com base no papel (`role`) fornecido, sem precisar que o código que chama o factory saiba os detalhes de como instanciar o usuário.

2. **Classe `UserCreator` (Método de Criação Delegado):**
   A classe `UserCreator` delega a criação dos usuários ao `UserFactory`, criando os tipos específicos de usuários, como `Student`, `Teacher`, ou `SuperUser`, usando os métodos auxiliares de criação de cada tipo de usuário.

   **Exemplo de implementação:**

   ```python
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
   ```

#### **Benefícios do Factory Method no código:**

* **Encapsulamento da criação de objetos:** A lógica de criação dos objetos `Student`, `Teacher`, e `SuperUser` está centralizada na classe `UserFactory`, o que facilita a manutenção e a extensão do código (por exemplo, adicionar um novo tipo de usuário no futuro).
* **Desacoplamento:** O restante do código não precisa saber como instanciar os objetos. Ele apenas solicita a criação do usuário, e o Factory se encarrega de determinar qual tipo de usuário criar com base no `role`.

---

### **Facade**

O **Facade** é um padrão de design estrutural que oferece uma interface simplificada para um conjunto de interfaces ou subsistemas complexos. Esse padrão visa fornecer uma interface única para interagir com um sistema mais complexo, ocultando a complexidade interna.

#### **Implementação do Facade no seu projeto:**

1. **Classe `UserManager` (Facade):**
   A classe `UserManager` atua como a fachada, simplificando a interação com os diferentes subsistemas de criação, armazenamento e manipulação de usuários. Ela expõe uma interface simples e de alto nível para operações como adicionar, deletar e verificar usuários, sem que o cliente precise lidar diretamente com os detalhes de implementação desses processos.

   **Exemplo de implementação:**

   ```python
   class UserManager:
       def __init__(self, creator, storage):
           self.creator = creator
           self.storage = storage

       def add_user(self, role, username, password, age=None, course=None, paid=None):
           user = self.creator.create_user(role, username, password, age, course, paid)
           if user:
               self.storage.add(user)  # Salva o usuário criado
           else:
               print(f"[ERRO] Falha ao criar usuário com role '{role}'. Verifique os dados.")

       def delete_user(self, username, password):
           if self.storage.remove(username, password):
               print(f"Usuário {username} removido com sucesso.")
           else:
               print(f"[ERRO] Falha ao remover usuário {username}.")
   ```

   A classe `UserManager` simplifica as interações com o armazenamento de usuários (`UserStorage`) e a criação de usuários (`UserCreator`), oferecendo métodos como `add_user` e `delete_user` que fazem o trabalho pesado de interagir com os subsistemas, sem expor sua complexidade ao código que usa a fachada.

#### **Benefícios do Facade no código:**

* **Simplificação da interface:** O cliente (por exemplo, a `FirstView`) interage apenas com o `UserManager`, sem se preocupar com como a criação ou o armazenamento de usuários acontece.
* **Facilidade de uso:** Com o `UserManager`, você pode realizar operações como adicionar ou remover usuários com uma interface simples e de alto nível, enquanto a complexidade dos subsistemas internos é oculta.
* **Encapsulamento da lógica interna:** As interações com o `UserCreator` e `UserStorage` são abstraídas, tornando a interação com o sistema mais intuitiva e menos propensa a erros.

---

### **Resumo Final:**

* **Factory Method:** Usado para centralizar e delegar a criação de diferentes tipos de usuários (como `Student`, `Teacher`, e `SuperUser`) em uma única classe (`UserFactory`), permitindo a criação de usuários sem expor a lógica de implementação.
* **Facade:** A classe `UserManager` atua como uma fachada, simplificando as interações com o processo de criação, armazenamento e manipulação de usuários, proporcionando uma interface unificada e de alto nível para o restante do sistema.
