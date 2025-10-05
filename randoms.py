"""Random module exploration + answers in comments."""
import random

# Lines to run (execute multiple times to observe the ranges):
print(random.randint(5, 20))        # line 1
print(random.randrange(3, 10, 2))   # line 2
print(random.uniform(2.5, 5.5))     # line 3

# Answers (write them here in code comments):
# Q1 (line 1): randint(5, 20) -> smallest = 5, largest = 20 (both inclusive).
# Q2 (line 2): randrange(3, 10, 2) -> values from {3, 5, 7, 9}; smallest = 3, largest = 9; it CANNOT produce 4.
# Q3 (line 3): uniform(2.5, 5.5) -> any float in [2.5, 5.5]; endpoints are possible in principle.

# Code to produce a random number between 1 and 100 inclusive:
random_1_to_100 = random.randint(1, 100)
print(f"Random 1..100: {random_1_to_100}")
