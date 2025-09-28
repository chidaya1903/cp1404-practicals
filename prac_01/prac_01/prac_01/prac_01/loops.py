"""
For-loop practice. Keep all parts (a–d) in this file.
"""
# Provided example: odd numbers 1..20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("a. Count in 10s from 0 to 100")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("b. Count down from 20 to 1")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print("c. Print a number of stars on one line")
number_of_stars = int(input("Number of stars: "))
for _ in range(number_of_stars):
    print("*", end='')
print()

print("d. Print lines of increasing stars")
number_of_lines = int(input("Number of lines: "))
for i in range(1, number_of_lines + 1):
    print("*" * i)
