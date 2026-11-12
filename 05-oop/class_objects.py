#Student Management System
class Student:
    def __init__(self, name, student_id, age, CGPA):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.CGPA = CGPA


    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"CGPA: {self.CGPA}")

    def validation_cgpa(self):
       if self.CGPA > 3.50:
           print(f"{self.name} is an Excellent Student and eligible for Scholarship")
       else:
            print(f"{self.name} Needs Improvement and is not eligible for Scholarship")

s1 = Student("John Doe", "S12345", 20, 3.8)
s1.display_student_info()
s1.validation_cgpa()

s2 = Student("Asibul", "S12346", 21, 3.2)
s2.display_student_info()
s2.validation_cgpa()



# Bank Account Management System
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

c1 = BankAccount("Alice Smith", "A123456", 1000)
c1.display_account_info()
c1.deposit(500)
c1.withdraw(200)
c1.display_account_info()
print("\n")
c2 = BankAccount("Bob Johnson", "B654321", 1500)
c2.display_account_info()
c2.deposit(1000)
c2.withdraw(500)
c2.display_account_info()
print("\n")
c3 = BankAccount("Asibul", "C789012", 2000)
c3.display_account_info()
c3.deposit(199999)
c3.withdraw(500)
c3.display_account_info()

print("\n")

c4 = BankAccount("John Doe", "D345678", 3000)
c4.display_account_info()
c4.deposit(-5599)
c4.withdraw(-209)
c4.display_account_info()

# Rectangle Calculator

class Rectangle:
    def __init__(self, length, width):
        if length <= 0:
            raise ValueError("Length must be a positive value.")

        if width <= 0:
            raise ValueError("Width must be a positive value.")

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width


case1 = Rectangle(10, 5)

print(f"Area: {case1.area()}")
print(f"Perimeter: {case1.perimeter()}")

if case1.is_square():
    print("This rectangle is a square.")
else:
    print("This rectangle is not a square.")

# Employee Salary Calculator
class Employee:
    def __init__(self, name, employee_id, monthly_salary):
        if monthly_salary <= 0:
            raise ValueError("Monthly salary must be a positive value.")
        self.name = name
        self.employee_id = employee_id
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def salary_increment(self, percentage):
        if percentage <= 0:
            raise ValueError("Percentage increase must be a positive value.")
        self.monthly_salary += self.monthly_salary * (percentage / 100)
        return self.monthly_salary

    def display_employee_info(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}, Monthly Salary: {self.monthly_salary}"
    
e1 = Employee("Alice Johnson", "E12345", 3000)

print(e1.display_employee_info())
print(f"Annual Salary: {e1.annual_salary()}")
print(f"New Monthly Salary after 10% increase: {e1.salary_increment(10)}")


print("\n")

e2 = Employee("Bob Smith", "E67890", 4000)
print(e2.display_employee_info())
print(f"Annual Salary: {e2.annual_salary()}")
print(f"New Monthly Salary after 15% increase: {e2.salary_increment(15)}")

# Book Management System
class Book:
    def __init__(self, title, author, price, is_available):
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        
        self.title = title
        self.author = author
        self.price = price
        self.is_available = is_available

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Availability: {'Available' if self.is_available else 'Not Available'}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

book1 = Book("Atomic Habits", "James Clear", 500, True)
book2 = Book("Deep Work", "Cal Newport", 650, True)

book1.display_book_info()
book1.borrow_book()
book1.display_book_info()
book1.display_book_info()
book1.return_book()
book1.return_book()
book1.display_book_info()


# Library Management System
class Book:
    def __init__(self, title, author, publication_year, is_available):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = is_available

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Availability: {'Available' if self.is_available else 'Not Available'}")
        print()

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")


class Library:
    def __init__(self, library_name, books=None):
        self.library_name = library_name
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_books(self):
        print(f"Books in {self.library_name}:")
        for book in self.books:
            book.display_book_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow_book()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' is not borrowed from the library.")


city_library = Library("City Library")


city_library.add_book(Book("Atomic Habits", "James Clear", 2018, True))
city_library.add_book(Book("Clean Code", "Robert C. Martin", 2008, True))
city_library.add_book(Book("Deep Work", "Cal Newport", 2016, True))


city_library.display_books()

city_library.borrow_book("Atomic Habits")  
city_library.borrow_book("Atomic Habits")  
city_library.borrow_book("Unknown Book")   


city_library.return_book("Atomic Habits")   
city_library.return_book("Atomic Habits")   

city_library.remove_book("Deep Work")      
city_library.remove_book("Deep Work")       

city_library.display_books()

