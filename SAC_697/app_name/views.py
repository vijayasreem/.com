from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_welcome_email(user):
    subject = "Welcome to our site!"
    message = render_to_string('email_templates/welcome_email.html', {'user': user})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)

def send_password_reset_email(user):
    subject = "Password Reset Request"
    message = render_to_string('email_templates/password_reset_email.html', {'user': user})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)

def send_order_confirmation_email(user):
    subject = "Order Confirmation"
    message = render_to_string('email_templates/order_confirmation_email.html', {'user': user})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)

def send_account_activity_alert_email(user):
    subject = "Account Activity Alert"
    message = render_to_string('email_templates/account_activity_alert_email.html', {'user': user})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)

def log_email_status(email_status):
    # logic to log email status
    pass