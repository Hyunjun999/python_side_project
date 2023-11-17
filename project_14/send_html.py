import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

send_email = "type_yours"
send_pw = "your_pw"

receive_email = "type_yours"

smtp_name = "smtp.domain.com"  # ex) smtp.gmail.com
smtp_port = 587

msg = MIMEMultipart()
msg["Subject"] = "HTML msg included mail "
msg["From"] = send_email
msg["To"] = receive_email

html_body = """
    <h1 style="color: purple; background-color: black">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </h1>
    <ul style="list-style: square; color: red">
      <li>first</li>
      <li>second</li>
      <li>third</li>
    </ul>
"""
msg.attach(
    MIMEText(html_body, "html")
)  # determime the content-type as html to convert it
s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()  # Encrypts data here to prevent others from eavesdropping
s.login(send_email, send_pw)
s.sendmail(send_email, receive_email, msg.as_string())
s.quit()
