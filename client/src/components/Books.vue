<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Книги</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Добавить книгу
        </button>
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
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="toggleEditBookModal(book)">
                    Изменить
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleDeleteBook(book)">
                    Удалить
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- add new book modal -->
    <div
    ref="addBookModal"
    class="modal fade"
    :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
    tabindex="-1"
    role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Добавить новую книгу</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookTitle" class="form-label">Название:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookTitle"
                  v-model="addBookForm.title"
                  placeholder="Введите название">
              </div>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Автор:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addBookForm.author"
                  placeholder="Введите автора">
              </div>
              <div class="mb-3">
                <label for="addBookDescription" class="form-label">Описание:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookDescription"
                  v-model="addBookForm.description"
                  placeholder="Введите описание">
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="addBookRead"
                  v-model="addBookForm.read">
                <label class="form-check-label" for="addBookRead">Прочитали?</label>
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit">
                  Сохранить
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset">
                  Отменить
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>
    
    <!-- edit book modal -->
    <div
    ref="editBookModal"
    class="modal fade"
    :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
    tabindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Изменить</h5>
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleEditBookModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="editBookTitle" class="form-label">Название:</label>
              <input
                type="text"
                class="form-control"
                id="editBookTitle"
                v-model="editBookForm.title"
                placeholder="Введите название">
            </div>
            <div class="mb-3">
              <label for="editBookAuthor" class="form-label">Автор:</label>
              <input
                type="text"
                class="form-control"
                id="editBookAuthor"
                v-model="editBookForm.author"
                placeholder="Введите автора">
            </div>
            <div class="mb-3">
              <label for="editBookDescription" class="form-label">Описание:</label>
              <input
                type="text"
                class="form-control"
                id="editBookDescription"
                v-model="editBookForm.description"
                placeholder="Введите описание">
            </div>
            <div class="mb-3 form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="editBookRead"
                v-model="editBookForm.read">
              <label class="form-check-label" for="editBookRead">Прочитали?</label>
            </div>
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="handleEditSubmit">
                Сохранить
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="handleEditCancel">
                Отменить
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    </div>
    <div v-if="activeEditBookModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
  import axios from 'axios';
  import Alert from './Alert.vue';
  
  export default {
    data() {
      return {
        activeAddBookModal: false,
        activeEditBookModal: false,
        addBookForm: {
          title: '',
          author: '',
          description: '',
          read: [],
        },
        books: [],
        editBookForm: {
          id: '',
          title: '',
          author: '',
          description: '',
          read: [],
        },
        message: '',
        showMessage: false,
      };
    },
    components: {
      alert: Alert,
    },
    methods: {
      addBook(payload) {
        const path = 'http://localhost:5001/books';
        axios.post(path, payload)
          .then(() => {
            this.getBooks();
            this.message = 'Книга добавлена!';
            this.showMessage = true;
          })
          .catch((error) => {
  
            console.log(error);
            this.getBooks();
          });
      },
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
      updateBook(payload, bookID) {
        const path = `http://localhost:5001/books/${bookID}`
        axios.put(path, payload)
          .then(() => {
            this.getBooks();
            this.message = 'Книга изменена!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getBooks();
          });
      },
      handleAddReset() {
        this.initForm();
      },
      handleAddSubmit() {
        this.toggleAddBookModal();
        let read = false;
        if (this.addBookForm.read[0]) {
          read = true;
        }
        const payload = {
          title: this.addBookForm.title,
          author: this.addBookForm.author,
          description: this.addBookForm.description,
          read,
        };
        this.addBook(payload);
        this.initForm();
      },
      handleEditCancel() {
        this.toggleEditBookModal(null);
        this.initForm();
        this.getBooks();
      },
      handleEditSubmit() {
        this.toggleEditBookModal(null);
        let read = false;
        if (this.editBookForm.read) read = true;
        const payload = {
          title: this.editBookForm.title,
          author: this.editBookForm.author,
          description: this.editBookForm.description,
          read,          
        };
        this.updateBook(payload, this.editBookForm.id);
      },
      initForm() {
        this.addBookForm.title = '';
        this.addBookForm.author = '';
        this.addBookForm.description = '';
        this.addBookForm.read = [];
        this.editBookForm.id = '';
        this.editBookForm.title = '';
        this.editBookForm.author = '';
        this.editBookForm.description = '';
        this.editBookForm.read = [];
      },
      toggleAddBookModal() {
        const body = document.querySelector('body');
        this.activeAddBookModal = !this.activeAddBookModal;
        if (this.activeAddBookModal) {
          body.classList.add('modal-open');
        } else {
          body.classList.remove('modal-open');
        }
      },
      toggleEditBookModal(book) {
        if (book) {
          this.editBookForm = book;
        }
        const body = document.querySelector('body');
        this.activeEditBookModal = !this.activeEditBookModal;
        if (this.activeEditBookModal) {
          body.classList.add('modal-open');
        } else {
          body.classList.remove('modal-open');
        }
      },
      handleDeleteBook(book) {
        this.removeBook(book.id);
      },
      removeBook(bookID) {
        const path = `http://localhost:5001/books/${bookID}`;
        axios.delete(path)
          .then(() => {
            this.getBooks();
            this.message = 'Книга удалена!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getBooks();
          });
      },
    },
    created() {
      this.getBooks();
    },
  };
  </script>