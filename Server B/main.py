import EmialSender
import ImageProcess
import DB
import os
import pika
import sys

import S3DB

AMQP_URL = ""
def MainHandler(i):
    test = DB.GetUrl(i)
    result_image = ImageProcess.main(test[0])
    #result_image = ImageProcess.main(S3DB.GetURL(i))
    if  result_image == False:
        DB.setstate(i, False)
        EmialSender.send_email(test[1], i, False)
    else:
        DB.setstate(i, True)
        DB.SetCategory(i, result_image)
        EmialSender.send_email(test[1], i, True)



def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        print("Message received : ", body.decode())
        MainHandler(body.decode())
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

try:
    main()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

