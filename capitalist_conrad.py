"""Volatile stock-price simulator with day count and file output."""
import random

# Tunable constants (per the brief's later changes)
INITIAL_PRICE = 10.0
MIN_PRICE = 1.0
MAX_PRICE = 100.0
MAX_INCREASE = 0.175   # up to 17.5%
MAX_DECREASE = 0.05    # up to 5%
FILENAME = "conrad_output.txt"


def main():
    """Simulate daily price changes until it exits the bounds; write to a file."""
    price = INITIAL_PRICE
    day = 0

    with open(FILENAME, "w") as out_file:
        print(f"Starting price: ${price:,.2f}", file=out_file)
        while MIN_PRICE <= price <= MAX_PRICE:
            day += 1
            if random.randint(0, 1) == 1:
                price *= (1 + random.uniform(0, MAX_INCREASE))
            else:
                price *= (1 - random.uniform(0, MAX_DECREASE))
            print(f"On day {day} price is: ${price:,.2f}", file=out_file)


if __name__ == "__main__":
    main()
