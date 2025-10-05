"""Exceptions demo with answers and a safe change to avoid ZeroDivisionError."""

def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        # Guard against division by zero by validating:
        while denominator == 0:
            print("Cannot divide by zero.")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
    except ValueError:
        print("Numerator and denominator must be valid integers!")
    else:
        print(f"{numerator} / {denominator} = {fraction}")
    print("Finished.")


if __name__ == "__main__":
    main()

# Questions (answers in comments):
# 1) When will a ValueError occur?
#    -> When the user enters something that cannot be converted to an integer
#       for numerator or denominator (e.g., letters, blank, 3.5).
# 2) When will a ZeroDivisionError occur?
#    -> When the denominator is 0 at the moment of performing the division
#       (e.g., numerator / 0), if we don’t guard against it.
# 3) Could you change the code to avoid the possibility of a ZeroDivisionError?
#    -> Yes. Validate the denominator and re-prompt until it is not zero
#       (while denominator == 0: ask again), or catch ZeroDivisionError and ask again
#       before attempting the division. Implemented above with a simple loop.
