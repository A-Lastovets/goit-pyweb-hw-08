from mongoengine import Document, StringField, ReferenceField, ListField, connect

# Підключення до бази даних
connect(host='mongodb+srv://alastovets:password@clustera.jq75x.mongodb.net/')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)
    quote = StringField(required=True)
