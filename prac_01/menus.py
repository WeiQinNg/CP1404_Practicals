MENU = "(H)ello", "(G)oodbye", "(Q)uit"

name = input("Enter name: ")
print(*MENU, sep="\n")
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid choice")
    print(*MENU, sep="\n")
    menu_choice = input(">>> ").upper()
print("Finished.")