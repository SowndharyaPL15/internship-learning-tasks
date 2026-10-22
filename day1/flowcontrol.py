# PROGRAM 1: FIZZBUZZ
print("\n===== PROGRAM 1: FIZZBUZZ =====")

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# PROGRAM 2: PRIME NUMBER CHECKER
print("\n===== PROGRAM 2: PRIME CHECKER =====")

number = int(input("Enter a number to check prime: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            print(f"{number} is not a prime number.")
            break
        divisor += 1
    else:
        print(f"{number} is a prime number.")


# PROGRAM 3: PALINDROME CHECKER
print("\n===== PROGRAM 3: PALINDROME CHECKER =====")

def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


# PROGRAM 4: FACTORIAL CALCULATOR
print("\n===== PROGRAM 4: FACTORIAL =====")

def factorial(number):
    if number < 0:
        return None

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


number = int(input("Enter a non-negative integer: "))
answer = factorial(number)

if answer is None:
    print("Factorial is not defined for negative integers.")
else:
    print(f"Factorial of {number} is {answer}")


# PROGRAM 5: MULTIPLICATION TABLE
print("\n===== PROGRAM 5: MULTIPLICATION TABLE =====")

number = int(input("Enter a number for its multiplication table: "))

for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")


# PROGRAM 6: SUM NUMBERS USING WHILE, BREAK AND CONTINUE
print("\n===== PROGRAM 6: SUM OF NUMBERS =====")

number = 0
total = 0

while number < 20:
    number += 1

    if number == 16:
        break

    if number % 3 == 0:
        continue

    total += number

print(f"Sum from 1 to 15, excluding multiples of 3: {total}")


# PROGRAM 7: DEFAULT ARGUMENTS, *ARGS AND **KWARGS
print("\n===== PROGRAM 7: FUNCTION ARGUMENTS =====")

# Default argument
def greet(name="Student"):
    return f"Hello, {name}!"


print(greet())
print(greet("Sowndharya"))


# *args: accepts multiple positional arguments
def calculate_total(*args):
    return sum(args)


print("Total:", calculate_total(10, 20, 30, 40))


def display_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_profile(
    name="Sowndharya",
    department="CSE",
    year=4
)


# PROGRAM 8: NUMBER MENU
print("\n===== PROGRAM 8: NUMBER MENU =====")

def square(number):
    return number * number


def is_even(number):
    return number % 2 == 0


while True:
    print("\n--- NUMBER MENU ---")
    print("1. Find square")
    print("2. Check even or odd")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a number: "))
        print(f"Square: {square(number)}")

    elif choice == "2":
        number = int(input("Enter a number: "))

        if is_even(number):
            print("Even number")
        else:
            print("Odd number")

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")


print("\n===== T04 PRACTICE COMPLETED =====")
