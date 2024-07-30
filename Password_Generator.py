import random
import string
class PasswordGenerator:
    def __init__(self):
        self.password_length = 0
        self.password = ""
    def get_user_input(self):
        while True:
            try:
                self.password_length = int(input("Enter the desired length for the password: "))
                if self.password_length <= 0:
                    raise ValueError("Password length must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        try:
            if self.password_length == 0:
                raise Exception("Password length not set. Please provide a valid length.")
            self.password = ''.join(random.choice(characters) for _ in range(self.password_length))
        except Exception as e:
            print(f"Error generating password: {e}")
        finally:
            if not self.password:
                self.password = "Default@1234"  # Setting a default password in case of error
    def display_password(self):
        try:
            if not self.password:
                raise Exception("No password generated.")
            print(f"Generated Password: {self.password}")
        except Exception as e:
            print(f"Error: {e}")
def main():
    pg = PasswordGenerator()
    pg.get_user_input()
    pg.generate_password()
    pg.display_password()
if __name__ == "__main__":
    main()
