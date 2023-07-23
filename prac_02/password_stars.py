"""
CP1404 - Practical 2
"""

MINIMUM_LENGTH = 5

def main():
	"""Password checking program"""
	password = get_password()
	print_asterisks(password)


def print_asterisks(password):
	"""Print asterisks based on length of password"""
	print(len(password) * "*")


def get_password():
	"""Get password and check length"""
	password = input("Enter password: ")
	while len(password) < MINIMUM_LENGTH:
		print("Use a longer password")
		password = input("Enter password: ")
	return password


main()