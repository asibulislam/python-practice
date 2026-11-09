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
book1.display_book_info
book1.display_book_info()
book1.return_book()
book1.return_book()
book1.display_book_info()

