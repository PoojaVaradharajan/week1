import smtplib
import ssl

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, sender_password)
        
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, email_message)
        print("Email sent successfully")


s="oceanly204@gmail.com"
sp="lyihkkozuiqofazp"
sender_email=s
sender_password =sp
r=input("enter receiver mail: ")
recipient_email=r
subject = str(input("Enter Subject: "))
message = str(input("Enter message: "))

send_email(sender_email, sender_password, recipient_email, subject, message)
