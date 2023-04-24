# Banking System App
This is a Python-based console application that simulates a simple banking system. It allows users to perform various banking operations such as checking account balance, depositing money, withdrawing money, creating new accounts, closing accounts, and modifying account details.

# Features
User authentication: Users need to provide their account number and PIN to log in to the system. The system verifies the provided credentials against the database to ensure secure access.

Account operations: Once logged in, users can perform various account operations such as checking balance, depositing money, and withdrawing money.

Account management: Users can create new accounts, close existing accounts, and modify account details such as name and PIN.

Admin functionality: The system supports an optional "is_admin" flag while creating an account, which can be used to designate an account as an admin account. Admin accounts have additional privileges, such as closing any account in the system.

# Requirements
Python 3.x
MySQL database server
mysql-connector-python library

# How to Use
Set up a MySQL database server and create a database called "banking_system".
Update the database connection details (host, user, password) in the code with your own credentials.
Install the mysql-connector-python library using pip or any other package manager.
Run the code in a Python environment.
Follow the prompts to perform various banking operations.
Use the provided account number and PIN for logging in.
Use the "is_admin" flag while creating an account to designate an admin account if required.

# Note
This is a basic simulation of a banking system and does not include advanced security features. It is intended for learning and educational purposes only and should not be used in a production environment without proper security measures.

# Disclaimer
This application does not handle real money or real user accounts. It is a simulation and should not be used for actual banking transactions.
