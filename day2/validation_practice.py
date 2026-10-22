def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount

    return round(final_price, 2)


try:
    price = float(input("Enter product price: "))
    discount = float(input("Enter discount percentage: "))

    final_price = calculate_discount(price, discount)

except ValueError as error:
    print("Invalid input:", error)

else:
    print(f"Final price: Rs. {final_price:.2f}")

finally:
    print("Discount calculation completed.")
