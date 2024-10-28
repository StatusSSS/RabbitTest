import pika
import time
from celery_app import email_task

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='email', durable=True)
print("waiting for the message. To exit press Ctrl+C")


def callback(ch, method, properties, email):
    print(f"RabbitMQ получил {email}")
    email_str = email.decode('utf-8')
    new_email = email_task(email_str)
    time.sleep(10)
    print("RabbitMQ отправил Celery")


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback,
                      queue='email',
                      auto_ack=True)

channel.start_consuming()