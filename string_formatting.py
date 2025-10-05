"""String formatting walkthrough + tasks."""

# Task 1: f-string to match the exact output
instrument = "Gibson L-5 CES"
year = 1922
approx_price = 16036  # rounded to the nearest whole dollar
print(f"{year} {instrument} for about ${approx_price:,.0f}!")

# Task 2: right-aligned powers table (no list; use range and f-strings)
for i in range(0, 11):
    print(f"2 ^ {i:>2} is {2 ** i:>4}")
