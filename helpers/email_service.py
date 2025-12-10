
import smtplib
from email.mine.text import MIMEtext
from email.mime.multipart import MIMEmultipart
from config import DEFAULT_SENDER, SMTP_SERVER,SMTP_PORT,SMTP_PASSWORD

def send_transaction(recipient_email:str, subject:str, body:str):
    """sending a transaction confirmation to the user"""
    
    #creating the email
    