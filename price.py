def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage (e.g., 10 for 10%).

    Returns:
        float: The final price after discount, or the original price if
               the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

if __name__ == "__main__":
    try:
        original_price_str = input("Enter the original price of the item: ")
        original_price = float(original_price_str)

        discount_percentage_str = input("Enter the discount percentage (e.g., 10): ")
        discount_percentage = float(discount_percentage_str)

        final_price = calculate_discount(original_price, discount_percentage)

        print(f"\nOriginal Price: ${original_price:.2f}")
        if discount_percentage >= 20:
            print(f"Discount Applied: {discount_percentage:.2f}%")
            print(f"Final Price: ${final_price:.2f}")
        else:
            print("No discount applied.")
            print(f"Final Price: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")