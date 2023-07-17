MENU = "i", "ii", "iii", "iv"
print(*MENU, sep="\n")
menu_choice = input(">>> ")
while menu_choice != "iv":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if menu_choice == "i":
        for i in range(first_number, second_number+1):
            if i % 2 == 0:
                print(i)
    elif menu_choice == "ii":
        for i in range(first_number, second_number+1):
            if i % 2 != 0:
                print(i)
    elif menu_choice == "iii":
        pass
    else:
        print("Invalid choice")

print("Goodbye.")