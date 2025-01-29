### Patrones de diseño: singleton
"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""
# Método heredado de Java

class Class:
    
    __instance : None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance= super(Class, cls).__new__(cls)

        return cls.__instance


# Singleton como decorador (forma más pythonica)

def Singleton(cls):
    
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls]= cls(*args, **kwargs)
        return instances[cls]
    
    return wrap



"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class UserSession:

    __instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(UserSession, cls).__new__(cls)
        return cls.__instance

    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email}"

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

session1 = UserSession()
print(session1.get_user())
session1.set_user(2, 'RafaPro', 'Rafa', 'rafita@ono.com')
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())
