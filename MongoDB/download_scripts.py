import json
from mongoengine import connect
from models import Author, Quote

# Підключення до бази даних
connect(host='mongodb+srv://alastovets:password@clustera.jq75x.mongodb.net/')

# Завантаження авторів
def load_authors() -> None:
    with open('authors.json', 'r', encoding='utf-8') as f:
        authors = json.load(f)
        for author in authors:
            if not author:
                new_author = Author(
                fullname=author['fullname'],
                born_date=author['born_date'],
                born_location=author['born_location'],
                description=author['description']
            )
                new_author.save()
                print(f'Author: {new_author.fullname} created.')
            else:
                print(f'Author already exists:\n {author}')
        
# Завантаження цитат
def load_quotes() -> None:
    with open('qoutes.json', 'r', encoding='utf-8') as f:
        quotes = json.load(f)
        for quote in quotes:
            author = Author.objects(fullname=quote['author']).first() 
            if author:
                new_quote = Quote(
                    tags=quote['tags'],
                    author=author,
                    quote=quote['quote']
                )
                new_quote.save()
                print(f'{new_quote} by {new_quote.author} was created')
            else:
                print(f'Author {author} exists in file {quotes}')

if __name__ == '__main__':
    load_authors()
    load_quotes()
