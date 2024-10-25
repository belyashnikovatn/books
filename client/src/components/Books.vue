<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Книги</h1>
                <hr><br><br>
                <button type="button" class="btn btn-success btn-sm">Добавить книгу</button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Название</th>
                            <th scope="col">Автор</th>
                            <th scope="col">Описание</th>
                            <th scope="col">Прочли?</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(book, index) in books" :key="index">
                            <td>{{ book.title }}</td>
                            <td>{{ book.author }}</td>
                            <td>{{ book.description }}</td>
                            <td>
                                <span v-if="book.read">Да</span>
                                <span v-else>Нет</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button type="button" class="btn btn-warning btn-sm">Udpate</button>
                                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            books: [],
        };
    },
    methods: {
        getBooks() {
            const path = 'http://localhost:5001/books';
            axios.get(path)
                .then((res) => {
                    this.books = res.data.books;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
    created() {
        this.getBooks();
    },
};
</script>