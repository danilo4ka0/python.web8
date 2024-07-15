# consumer.py
import pika
from models import Contact

def send_email(contact):
    print(f"Sending email to {contact.email}")
    # Имитируем отправку email (функция-заглушка)
    return True

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    if contact:
        if send_email(contact):
            contact.sent = True
            contact.save()
            print(f"Email sent to {contact.email} and status updated")
    else:
        print(f"Contact with id {contact_id} not found")

def consume_from_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume_from_queue()
