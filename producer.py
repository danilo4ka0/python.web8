# producer.py
import pika
import json
from faker import Faker
from models import Contact

def generate_contacts(n):
    fake = Faker()
    contacts = []
    for _ in range(n):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email()
        )
        contact.save()
        contacts.append(contact)
    return contacts

def send_to_queue(contact_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact_id))
    connection.close()

if __name__ == '__main__':
    contacts = generate_contacts(10)
    for contact in contacts:
        send_to_queue(contact.id)
    print("Contacts generated and sent to queue")
