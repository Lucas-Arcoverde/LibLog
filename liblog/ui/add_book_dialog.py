import os
import json
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
)
from liblog.models.book import Book

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data')
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_book(book: Book):
    ensure_data_dir()
    books = []
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            try:
                books = json.load(f)
            except json.JSONDecodeError:
                books = []
    books.append(book.to_dict())
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

class AddBookDialog(QDialog):
    def __init__(self, parent=None, book: Book = None):
        super().__init__(parent)
        self.setWindowTitle('LibLog | Add/Edit Book')
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Title:"))
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Author:"))
        self.author_input = QLineEdit()
        layout.addWidget(self.author_input)

        layout.addWidget(QLabel("Genre:"))
        self.genre_input = QLineEdit()
        layout.addWidget(self.genre_input)

        layout.addWidget(QLabel("Review (1-5):"))
        self.review_input = QComboBox()
        self.review_input.addItems([str(i) for i in range(1, 6)])
        layout.addWidget(self.review_input)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.edit_mode = False
        if book:
            self.edit_mode = True
            self.title_input.setText(book.title)
            self.author_input.setText(book.author)
            self.genre_input.setText(book.genre)
            self.review_input.setCurrentText(str(book.review))

    def accept(self):
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()
        genre = self.genre_input.text().strip()
        review = int(self.review_input.currentText())

        if not title or not author or not genre:
            QMessageBox.warning(self, "Error", "Fill in all fields.")
            return

        self.book = Book(title, author, genre, review)
        if not self.edit_mode:
            save_book(self.book)
            QMessageBox.information(self, "Success", "Book saved successfully!")
        super().accept()

    def get_book(self):
        return