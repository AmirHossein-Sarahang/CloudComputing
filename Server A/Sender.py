import pika
AMQP_URL = "amqps://dfphuyyq:4FzUTXTxXZ5w3A20MRD3c6IIqTrOz4ZT@hawk.rmq.cloudamqp.com/dfphuyyq"

def SendMessage(Message):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=Message)
    print("Sent !")
    connection.close()