# Shopping Cart System
class Product:
    def __init__(self,name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def display_product_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Product ID: {self.product_id}"

class ShoppingCart:
    def __init__(self, products=None, quantity=None):
        self.products = products if products is not None else []
        self.quantity = quantity if quantity is not None else []


    def add_product(self, product, quantity):
        self.products.append(product)
        self.quantity.append(quantity)
        print(f"Added {quantity} of '{product.name}' to the cart.")

    def remove_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                removed_product = self.products.pop(i)
                removed_quantity = self.quantity.pop(i)
                print(f"Removed {removed_quantity} of '{removed_product.name}' from the cart price {removed_product.price * removed_quantity}.")
                return
        print(f"Product with ID '{product_id}' not found in the cart.")

    def update_quantity(self, product_id, new_quantity):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.quantity[i] = new_quantity
                print(f"Updated quantity of '{product.name}' to {new_quantity}.")
                return
        print(f"Product with ID '{product_id}' not found in the cart.")


    def calculate_total(self):
        total = 0
        for i, product in enumerate(self.products):
            total += product.price * self.quantity[i]
        return total
    

    def apply_discount(self, discount_code):
        discount_codes = {
            "SAVE10": 0.10,
            "SAVE20": 0.20,
            "SAVE30": 0.30,
            "SAVE40": 0.40,
            "SAVE50": 0.50, 
            "SAVE60": 0.60,
            "SAVE70": 0.70,
            "SAVE80": 0.80,
            "SAVE90": 0.90,
            "SAVE100": 1.00
        }
        if discount_code in discount_codes:
            discount_percentage = discount_codes[discount_code]
            total_price = self.calculate_total()
            discounted_price = total_price * (1 - discount_percentage)
            print(f"Discount code '{discount_code}' applied. Before discount: {total_price}, After discount: {discounted_price}")
        else:
            print(f"Invalid discount code '{discount_code}'.")


    def display_cart(self):
        print("Shopping Cart:")
        for i, product in enumerate(self.products):
            print(f"{product.display_product_info()}, Quantity: {self.quantity[i]}")
        print(f"Total Price: {self.calculate_total()}")


shop = ShoppingCart([Product("Laptop", 1000, "P001"), Product("Smartphone", 500, "P002")], quantity=[1, 2])
shop.display_cart()
shop.add_product(Product("Headphones", 100, "P003"), 3)
shop.add_product(Product("Keyboard", 50, "P004"), 2)
shop.display_cart()
shop.remove_product("P002")
shop.update_quantity("P003", 5)
shop.display_cart()
shop.apply_discount("SAVE20")


# temparature Converter

class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")  
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def celsius_to_kelvin(self):
        return self.celsius + 273.15

    def update_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        self.celsius = value
        print(f"Temperature updated to {self.celsius}°C.")

    def display_temperature(self):
        print(f"Temperature: {self.celsius}°C, {self.celsius_to_fahrenheit()}°F, {self.celsius_to_kelvin()}K")

t1 = Temperature(25)
t1.display_temperature()
t1.update_temperature(30)
t1.display_temperature()

t2 = Temperature(-300)  
t2.display_temperature()


#University Course Registration.
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.registered_courses = []

    def register_course(self, course):
        if course not in self.registered_courses:
            self.registered_courses.append(course)
            return True
        return False

    def display_student_info(self):
        print(f"Name: {self.name}, Student ID: {self.student_id}")
        print("Registered Courses:")
        for course in self.registered_courses:
            print(f"- {course.course_name} ({course.course_code})")


class Course:
    def __init__(self, course_name, course_code, max_students):
        self.course_name = course_name
        self.course_code = course_code
        self.max_students = max_students
        self.registered_students = []

    def is_full(self):
        return len(self.registered_students) >= self.max_students

    def add_student(self, student):
        if student in self.registered_students or self.is_full():
            return False
        self.registered_students.append(student)
        return True

    def remove_student(self, student):
        if student in self.registered_students:
            self.registered_students.remove(student)
            if self in student.registered_courses:
                student.registered_courses.remove(self)
            print(f"{student.name} has been removed from {self.course_name}.")
        else:
            print(f"{student.name} is not registered for {self.course_name}.")

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Course Code: {self.course_code}, Max Students: {self.max_students}")
        print("Registered Students:")
        for i, student in enumerate(self.registered_students, start=1):
            print(f"{i}. {student.name}")


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []
        self.courses = []

    def _find_student(self, student_id):
        return next((s for s in self.students if s.student_id == student_id), None)

    def _find_course(self, course_code):
        return next((c for c in self.courses if c.course_code == course_code), None)

    def add_student(self, student):
        if self._find_student(student.student_id):
            print(f"Student ID {student.student_id} already exists.")
            return
        self.students.append(student)
        print(f"Student added: {student.name}")

    def add_course(self, course):
        if self._find_course(course.course_code):
            print(f"Course code {course.course_code} already exists.")
            return
        self.courses.append(course)
        print(f"Course added: {course.course_name}")

    def register_student(self, student_id, course_code):
        student = self._find_student(student_id)
        course = self._find_course(course_code)

        if not student:
            print(f"Student with ID {student_id} not found.")
            return
        if not course:
            print(f"Course with code {course_code} not found.")
            return
        if student in course.registered_students:
            print("Already registered!")
            return
        if course.is_full():
            print(f"Cannot register {student.name}. {course.course_name} is full.")
            return

        course.add_student(student)
        student.register_course(course)
        print("Registration successful!")

    def display_registered_students(self, course_code):
        course = self._find_course(course_code)
        if course:
            course.display_course_info()
        else:
            print(f"Course with code {course_code} not found.")

    def display_available_seats(self, course_code):
        course = self._find_course(course_code)
        if course:
            seats = course.max_students - len(course.registered_students)
            print(f"Available Seats: {seats}")
        else:
            print(f"Course with code {course_code} not found.")


# Test with the example
uni = University("First Capital University")

alice = Student("Alice", 1)
bob = Student("Bob", 2)
uni.add_student(alice)
uni.add_student(bob)
uni.add_student(Student("Fake Alice", 1))      

python = Course("Python Programming", "CSE101", 30)
uni.add_course(python)
uni.add_course(Course("Duplicate", "CSE101", 5))  

print("\nRegistering Alice...")
uni.register_student(1, "CSE101")
print("Registering Alice again...")
uni.register_student(1, "CSE101")
print("Registering Bob...")
uni.register_student(2, "CSE101")
uni.register_student(99, "CSE101")             
uni.register_student(1, "XXX")                 

print()
uni.display_available_seats("CSE101")
print()
uni.display_registered_students("CSE101")


#Employee Management System
class Employee:
    def __init__(self, name, employee_id, base_salary):
        if base_salary <= 0:
            raise ValueError("Base salary must be a positive value.")
        self.name = name
        self.employee_id = employee_id
        
        self.base_salary = base_salary

    def display_info(self):
        print(f"Name: {self.name}, Employee Id: {self.employee_id}, Base Salary: {self.base_salary}")

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language, bonus=0):
        super().__init__(name, employee_id, base_salary)
        self.programming_language = programming_language
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_salary(self):
        return self.base_salary + self.bonus

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, department, allowance=0):
        super().__init__(name, employee_id, base_salary)
        self.department = department
        self.allowance = allowance

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_salary(self):
        return self.base_salary + self.allowance


