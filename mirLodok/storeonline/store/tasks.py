from time import sleep
from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task


@shared_task()
def send_email_message(name, number):
    sleep(10)
    send_mail(
        'Перезвонить, есть вопросы!',
        message=f'Пользователь по имени {name}, просил перезвонить по номеру: {number}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.DEFAULT_FROM_EMAIL]
    )


