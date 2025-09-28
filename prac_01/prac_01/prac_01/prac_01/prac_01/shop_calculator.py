"""
Shop calculator: ask for number of items and each price,
apply 10% discount if total > $100, then display total to 2 dp.
Includes input validation.
"""
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.10

def main():
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total = 0.0
    for _ in range(number_of_items):
        total += float(input("Price of item: "))

    if total > DISCOUNT_THRESHOLD:
        total -= total * DISCOUNT_RATE

    print(f"Total price for {number_of_items} items is ${total:.2f}")

if __name__ == "__main__":
    main()
