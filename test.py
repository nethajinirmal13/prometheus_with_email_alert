import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = 'mentornirmal@gmail.com'
msg['To'] = 'nethajinirmal13@gmail.com'

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('mentornirmal@gmail.com', 'yecq mlxi mttd dmlj')
    server.send_message(msg)
    print('Test email sent successfully.')
