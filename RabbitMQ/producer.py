import pika
from faker import Faker
from create_models import Contact

# Ініціалізація Faker
fake = Faker()

# Налаштування RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue='email_queue')

def create_fake_contacts(count=10):
    contacts = []
    for _ in range(count):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
        )
        contact.save()
        contacts.append(contact)
    return contacts

def send_contacts_to_queue(contacts):
    for contact in contacts:
        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(contact.id)
        )
        print(f'[x] Sent {contact}')

if __name__ == '__main__':
    # Генерація 10 фейкових контактів
    contacts = create_fake_contacts(10)
    # Відправка контактів у RabbitMQ
    send_contacts_to_queue(contacts)
    # Закриття з'єднання
    connection.close()