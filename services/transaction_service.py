from datetime import datetime
from db import SessionLocal
from models import Account, Transaction


def _get_account(session, account_number: str):
    return session.query(Account).filter_by(account_number=account_number).first()


def deposit(account_number: str, amount: float, description: str = None):
    """Deposit money and print result."""
    if amount <= 0:
        print("Amount must be greater than zero")
        return

    session = SessionLocal()
    try:
        account = _get_account(session, account_number)
        if not account:
            print("Account not found")
            return

        account.balance += amount

        tx = Transaction(
            account_id=account.id,
            type="deposit",
            amount=amount,
            timestamp=datetime.utcnow(),
            description=description,
        )

        session.add(tx)
        session.commit()

        print(f"Deposited {amount} into {account_number}. New balance: {account.balance}")
    finally:
        session.close()


def withdraw(account_number: str, amount: float, description: str = None):
    """Withdraw money and print result."""
    if amount <= 0:
        print("Amount must be greater than zero")
        return

    session = SessionLocal()
    try:
        account = _get_account(session, account_number)
        if not account:
            print("Account not found")
            return

        if account.balance < amount:
            print("Insufficient funds")
            return

        account.balance -= amount

        tx = Transaction(
            account_id=account.id,
            type="withdraw",
            amount=amount,
            timestamp=datetime.utcnow(),
            description=description,
        )

        session.add(tx)
        session.commit()

        print(f"Withdrew {amount} from {account_number}. New balance: {account.balance}")
    finally:
        session.close()


def transfer(from_acc: str, to_acc: str, amount: float, description: str = None):
    """Transfer money and print result."""
    if amount <= 0:
        print("Amount must be greater than zero")
        return

    session = SessionLocal()
    try:
        sender = _get_account(session, from_acc)
        receiver = _get_account(session, to_acc)

        if not sender or not receiver:
            print("One or both accounts not found")
            return

        if sender.balance < amount:
            print("Insufficient funds in sender account")
            return

        # Update balances
        sender.balance -= amount
        receiver.balance += amount

        # Log transactions
        out_tx = Transaction(
            account_id=sender.id,
            type="transfer_out",
            amount=amount,
            timestamp=datetime.utcnow(),
            description=description,
        )
        in_tx = Transaction(
            account_id=receiver.id,
            type="transfer_in",
            amount=amount,
            timestamp=datetime.utcnow(),
            description=description,
        )

        session.add_all([out_tx, in_tx])
        session.commit()

        print(f"Transferred {amount} from {from_acc} to {to_acc}.")
        print(f"New balance for {from_acc}: {sender.balance}")
        print(f"New balance for {to_acc}: {receiver.balance}")

    finally:
        session.close()


def show_balance(account_number: str):
    """Print account balance."""
    session = SessionLocal()
    try:
        account = _get_account(session, account_number)
        if not account:
            print("Account not found")
            return

        print(f"Balance for {account_number}: {account.balance}")
    finally:
        session.close()


def show_transactions(account_number: str):
    """Print all transactions for an account."""
    session = SessionLocal()
    try:
        account = _get_account(session, account_number)
        if not account:
            print("Account not found")
            return

        txs = (
            session.query(Transaction)
            .filter_by(account_id=account.id)
            .order_by(Transaction.timestamp.desc())
            .all()
        )

        if not txs:
            print("No transactions found for this account")
            return

        print(f"Transaction history for {account_number}:")
        for tx in txs:
            print(
                f"{tx.timestamp} | {tx.type.upper():<12} | {tx.amount} | "
                f"{tx.description or ''}"
            )

    finally:
        session.close()
