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

