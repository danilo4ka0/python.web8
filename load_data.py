import json
import mongoengine as me
import os
from models import Author, Quote

# Подключение к MongoDB с дополнительными параметрами
me.connect(
    db='Danil',
    host='mongodb+srv://danilliashetsky:fAIk5srVPzr5lFxb@cluster0.dceb9uj.mongodb.net/',
    tlsAllowInvalidCertificates=True,
    tlsAllowInvalidHostnames=True
)

# Пути к файлам
authors_file_path = 'C:\\Users\\demo\\Desktop\\python.web8\\data\\authors.json'
quotes_file_path = 'C:\\Users\\demo\\Desktop\\python.web8\\data\\quotes.json'

# Проверка существования файлов
if not os.path.exists(authors_file_path):
    print(f"File not found: {authors_file_path}")
    exit(1)
if not os.path.exists(quotes_file_path):
    print(f"File not found: {quotes_file_path}")
    exit(1)

# Загрузка авторов
with open(authors_file_path, 'r', encoding='utf-8') as f:
    authors_data = json.load(f)
    for author in authors_data:
        a = Author(
            fullname=author['fullname'],
            born_date=author['born_date'],
            born_location=author['born_location'],
            description=author['description']
        )
        a.save()

# Загрузка цитат
with open(quotes_file_path, 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)
    for quote in quotes_data:
        author = Author.objects(fullname=quote['author']).first()
        if author:
            q = Quote(
                tags=quote['tags'],
                author=author,
                quote=quote['quote']
            )
            q.save()
