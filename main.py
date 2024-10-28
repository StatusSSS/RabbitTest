import fastapi
from fastapi import FastAPI
from schemas import Account
import pika


app = FastAPI()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue="email", durable=True)

@app.post("/")
async def root(acc_data: Account):
    message = acc_data.email

    channel.basic_publish(exchange='',
                      routing_key='email',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode= 2,
                      ))
    connection.close()
    return "account register"