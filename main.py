import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="banking_system"
)
mycursor = mydb.cursor()

# Function to check if account number and PIN are valid
def check_login(account_number, pin):
    query = "SELECT * FROM users WHERE account_number = %s AND pin = %s"
    values = (account_number, pin)
    mycursor.execute(query, values)
    user = mycursor.fetchone()
    if user:
        return user
    else:
        return None

# Function to check account balance
def check_balance(user):
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    values = (user[2], )
    mycursor.execute(query, values)
    balance = mycursor.fetchone()[0]
    print("Your current balance is: $" + str(balance))

# Function to deposit money into account
def deposit(user, amount):
    query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    values = (amount, user[2])
    mycursor.execute(query, values)
    mydb.commit()
    print("$" + str(amount) + " has been deposited into your account.")

# Function to withdraw money from account
def withdraw(user, amount):
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    values = (user[2], )
    mycursor.execute(query, values)
    balance = mycursor.fetchone()[0]
    if amount > balance:
        print("Insufficient funds.")
    else:
        query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
        values = (amount, user[2])
        mycursor.execute(query, values)
        mydb.commit()
        print("$" + str(amount) + " has been withdrawn from your account.")

# Function to create a new account
def create_account(name, account_number, pin, is_admin=False):
    query = "INSERT INTO users (name, account_number, pin, is_admin) VALUES (%s, %s, %s, %s)"
    values = (name, account_number, pin, is_admin)
    mycursor.execute(query, values)
    mydb.commit()
    query = "INSERT INTO accounts (account_number, balance) VALUES (%s, %s)"
    values = (account_number, 0)
    mycursor.execute(query, values)
    mydb.commit()
    print("Account created successfully.")

# Function to close an account
def close_account(user):
    query = "DELETE FROM users WHERE id = %s"
    values = (user[0], )
    mycursor.execute(query, values)
    mydb.commit()
    query = "DELETE FROM accounts WHERE account_number = %s"
    values = (user[2], )
    mycursor.execute(query, values)
    mydb.commit()
    print("Account closed successfully.")

# Function to modify an account
def modify_account(user, field, value):
    if field == "name":
        query = "UPDATE users SET name = %s WHERE id = %s"
    elif field == "pin":
        query = "UPDATE users SET pin = %s WHERE id = %s"
    else:
        print("Invalid field.")
        return
    values = (value, user[0])
    mycursor.execute(query, values)
    mydb.commit()
    print("Account modified successfully.")

# Main function to run the program
def main():
    print("Welcome to the Online Banking System.")

# Create the necessary tables if they do not exist
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            account_number VARCHAR(255) UNIQUE,
            pin VARCHAR(255),
            is_admin BOOLEAN
        )
    """)
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            account_number VARCHAR(255),
            balance DECIMAL(10,2)
        )
    """)
    mydb.commit()


    while True:
        print("Select an option:")
        print("1. Log in")
        print("2. Sign up")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            # Login
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            user = check_login(account_number, pin)
            if user is None:
                print("Invalid login credentials.")
            else:
                print("Login successful.")
                # Main menu
                while True:
                    print("Select an option:")
                    print("1. Check balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Create account")
                    print("5. Close account")
                    print("6. Modify account")
                    print("7. Logout")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        check_balance(user)
                    elif choice == "2":
                        amount = float(input("Enter the amount to deposit: "))
                        deposit(user, amount)
                    elif choice == "3":
                        amount = float(input("Enter the amount to withdraw: "))
                        withdraw(user, amount)
                    elif choice == "4":
                        name = input("Enter the name of the new account holder: ")
                        account_number = input("Enter the account number for the new account: ")
                        pin = input("Enter the PIN for the new account: ")
                        create_account(name, account_number, pin)
                    elif choice == "5":
                        close_account(user)
                        break
                    elif choice == "6":
                        field = input("Enter the field to modify (name or pin): ")
                        value = input("Enter the new value: ")
                        modify_account(user, field, value)
                    elif choice == "7":
                        break
                    else:
                        print("Invalid choice.")
                print("Logged out.")
        elif choice == "2":
            # Sign up
            name = input("Enter your name: ")
            account_number = input("Enter an account number: ")
            pin = input("Enter a PIN: ")
            create_account(name, account_number, pin)
        elif choice == "3":
            # Exit
            break
        else:
            print("Invalid choice.")
main()
