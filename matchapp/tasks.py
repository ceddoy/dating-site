from django.core.mail import send_mail

from dating_site import settings
from dating_site.celery import app


@app.task
def send_email_to_users(user_1, user_2):
    full_data_users = [user_1, user_2]
    email_users = [user_2.get('email'), user_1.get('email')]
    for user_to in full_data_users:
        subject = f'У вас произошла взаимность!'
        message = f'Вы понравились {user_to.get("last_name")} {user_to.get("first_name")}! ' \
                  f'Почта участника: {user_to.get("email")}'
        for from_user in email_users:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [from_user], fail_silently=True)
            email_users.reverse()
            break
