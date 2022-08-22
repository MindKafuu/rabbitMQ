import pika
import sys

parameters = pika.URLParameters('amqp://guest:guest@10.131.200.163:5672/')
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message)

print(" [x] Sent %r" % message)
connection.close()