from flask import Flask, jsonify, request
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


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'description': post_data.get('description'),
            'read': post_data.get('read'),
        })
        response_object['message'] = 'Книга добавлена!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
