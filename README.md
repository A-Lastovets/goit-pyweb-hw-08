# goit-pyweb-hw-08

Частина 1: MongoDB

Запуск скриптів:
1. Запустіть файл "download_scripts.py" для генерації данних в базу MongoDB згідно вмісту файлів authors.json та quotes.json
2. Запустіть файл finding_quotes.py" щоб розпочати пошук цитат. Ви можете вводити команди у форматі:

name: Steve Martin
tag: life
tags: life,live
exit (для завершення скрипту)

Частина 2: RabbitMQ

Запуск скриптів:
1. Запустіть consumer.py, який буде постійно очікувати на нові повідомлення.
2. Запустіть producer.py, який згенерує фейкові контакти та відправить повідомлення в RabbitMQ.

Примітка:
MongoDB: Потрібно запустити MongoDB локально або використовувати MongoDB Atlas.
RabbitMQ: Переконайтеся, що RabbitMQ запущений локально.

Встановив локально сервіс RabbitMQ можна за допомогою Docker-образу:

docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

Таким чином, ці два скрипти дозволяють організувати просту систему розсилки email, використовуючи RabbitMQ та MongoDB.