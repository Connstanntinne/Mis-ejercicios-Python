### SOLID: Principio de Responsabilidad Única
"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_person(self):
        print(f"Me llamo {self.name} {self.surname}.")

print("----------------")
### Principio SOLID 1
class PersonSolid:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class PrintPersonSolid(PersonSolid):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def print_person2(self):
        print(f"Me llamo {self.name} {self.surname}.")


person1 = Person("Oscar", "Ramirez")
person1.print_person()

person2 = PersonSolid("Anibal", "Ramirez")
print_person2 = PrintPersonSolid("Anibal", "Ramirez")
print_person2.print_person2()


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
"""
### sin SOLID
class Library:
    def __init__(self):
        self.books = []
        self. users = []
        self.loan_register = []


    def book_register(self, title: str, author: str, copies: int):
        self.books.append({"Title": title, "Author": author, "Capies": copies})
  

    def user_register(self, name : str, id: int, email: str):
        self.users.append({"Name": name, "ID": id, "email": email})
    

    def book_loan(self, id, title):
        
        for book in self.books:
            if book["Title"] == title and book["Copies"] > 0:
                book["Copies"] -= 1
                self.loan_register.append({"ID": id, "Title": title})
                return True
            
        return False

        
    def book_return(self, id, title):

        for loan in self.loan_register:
            if loan["ID"] == id and loan["Title"] == title:
                self.loan_register.remove(loan)
                for book in self.books:
                    if book["Title"] == title:
                        book["Copies"] += 1
                    return True
                    
        return False

### Con SOLID

class Book:
    def __init__(self, title: str, author: str, copies: int):
        self.titile = title
        self.author = author
        self.copies = copies
        self.books = []

class User:
    def __init__(self, name : str, id: int, email: str):
        self.name = name
        self.id = id
        self.email = email
        self.users = []


class Loans:
    def __init__(self):
        self.loans = []

    def book_loan(self, user, book): 
        if book.copies > 0:
            book.copies -= 1
            self.loans.append({"ID": user.id, "Title": book.title})
            return True
            
        return False
    
    
    def book_return(self, user, book):
        for loan in self.loans:
            if loan["ID"] == id and loan["Title"] == title:
                self.loans.remove(loan)
                book.copies += 1
                return True
                    
        return False


class Library:

    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.loan_book(user, book)
        return False

    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.return_book(user, book)
        return False
