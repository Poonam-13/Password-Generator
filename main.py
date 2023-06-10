import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def save_password(username, password):
    with open('passwords.txt', 'a') as file:
        file.write(f'{username}:{password}\n')


def get_password(username):
    with open('passwords.txt', 'r') as file:
        for line in file:
            if line.startswith(username + ':'):
                return line.split(':')[1].strip()


def main():
    while True:
        print("\n--- Password Generator and Manager ---")
        print("1. Generate a password")
        print("2. Save a password")
        print("3. Get a password")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            length = int(input("Enter the length of the password: "))
            password = generate_password(length)
            print("Generated password:", password)
        elif choice == '2':
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(username, password)
            print("Password saved successfully!")
        elif choice == '3':
            username = input("Enter the username: ")
            password = get_password(username)
            if password:
                print("Password:", password)
            else:
                print("Password not found!")
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()
