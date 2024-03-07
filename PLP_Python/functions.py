def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    return_price = ((100 - discount_percent)/100) * price
    return (return_price)
  return price

price = float(input("Please enter the original price: "))
discount = float(input("Please enter the discount percentage: "))

final_price = calculate_discount(price, discount)

print(f"You will pay {final_price}")