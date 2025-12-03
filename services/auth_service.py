from db import SessionLocal
from models import User
from helpers.security import hash_pin, verify_pin


def register_user(username: str, pin:int):
    session = SessionLocal()
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        session.close()
        print("Username already taken")
        return 
    #Validating the 4 pin integer
    if not (1000<=pin<= 9999):
        session.close()
        print("Pin must be a 4 digit integer")
        return
    
    #new user
    new_user = User(username=username, pin_hash = hash_pin(pin))
    session.add(new_user)
    session.commit()
    session.close()
    print("User registered succesfuly")
    return

#login

def login_user(username:str, pin:int):
    session = SessionLocal()
    user = session.query(User).filter_by(username =username).first()
    if not user:
        session.close()
        print("User not found")
        return 
    
    if not verify_pin(pin, user.pin_hash):
        session.close()
        print("Incorrect pin")
        return 
    
    session.close()
    print("Login Successful")
    return