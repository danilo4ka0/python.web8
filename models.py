from mongoengine import Document, StringField, EmailField, BooleanField, connect

# Подключение к MongoDB
connect(db='Danil', host='mongodb+srv://danilliashetsky:fAIk5srVPzr5lFxb@cluster0.dceb9uj.mongodb.net/your_database_name?retryWrites=true&w=majority')

class Contact(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True)
    sent = BooleanField(default=False)
