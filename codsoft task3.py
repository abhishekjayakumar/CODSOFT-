import json
import getpass
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt the password
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode())

# Function to decrypt the password
def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password).decode()

# Function to save credentials to a file
def save_credentials(credentials):
    with open('credentials.json', 'w') as file:
        json.dump(credentials, file)

# Function to load credentials from a file
def load_credentials():
    try:
        with open('credentials.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to add a new credential
def add_credential():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    encrypted_password = encrypt_password(password)
    credentials[website] = {'username': username, 'password': encrypted_password}
    save_credentials(credentials)
    print("Credential added successfully!")

# Function to retrieve a password
def retrieve_password():
    website = input("Enter website: ")
    if website in credentials:
        username = credentials[website]['username']
        encrypted_password = credentials[website]['password']
        password = decrypt_password(encrypted_password)
        print(f"Username: {username}, Password: {password}")
    else:
        print("Website not found in credentials.")

# Main function
def main():
    global credentials
    credentials = load_credentials()
    while True:
        print("\n1. Add a new credential")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_credential()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
