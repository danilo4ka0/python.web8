import mongoengine as me
from models import Author, Quote

# Подключение к MongoDB
me.connect('Danil', host='mongodb+srv://danilliashetsky:fAIk5srVPzr5lFxb@cluster0.dceb9uj.mongodb.net/')

def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [q.quote for q in quotes]
    return []

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [q.quote for q in quotes]

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [q.quote for q in quotes]

def main():
    while True:
        command = input('Введите команду: ').strip()
        if command.startswith('name:'):
            name = command[len('name:'):].strip()
            quotes = search_by_author(name)
        elif command.startswith('tag:'):
            tag = command[len('tag:'):].strip()
            quotes = search_by_tag(tag)
        elif command.startswith('tags:'):
            tags = command[len('tags:'):].strip()
            quotes = search_by_tags(tags)
        elif command == 'exit':
            break
        else:
            print('Неверная команда')
            continue
        
        for quote in quotes:
            print(quote)

if __name__ == '__main__':
    main()
