import smtplib
from email.mime.text import MIMEText

send_email = "type_yours"
send_pw = "your_pw"

receive_email = "type_yours"

smtp_name = "smtp.domain.com"  # ex) smtp.gmail.com
smtp_port = 587

text = """this is an email sent by python automatically."""
msg = MIMEText(text)
msg["Subject"] = "Mail Subject"
msg["From"] = send_email
msg["To"] = receive_email
print(msg.as_string())
s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()  # Encrypts data here to prevent others from eavesdropping
s.login(send_email, send_pw)
s.sendmail(send_email, receive_email, msg.as_string())
s.quit()
