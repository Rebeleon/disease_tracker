from celery import shared_task
from django.core.mail import send_mail
from disease_tracker.settings import EMAIL_HOST_USER


@shared_task
def send_otp_email(email, otp):
    print('task entered')
    subject = 'Your OTP for login'
    message = f'Your OTP is: {otp}. This OTP is valid for 5 minutes.'
    from_email = EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    print('task done')
    return otp
