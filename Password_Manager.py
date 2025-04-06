import getpass
import hashlib
import os

class PasswordManager:
    def __init__(self):
        self.data = {}
        self.username = None
        self.password = None

    def create_account(self):
        self.username = input("Enter a unique username: ")
        while True:
            self.password = getpass.getpass("Enter a password: ")
            confirm_password = getpass.getpass("Confirm password: ")
            if self.password == confirm_password:
                hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
                self.data[self.username] = hashed_password
                break
            else:
                print("Passwords do not match. Please try again.")

    def add_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.data[self.username] = hashed_password

    def get_password(self):
        if self.username is not None:
            return self.data[self.username]
        else:
            return None

    def delete_password(self):
        if self.username is not None:
            del self.data[self.username]
        else:
            print("You must create an account first.")

    def view_passwords(self):
        if self.username is not None:
            print(self.data)
        else:
            print("You must create an account first.")

    def login(self):
        while True:
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if username in self.data and self.data[username] == hashed_password:
                self.username = username
                break
            else:
                print("Invalid username or password. Please try again.")

def main():
    manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Add Password")
        print("4. Get Password")
        print("5. Delete Password")
        print("6. View Passwords")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.create_account()
        elif choice == "2":
            manager.login()
        elif choice == "3":
            if manager.username is not None:
                password = getpass.getpass("Enter a password: ")
                manager.add_password(password)
            else:
                print("You must login first.")
        elif choice == "4":
            if manager.username is not None:
                password = manager.get_password()
                if password:
                    print("Password:", password)
                else:
                    print("You must add a password first.")
            else:
                print("You must login first.")
        elif choice == "5":
            if manager.username is not None:
                manager.delete_password()
            else:
                print("You must login first.")
        elif choice == "6":
            manager.view_passwords()
        elif choice == "7":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()