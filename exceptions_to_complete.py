"""Get an integer safely; demonstrate try/except and a final result."""

def main():
    is_valid = False
    while not is_valid:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            result = numerator / denominator
            is_valid = True
        except ValueError:
            print("Numerator and denominator must be valid integers!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
    print(f"Result is {result:.2f}")
    print("Finished.")


if __name__ == "__main__":
    main()
