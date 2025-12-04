Thomas Muia
### CLI Money Transfer Project Overview
## Problem Statement
The project aims to build a simple Command-Line Banking System that allows users to securely manage their money. Users should be able to register, log in, check their balance, deposit funds, withdraw funds, and transfer money to other users. All data, including users, accounts, and transactions, must be stored in a relational database using SQLAlchemy for persistence and clean ORM management. The system should include proper validation, password security, and clear CLI menus to ensure smooth interaction and reliable financial operations.
## Description
 I will create a simple banking system where users can create accounts, check balances, deposit, withdraw, and transfer money to other users through the terminal.
 
# Key Features
## User Accounts
 Creating an account with a username, password, and initial balance.
Login/logout functionality.
Account Management
 Checking balance.
 Depositing money.
 Withdraw money.
## Money Transfer
 Transferring money between users.
  Verifying the recipient exists and has a valid account.
  Tracking transaction history.
## Transaction History
  Showing past deposits, withdrawals, and transfers.
## Data Persistence
  Storing user info and transactions in SQLite.
## Security Features
  Password validation (min length, symbols, numbers).


Models that I will be working with
## User Model
Represents each person using the system.
Key fields:
id – unique identifier
username – must be unique
password – hashed password
Relationship: One user → one account

## Account Model
Represents the user’s bank account.
Key fields:
id – unique identifier
user_id – links to the User
balance – current account balance
Relationship: One account → many transactions
## Transaction Model
Stores every financial action.
Key fields:
id – unique identifier
account_id – links to the Account
type – "deposit", "withdraw", or "transfer"
amount – transaction value
timestamp – when it occurred


