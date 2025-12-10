import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import DEFAULT_SENDER, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD

def send_transaction(recipient_email: str, subject: str, body: str):
    """Send a transaction confirmation to the user via email."""

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = DEFAULT_SENDER
    msg['To'] = recipient_email
    msg['Subject'] = subject  

    # Attach plain text body
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(DEFAULT_SENDER, SMTP_PASSWORD)
            server.send_message(msg)
        print(f"Transaction confirmation sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
