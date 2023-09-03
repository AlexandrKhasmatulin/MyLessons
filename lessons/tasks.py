from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


@shared_task
def send_message_about_subscription():
    print(f'Письмо отослано')
def send_message_of_abscence():
    users_list = User.objects.filter(last_login=datetime.date.today()-timedelta(days = 30 ))
    for user in users_list:
        print(f'Change {user} to inactive')