# import math 

# print ( math . sqrt(4096))

# marks = [90,54,56,65,45]

# print(marks[2:4])

# marks= [5,10,56,29,45]

# extra_marks = [53,26,59,65]


# print(marks)
# # marks.append(60)
# print(marks)
# # marks.pop()

# marks.extend(extra_marks)

# print(marks)


# a = 5
# table = []

# for i in range(1,11):
#     table.append(5*i)



# print(table)



# Employee inheritance structure


class Employee:

    def show(self):
        print("Employee")


class Developer(Employee):

    def show(self):
        print("Developer")


class Manager(Employee):

    def show(self):
        print("Manager")


class PythonDeveloper(Developer):

    def show(self):
        print("Python Developer")


employee = Employee()
developer = Developer()
manager = Manager()
python_developer = PythonDeveloper()

employee.show()
developer.show()
manager.show()
python_developer.show()


#Shape runtime polymorphism

class Shape:

    def area(self):
        print("Area of shape")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 4)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    print(shape.area())



# Operator overloading - student 



class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

    def __gt__(self, other):
        return self.marks > other.marks


student1 = Student("Aditya", 80)
student2 = Student("Rahul", 70)

print("Total marks:", student1 + student2)

if student1 > student2:
    print("Student 1 has higher marks")
else:
    print("Student 2 has higher marks")



# Operator overloading - book 



class Book:

    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __eq__(self, other):
        return self.price == other.price


book1 = Book("Python", 500, 300)
book2 = Book("Java", 600, 400)

print("Book 1 has fewer pages:", book1 < book2)

print("Both books have same price:", book1 == book2)



# Employee company system 

class Employee:

    company_name = "ABC Company"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Company:", Employee.company_name)

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def validate_employee_id(employee_id):

        if employee_id > 0:
            return True
        else:
            return False


employee1 = Employee("Aditya", 101)

employee1.display_details()

Employee.change_company_name("XYZ Company")

employee1.display_details()

print("Valid ID:", Employee.validate_employee_id(101))



# Library and  books object relationship


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed.")
        else:
            print("Book not found.")

    def display_books(self):

        print("\nBooks in Library:")

        for book in self.books:
            book.display_book()


book1 = Book("Python Basics", "Author 1")
book2 = Book("Java Basics", "Author 2")
book3 = Book("C++ Basics", "Author 3")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.remove_book(book2)

library.display_books()



852.  


