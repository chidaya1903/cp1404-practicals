"""Exceptions demo with simple guard against division by zero."""

def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        # Guard: keep asking until denominator is non-zero.
        while denominator == 0:
            print("Cannot divide by zero.")
            denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Numerator and denominator must be valid integers!")
    else:
        print(f"{numerator} / {denominator} = {result}")
    print("Finished.")


if __name__ == "__main__":
    main()

# Questions (answers):
# 1) When will a ValueError occur?
#    When the input for numerator/denominator is not an integer (e.g. "abc", "", "3.5").
# 2) When will a ZeroDivisionError occur?
#    If we attempt numerator / 0 (before adding the guard).
# 3) How to avoid ZeroDivisionError?
#    Validate and re-prompt until denominator != 0 (as implemented above).
