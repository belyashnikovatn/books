# books
Книги для книжного клуба: добавить/изменить/удалить книгу, отметить факт прочтения.

## Технологии
- Flask (for RESTful API)
- Vue (JS framework for the interface)
- Axios library (for the requests)
- Bootstrap (for the beauty)

## Запуск проекта
```bash
git clone https://github.com/belyashnikovatn/books.git
cd server
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run --port=5001 --debug

# в другом терминале
cd client
npm install
npm run dev

```
http://localhost:5173/

## Структура проекта
Интерфейс находится в:  
- books\client\src\components\Books.vue: список объектов, формы, кнопки;
- books\client\src\components\Alert.vue: уведомление.

Машрутизация прописана в books\client\src\router\index.js.  

Реализация API находится в books\server\app.py.  
