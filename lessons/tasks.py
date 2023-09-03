from datetime import datetime, timedelta

from celery import shared_task

from django.core.mail import send_mail
from django.shortcuts import render

from MyLessons import settings
from lessons.models_lessons import Mailing
from users.models import User


@shared_task
def about_subscription(request):
    mailing = Mailing.objects.get(title="Подписка")  # Get the specific Mailing object with the desired title
    title = mailing.title
    content = mailing.content

    # Get the list of clients
    clients = User.objects.all()

    # Create a list of email addresses from the clients list
    recipient_list = [client.email for client in clients]

    # Send the email to all addresses in recipient_list
    send_mail(title, content, settings.EMAIL_HOST_USER, recipient_list)
    return render(request, "latter/email_complete.html")


def send_message_of_abscence(request):
    mailing = Mailing.objects.get(
        title="Отсутствие более месяца")  # Get the specific Mailing object with the desired title
    title = mailing.title
    content = mailing.content

    # Get the list of clients
    clients = User.objects.all()

    # Create a list of email addresses from the clients list
    users_list = User.objects.filter(last_login=datetime.date.today() - timedelta(days=30))
    recipient_list = [client.email for client in users_list]
    # Send the email to all addresses in recipient_list
    send_mail(title, content, settings.EMAIL_HOST_USER, recipient_list)
    return render(request, "latter/email_complete.html")
