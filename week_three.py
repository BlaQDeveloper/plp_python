def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
    
price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percentage: "))
discount_applied = calculate_discount(price, discount_percent)
if discount_applied != price:
    print(f"The final price after {discount_percent}% discount is: {discount_applied}")
else:
    print(f"The original price is: {price}")