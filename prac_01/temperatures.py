"""
Convert temperatures between Celsius and Fahrenheit.
Menu-driven so you can do multiple conversions.
"""
MENU = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"

def c_to_f(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def main():
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "C":
            c = float(input("Celsius: "))
            print(f"Result: {c_to_f(c):.2f} F")
        elif choice == "F":
            f = float(input("Fahrenheit: "))
            print(f"Result: {f_to_c(f):.2f} C")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Thank you.")

if __name__ == "__main__":
    main()
