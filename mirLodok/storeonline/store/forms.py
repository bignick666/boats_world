from django import forms
from django.conf import settings
from django.core.mail import send_mail

from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, help_text='Укажите, как к вам обращаться')
    phone_number = PhoneNumberField(help_text='Введите ваш номер телефона')

    def get_message(self):
        cl_data = super().clean()
        name_f = cl_data.get('name').strip()
        number = cl_data.get('phone_number')
        subject = 'Перезвонить, есть вопросы'
        msg = f'Пользователь по имени {name_f}, просил перезвонить по номеру: {number}'
        return subject, msg

    def send(self):
        subject, msg = self.get_message()
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.DEFAULT_FROM_EMAIL]
        )
