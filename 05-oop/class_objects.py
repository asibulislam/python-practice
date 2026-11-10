# #Student Management System
# class Student:
#     def __init__(self, name, student_id, age, CGPA):
#         self.name = name
#         self.student_id = student_id
#         self.age = age
#         self.CGPA = CGPA


#     def display_student_info(self):
#         print(f"Name: {self.name}")
#         print(f"Student ID: {self.student_id}")
#         print(f"Age: {self.age}")
#         print(f"CGPA: {self.CGPA}")

#     def validation_cgpa(self):
#        if self.CGPA > 3.50:
#            print(f"{self.name} is an Excellent Student and eligible for Scholarship")
#        else:
#             print(f"{self.name} Needs Improvement and is not eligible for Scholarship")

# s1 = Student("John Doe", "S12345", 20, 3.8)
# s1.display_student_info()
# s1.validation_cgpa()

# s2 = Student("Asibul", "S12346", 21, 3.2)
# s2.display_student_info()
# s2.validation_cgpa()



# # Bank Account Management System
# class BankAccount:
#     def __init__(self, account_holder, account_number, balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient balance.")

#     def display_account_info(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Balance: {self.balance}")

# c1 = BankAccount("Alice Smith", "A123456", 1000)
# c1.display_account_info()
# c1.deposit(500)
# c1.withdraw(200)
# c1.display_account_info()
# print("\n")
# c2 = BankAccount("Bob Johnson", "B654321", 1500)
# c2.display_account_info()
# c2.deposit(1000)
# c2.withdraw(500)
# c2.display_account_info()
# print("\n")
# c3 = BankAccount("Asibul", "C789012", 2000)
# c3.display_account_info()
# c3.deposit(199999)
# c3.withdraw(500)
# c3.display_account_info()

# print("\n")

# c4 = BankAccount("John Doe", "D345678", 3000)
# c4.display_account_info()
# c4.deposit(-5599)
# c4.withdraw(-209)
# c4.display_account_info()

# # Rectangle Calculator

# class Rectangle:
#     def __init__(self, length, width):
#         if length <= 0:
#             raise ValueError("Length must be a positive value.")

#         if width <= 0:
#             raise ValueError("Width must be a positive value.")

#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

#     def is_square(self):
#         return self.length == self.width


# case1 = Rectangle(10, 5)

# print(f"Area: {case1.area()}")
# print(f"Perimeter: {case1.perimeter()}")

# if case1.is_square():
#     print("This rectangle is a square.")
# else:
#     print("This rectangle is not a square.")

# # Employee Salary Calculator
# class Employee:
#     def __init__(self, name, employee_id, monthly_salary):
#         if monthly_salary <= 0:
#             raise ValueError("Monthly salary must be a positive value.")
#         self.name = name
#         self.employee_id = employee_id
#         self.monthly_salary = monthly_salary

#     def annual_salary(self):
#         return self.monthly_salary * 12

#     def salary_increment(self, percentage):
#         if percentage <= 0:
#             raise ValueError("Percentage increase must be a positive value.")
#         self.monthly_salary += self.monthly_salary * (percentage / 100)
#         return self.monthly_salary

#     def display_employee_info(self):
#         return f"Name: {self.name}, Employee ID: {self.employee_id}, Monthly Salary: {self.monthly_salary}"
    
# e1 = Employee("Alice Johnson", "E12345", 3000)

# print(e1.display_employee_info())
# print(f"Annual Salary: {e1.annual_salary()}")
# print(f"New Monthly Salary after 10% increase: {e1.salary_increment(10)}")


# print("\n")

# e2 = Employee("Bob Smith", "E67890", 4000)
# print(e2.display_employee_info())
# print(f"Annual Salary: {e2.annual_salary()}")
# print(f"New Monthly Salary after 15% increase: {e2.salary_increment(15)}")

# # Book Management System
# class Book:
#     def __init__(self, title, author, price, is_available):
#         if price <= 0:
#             raise ValueError("Price must be a positive value.")
        
#         self.title = title
#         self.author = author
#         self.price = price
#         self.is_available = is_available

#     def display_book_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
#         print(f"Availability: {'Available' if self.is_available else 'Not Available'}")

#     def borrow_book(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"You have borrowed '{self.title}'.")
#         else:
#             print(f"Sorry, '{self.title}' is currently not available.")
    
#     def return_book(self):
#         if not self.is_available:
#             self.is_available = True
#             print(f"You have returned '{self.title}'.")
#         else:
#             print(f"'{self.title}' was not borrowed.")

# book1 = Book("Atomic Habits", "James Clear", 500, True)
# book2 = Book("Deep Work", "Cal Newport", 650, True)

# book1.display_book_info()
# book1.borrow_book()
# book1.display_book_info
# book1.display_book_info()
# book1.return_book()
# book1.return_book()
# book1.display_book_info()


# # Library Management System
# class Book:
#     def __init__(self, title, author, publication_year, is_available):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.is_available = is_available

#     def display_book_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Publication Year: {self.publication_year}")
#         print(f"Availability: {'Available' if self.is_available else 'Not Available'}")
#         print()

#     def borrow_book(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"You have borrowed '{self.title}'.")
#         else:
#             print(f"Sorry, '{self.title}' is currently not available.")

#     def return_book(self):
#         if not self.is_available:
#             self.is_available = True
#             print(f"You have returned '{self.title}'.")
#         else:
#             print(f"'{self.title}' was not borrowed.")


# class Library:
#     def __init__(self, library_name, books=None):
#         self.library_name = library_name
#         self.books = books if books is not None else []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Book '{book.title}' added to the library.")

#     def remove_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 print(f"Book '{title}' removed from the library.")
#                 return
#         print(f"Book '{title}' not found in the library.")

#     def display_books(self):
#         print(f"Books in {self.library_name}:")
#         for book in self.books:
#             book.display_book_info()

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 book.borrow_book()
#                 return
#         print(f"Book '{title}' not found in the library.")

#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 book.return_book()
#                 return
#         print(f"Book '{title}' is not borrowed from the library.")


# city_library = Library("City Library")

# # Add books
# city_library.add_book(Book("Atomic Habits", "James Clear", 2018, True))
# city_library.add_book(Book("Clean Code", "Robert C. Martin", 2008, True))
# city_library.add_book(Book("Deep Work", "Cal Newport", 2016, True))

# # View all books
# city_library.display_books()

# # Borrow a book
# city_library.borrow_book("Atomic Habits")   # Borrowed successfully
# city_library.borrow_book("Atomic Habits")   # Not available, already borrowed
# city_library.borrow_book("Unknown Book")    # Not in library

# # Return a book
# city_library.return_book("Atomic Habits")   # Returned successfully
# city_library.return_book("Atomic Habits")   # Was not borrowed

# # Remove a book
# city_library.remove_book("Deep Work")       # Removed
# city_library.remove_book("Deep Work")       # Not found, already removed

# # Final state
# city_library.display_books()

#Shopping Cart System
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
