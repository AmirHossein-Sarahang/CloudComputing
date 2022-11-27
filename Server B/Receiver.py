import os
import pika
import sys

AMQP_URL = "amqps://dfphuyyq:4FzUTXTxXZ5w3A20MRD3c6IIqTrOz4ZT@hawk.rmq.cloudamqp.com/dfphuyyq"
def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        print()
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def Recive():
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)