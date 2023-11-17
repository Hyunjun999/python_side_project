import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

send_email = "type_yours"
send_pw = "your_pw"

receive_email = "type_yours"

smtp_name = "smtp.domain.com"
smtp_port = 587

msg = (
    MIMEMultipart()
)  # create a MIMEMultipart object to send both text(content) and attachment
msg["Subject"] = "automatically send with an attachment"
msg["From"] = send_email
msg["To"] = receive_email
text = """this is an email with an attachment sent by python automatically."""
content = MIMEText(text)
msg.attach(content)
attachment_path = r"attachment.txt"
with open(attachment_path, "rb") as f:
    etc_part = MIMEApplication(f.read())  # read the file and load it on the header
    etc_part.add_header("Content-Disposition", "attachment", filename="attachment.txt")
    msg.attach(etc_part)
s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()  # Encrypts data here to prevent others from eavesdropping
s.login(send_email, send_pw)
s.sendmail(send_email, receive_email, msg.as_string())
s.quit()
