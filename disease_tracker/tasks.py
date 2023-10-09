from celery import shared_task
from django.core.mail import send_mail
import random


@shared_task
def send_otp_email(email):
    otp = str(random.randint(100000, 999999))
    subject = 'Your OTP for login'
    message = f'Your OTP is: {otp}. This OTP is valid for 5 minutes.'
    from_email = 'your_email@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return otp
