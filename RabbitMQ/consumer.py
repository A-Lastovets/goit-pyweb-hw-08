import pika
from create_models import Contact

def send_email(contact):
    # Імітація відправки email
    print(f"Sending email to {contact.full_name} <{contact.email}>")
    # Оновлення статусу у базі даних
    contact.message_sent = True
    contact.save()

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects.get(id=contact_id)
    send_email(contact)
    print(f'[x] Email sent and status updated for {contact}')

# Налаштування RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

# Підписка на чергу
channel.queue_declare(queue='email_queue')
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()