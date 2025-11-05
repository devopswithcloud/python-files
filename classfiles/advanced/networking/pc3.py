import smtplib

sender ="your_email@gail.com"
receiver ="receiver_email@gmail.com"
password ="your_password"

message ="""\
Subject: Test email from python
hello this is a test email 
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,message)
server.quit()
print("email sent scuessfully")