emp1 = Developer("Alice", "D001", 5000, "Python", bonus=1000)
emp2 = Manager("Bob", "M001", 6000, "IT", allowance=1500)
emp3 = Employee("Charlie", "E001", 4000)
emp4 = Developer("David", "D002", 5500, "Java", bonus=1200)
emp5 = Manager("Eve", "M002", 6500, "HR", allowance=2000)
emp6 = Employee("Frank", "E002", 4500)

employees = [emp1, emp2, emp3, emp4, emp5, emp6]
for emp in employees:
    emp.display_info()
    print(f"Total Salary: {emp.calculate_salary()}")
    print()

#Shape Area Calculator
class Shape:
    def calculate_area(self):
        return 0
    def display_area(self):
        area = self.calculate_area()
        print(f"Area: {area}")


class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0:
            raise ValueError("Length must be a positive value.")
        if width <= 0:
            raise ValueError("Width must be a positive value.")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")

        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0:
            raise ValueError("Base must be a positive value.")
        if height <= 0:
            raise ValueError("Height must be a positive value.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


    
a1 = Rectangle(10, 5)
a2 = Circle(7)
a3 = Triangle(8, 6)
area = [a1, a2, a3]
for a in area:
    a.display_area()


# Bank Account Management System
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Your current balance after deposit: {self.get_balance()}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._max_withdrawable():
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        print(f"Withdrawn: {amount}. Available balance: {self.get_balance()}")
        return self.__balance

    def _max_withdrawable(self):
        return self.__balance

    def get_balance(self):
        return self.__balance

    def describe(self):
        return f"{self.account_holder} ({self.account_number}) | Basic account | Balance: {self.get_balance()}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        if not 0 <= interest_rate <= 100:
            raise ValueError("Interest rate must be between 0 and 100.")
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * (self.interest_rate / 100)

    def describe(self):
        return (f"{self.account_holder} ({self.account_number}) | Savings account | "
                f"Balance: {self.get_balance()} | Interest rate: {self.interest_rate}%")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, overdraft_limit):
        super().__init__(account_holder, account_number, balance)
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.overdraft_limit = overdraft_limit

    def _max_withdrawable(self):
        return self.get_balance() + self.overdraft_limit

    def describe(self):
        return (f"{self.account_holder} ({self.account_number}) | Current account | "
                f"Balance: {self.get_balance()} | Overdraft limit: {self.overdraft_limit}")



accounts = [
    CurrentAccount("Asibul Islam", 1003105, 5000, 20000),
    SavingsAccount("Khalid Mamun", 100512, 50000, 10),
    BankAccount("Amanul Islam", 1002193, 3000),
]

for account in accounts:
    print(account.describe())
    print("-" * 40)

bad_cases = [
    lambda: BankAccount("Test", 1, -100),
    lambda: SavingsAccount("Test", 2, 1000, -5),
    lambda: SavingsAccount("Test", 3, 1000, 150),
    lambda: CurrentAccount("Test", 4, 1000, -2000),
]

for make_account in bad_cases:
    try:
        make_account()
    except ValueError as e:
        print(f"Error: {e}")