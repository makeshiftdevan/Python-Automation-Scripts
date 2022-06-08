import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#Insert email addresses (from, to)
fromaddr = "sendingEmailAddressGoesHere"
toaddr = "recievingEmailAddressGoesHere"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject
time_now = datetime.datetime.now().isoformat()
msg['Subject'] = "Daily Attendance" + time_now[0:10]
  
# string to store the body of the mail 
body = r"Today's attendance has been taken."
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# encode into base64 
#encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment;None") 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication. Replace ****** with password for FROM email address
s.login(fromaddr, "******") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit()



