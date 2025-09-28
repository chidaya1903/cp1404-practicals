"""
Calculate and display a user's bonus based on sales.
< $1000 -> 10%   |   >= $1000 -> 15%
Repeats until a negative number is entered.
"""
LOW_RATE = 0.10
HIGH_RATE = 0.15
THRESHOLD = 1000

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        rate = HIGH_RATE if sales >= THRESHOLD else LOW_RATE
        print(f"Bonus: ${sales * rate:.2f}")
        sales = float(input("Enter sales: $"))
    print("Goodbye.")

if __name__ == "__main__":
    main()
