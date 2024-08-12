import mongoengine as me

# Підключення до MongoDB
me.connect(host='mongodb+srv://alastovets:8yqcQPghSOJWSYWo@clustera.jq75x.mongodb.net/')

class Contact(me.Document):
    full_name = me.StringField(required=True)
    email = me.EmailField(required=True)
    message_sent = me.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name} <{self.email}>'