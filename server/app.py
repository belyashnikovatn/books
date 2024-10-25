from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'title': 'Повелитель мух',
        'author': 'У.Голдинг',
        'description': 'История благовоспитанных мальчиков, внезапно оказавшихся на необитаемом острове.',
        'read': True
    },
    {
        'title': 'Смерти.net',
        'author': 'Татьяна Замировская',
        'description': 'Антиутопия о об интернете для мертвых, всеобщем цифровом воскресении и изоляции',
        'read': True
    },
    {
        'title': 'Опосредованно',
        'author': 'А.Сальников',
        'description': 'Альтернативная реальность, где стихи - это не просто текст, а настоящий наркотик',
        'read': False
    },
]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


if __name__ == '__main__':
    app.run()
