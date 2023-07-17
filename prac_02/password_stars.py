MINIMUM_LENGTH = 5

def main():
	password = get_password()
	print_asterisks(password)


def print_asterisks(password):
	print(len(password) * "*")


def get_password():
	password = input("Enter password: ")
	while len(password) < MINIMUM_LENGTH:
		print("Use a longer password")
		password = input("Enter password: ")
	return password


main()