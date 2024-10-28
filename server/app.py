import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Повелитель мух',
        'author': 'У.Голдинг',
        'description': 'История благовоспитанных мальчиков, внезапно оказавшихся на необитаемом острове.',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Смерти.net',
        'author': 'Татьяна Замировская',
        'description': 'Антиутопия о об интернете для мертвых, всеобщем цифровом воскресении и изоляции',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Опосредованно',
        'author': 'А.Сальников',
        'description': 'Альтернативная реальность, где стихи - это не просто текст, а настоящий наркотик',
        'read': False
    },
]


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'description': post_data.get('description'),
            'read': post_data.get('read'),
        })
        response_object['message'] = 'Книга добавлена!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'description': post_data.get('description'),
            'read': post_data.get('read'),
        })
        response_object['message'] = 'Книга изменена!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
