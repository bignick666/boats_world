from django import forms
from django.conf import settings
from django.core.mail import send_mail

from phonenumber_field.formfields import PhoneNumberField

from store.tasks import send_email_message


class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, help_text='Укажите, как к вам обращаться')
    phone_number = PhoneNumberField(help_text='Введите ваш номер телефона')

    def send(self):
        send_email_message.delay(
            self.cleaned_data['name'],
            str(self.cleaned_data['phone_number'])
        )
