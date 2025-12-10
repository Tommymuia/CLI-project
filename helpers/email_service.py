import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import DEFAULT_SENDER, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD

def send_transaction(recipient_email: str, subject: str, body: str, amount, balance, name: str):
    amount = float(amount)
    balance = float(balance)

    """Send a professional HTML transaction confirmation email."""

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color:#f4f4f4; padding:20px;">
        <div style="max-width:600px; margin:auto; background:#ffffff; padding:25px; 
                    border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">

          <h2 style="color:#0A66C2; font-weight:bold; text-align:center;">
            Deposit Confirmation
          </h2>

          <p style="font-size:15px; color:#333;">
            Dear <strong>{name}</strong>,
          </p>

          <p style="font-size:15px; color:#333;">
            Your recent deposit has been successfully processed.
          </p>

          <table style="width:100%; margin-top:20px; border-collapse:collapse;">
            <tr>
              <td style="padding:10px; background:#fafafa; border:1px solid #ddd;">
                <strong>Amount Deposited:</strong>
              </td>
              <td style="padding:10px; border:1px solid #ddd;">
                KSh {amount:,.2f}
              </td>
            </tr>

            <tr>
              <td style="padding:10px; background:#fafafa; border:1px solid #ddd;">
                <strong>Current Balance:</strong>
              </td>
              <td style="padding:10px; border:1px solid #ddd;">
                KSh {balance:,.2f}
              </td>
            </tr>
          </table>

          <p style="font-size:15px; color:#222; margin-top:30px;">
            Thank you for banking with us.
          </p>

          <p style="font-size:15px; color:#333; margin-top:25px;">
            Thanks,<br>
            <strong>Muia CLI Group</strong>
          </p>

        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["From"] = DEFAULT_SENDER
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(DEFAULT_SENDER, SMTP_PASSWORD)
            server.send_message(msg)
        print(f"Transaction confirmation sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
