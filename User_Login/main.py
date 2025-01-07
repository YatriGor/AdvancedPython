import bcrypt
import logging

# Configure logging
logging.basicConfig(filename='usermanagement.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    """Check hashed password."""
    return bcrypt.checkpw(user_password.encode(), hashed_password)

def sign_up():
    """Register a new user."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Hash the password
    hashed = hash_password(password)
    
    # Save user data
    with open('user_Data.txt', 'a') as f:
        f.write(f"{username} {hashed.decode()}\n")
    
    # Log the sign-up
    logging.info(f"User '{username}' signed up successfully.")
    print("Sign up successful.")

def log_in():
    """Log in an existing user."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Read user data file
    try:
        with open('user_Data.txt', 'r') as f:
            users = f.readlines()
    except FileNotFoundError:
        print("No users found. Please sign up first.")
        return

    # Check if user exists and password is correct
    for user in users:
        stored_username, stored_hashed_password = user.split()
        if stored_username == username:
            if check_password(stored_hashed_password.encode(), password):
                logging.info(f"User '{username}' logged in successfully.")
                print("Log in successful.")
                return
            else:
                logging.warning(f"Failed login attempt for user '{username}': Incorrect password.")
                print("Login not successful. Wrong password or username.")
                return

    logging.warning(f"Failed login attempt: User '{username}' not found.")
    print("Login not successful. Wrong password or username.")

def main():
    """Main menu loop."""
    print("USER MANAGEMENT SYSTEM")
    while True:
        print("Menu:\n1. Sign Up\n2. Log in\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            sign_up()
        elif choice == '2':
            log_in()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
