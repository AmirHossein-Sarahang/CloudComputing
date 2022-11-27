import pika
AMQP_URL = "amqps://gyjulrsw:MzcT8naV6UtpQX05P_1HMBTKDQNX_2ig@beaver.rmq.cloudamqp.com/gyjulrsw"

def SendMessage(Message):
    try:
        connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body=Message)
        print("Sent !")
        connection.close()
        return True
    except():
        return False

