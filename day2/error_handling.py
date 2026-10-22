def divide_numbers(first_number, second_number):
    """Divide two numbers after validating the divisor."""

    if second_number == 0:
        raise ValueError("The divisor cannot be zero.")

    return first_number / second_number
try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))

    result = divide_numbers(first, second)

except ValueError as error:
    print("Input error:", error)

else:
    print(f"Result: {result:.2f}")

finally:
    print("Division program finished.")
