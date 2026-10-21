# Program 1: Basic Calculator
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
difference = num1 - num2
product = num1 * num2

print(f"Sum: {total:.2f}")
print(f"Difference: {difference:.2f}")
print(f"Product: {product:.2f}")

if num2 != 0:
    print(f"Division: {num1 / num2:.2f}")
else:
    print("Division by zero is not allowed.")"""
    
# Program 2: Temperature Converter
"""
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Celsius: {celsius:.1f}°C")
print(f"Fahrenheit: {fahrenheit:.1f}°F")"""

# Program 3: Name Formatter
"""
name = input("Enter your full name: ").strip()

print(f"Original name: {name}")
print(f"Title case: {name.title()}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Characters: {len(name)}")"""

# Program 4: Student Marks Calculator
"""
name = input("Enter student name: ").strip().title()

mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))

total = mark1 + mark2 + mark3
average = total / 3

passed = mark1 >= 40 and mark2 >= 40 and mark3 >= 40

print(f"Student: {name}")
print(f"Total: {total:.2f} / 300")
print(f"Average: {average:.2f}")
print(f"Passed all subjects: {passed}")"""

# Program 5: Shopping Bill
"""
item = input("Enter item name: ").strip().title()
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Item: {item}")
print(f"Price: Rs. {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total bill: Rs. {total:.2f}")"""

# Program 6: Voting Eligibility Checker
"""
age = int(input("Enter your age: "))

eligible = age >= 18

print(f"Age: {age}")
print(f"Eligible to vote: {eligible}")"""

# Program 7: Email Username Extractor
"""
email = input("Enter your email: ").strip().lower()

if "@" in email:
    username = email.split("@", 1)[0]
    print(f"Email: {email}")
    print(f"Username: {username}")
else:
    print("Please enter an email containing @.")"""

# Program 8: Discount Calculator
"""
price = float(input("Enter product price: Rs. "))
discount = float(input("Enter discount percentage: "))

savings = price * discount / 100
final_price = price - savings

print(f"Original price: Rs. {price:.2f}")
print(f"Savings: Rs. {savings:.2f}")
print(f"Final price: Rs. {final_price:.2f}")"""

# Program 9: Message Analyzer
"""
message = input("Enter a message: ").strip()

characters = len(message)
words = len(message.split())
contains_python = "python" in message.lower()

print(f"Message: {message}")
print(f"Characters: {characters}")
print(f"Words: {words}")
print(f"Contains Python: {contains_python}")"""

# Program 10: Student Profile Generator

name = input("Enter your name: ").strip().title()
department = input("Enter department: ").strip().upper()
year = int(input("Enter study year: "))
cgpa = float(input("Enter CGPA (0-10): "))

valid_cgpa = 0 <= cgpa <= 10

print("\n--- STUDENT PROFILE ---")
print(f"Name: {name}")
print(f"Department: {department}")
print(f"Study year: {year}")
print(f"CGPA: {cgpa:.2f}")
print(f"Valid CGPA: {valid_cgpa}")