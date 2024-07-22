from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation(email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Your booking details: {booking_details}'
    send_mail(subject, message, 'from@example.com', [email])
