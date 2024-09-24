import subprocess
import boto3
import json
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



#do your tasks


def send_email(sender_email, sender_password, recipients, subject, body_text):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipients)
    message['Subject'] = subject

    message.attach(MIMEText(body_text, 'plain'))

    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)

        # Send email
        server.send_message(message)
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
    finally:
        server.quit()


def stop_instance():
    instance_id = 'i-09ba87c38aed3e805'
    region = 'eu-north-1'

    # Send email notification
    sender_email = "jahansumaiya49@gmail.com"
    sender_password = "moqo fvwn grlo uzqh"
    recipients = ["monirul399399820@gmail.com", "jahansumaiya49@gmail.com"]
    subject = "EC2 Instance Shutdown Notification"
    body_text = f"The EC2 instance v7: {instance_id} in region: {region} and districts[-1687:-1615] is about to shut down."

    send_email(sender_email, sender_password, recipients, subject, body_text)

    # Stop the instance
    command = f'aws ec2 stop-instances --instance-ids {instance_id} --region {region}'
    subprocess.run(command, shell=True, check=True)
    print(f'Stopped instance {instance_id}')