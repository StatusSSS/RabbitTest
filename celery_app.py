from celery import Celery
import time



celery_app = Celery('email_task', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


@celery_app.task
def email_task(email_data: bytes):
    print(f"Отправка письма на почту: {email_data}")
    time.sleep(5)
    print("Письмо доставлено")

