import bcrypt

def hash_pin(pin:int):
    """Hash a 4 pin integer"""
    return bcrypt.hashpw(str(pin).encode(), bcrypt.gensalt()).decode()
#verifying the pin
def verify_pin(pin:int, hashed_pin: str ):
    """verify integer pin against hashed pin"""
    return bcrypt.checkpw(str(pin).encode(),hashed_pin.encode() )