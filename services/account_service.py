# services/account_service.py

import random
from db import SessionLocal
from models import User, Account

def _make_account_number():
    """Create a short random account number like ACC-123456."""
    return f"ACC-{random.randint(100000, 999999)}"

def create_account(username: str, account_number: str = None, starting_balance: float = 0.0):
    """
    Create an account for an existing user.
    Prints success/failure messages (no return).
    If account_number is None, a unique random one will be generated.
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(username=username).first()
        if not user:
            print(f"User '{username}' not found.")
            return

        # choose or generate an account number
        acct_no = account_number or _make_account_number()

        # ensure uniqueness (if random collides, try again a few times)
        attempts = 0
        while session.query(Account).filter_by(account_number=acct_no).first():
            attempts += 1
            if attempts > 5:
                print("Failed to generate a unique account number; try passing one manually.")
                return
            acct_no = _make_account_number()

        new_acc = Account(user_id=user.id, account_number=acct_no, balance=starting_balance)
        session.add(new_acc)
        session.commit()
        session.refresh(new_acc)

        print("Account created successfully!")
        print(f"  Username: {username}")
        print(f"  Account Number: {new_acc.account_number}")
        print(f"  Balance: {new_acc.balance}")
    finally:
        session.close()


def list_accounts(username: str):
    """
    Print all accounts for a username.
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(username=username).first()
        if not user:
            print(f"User '{username}' not found.")
            return

        accounts = session.query(Account).filter_by(user_id=user.id).all()
        if not accounts:
            print(f"No accounts found for user '{username}'.")
            return

        print(f"Accounts for {username}:")
        for a in accounts:
            print(f"  - {a.account_number} (balance: {a.balance})")
    finally:
        session.close()


def get_account(account_number: str):
    """
    Print a single account's details.
    """
    session = SessionLocal()
    try:
        acc = session.query(Account).filter_by(account_number=account_number).first()
        if not acc:
            print(f"Account '{account_number}' not found.")
            return
        print(f"Account: {acc.account_number}")
        print(f"  Owner user_id: {acc.user_id}")
        print(f"  Balance: {acc.balance}")
    finally:
        session.close()
