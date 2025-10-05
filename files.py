"""Files practice: separate parts in one script (labelled)."""

# 1. Write a name to name.txt (use open/close)
print("# 1.")
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and greet (use open/close)
print("# 2.")
in_file = open("name.txt", "r")
stored_name = in_file.read().strip()
in_file.close()
print(f"Hi {stored_name}!")

# 3. Read first two numbers from numbers.txt and print their sum (use with)
print("# 3.")
with open("numbers.txt", "r") as f:
    first = int(f.readline())
    second = int(f.readline())
print(first + second)  # should be 59 for the given numbers: 17 + 42

# 4. Total all numbers in numbers.txt (works for any length; use with + for loop)
print("# 4.")
total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line.strip())
print(total)
