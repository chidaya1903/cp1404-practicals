"""
Very simple menu-driven greeting program.
(H)ello, (G)oodbye, (Q)uit
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"

def main():
    name = input("Enter name: ").strip()
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Finished.")

if __name__ == "__main__":
    main()
