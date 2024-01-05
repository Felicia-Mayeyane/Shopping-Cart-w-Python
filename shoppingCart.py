foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy: (q to quit)")
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)

print("----YOUR SHOPPING CART----")

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price
print()
print(f"Your Total price is R{total}")