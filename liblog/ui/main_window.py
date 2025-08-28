import sys
import os
import json
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtWidgets import (
    QWidget, QApplication, QMainWindow, QPushButton, QLabel, QToolBar, 
    QVBoxLayout, QHBoxLayout, QMenu, QToolButton, QLineEdit, QTableWidget, 
    QHeaderView, QTableWidgetItem, QMessageBox
)

from liblog.ui.add_book_dialog import AddBookDialog
from liblog.models.book import Book
from liblog.utils.book_storage import load_books

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data')
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')

def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump([b.to_dict() for b in books], f, ensure_ascii=False, indent=4)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('LibLog | v0.0.1')
        self.resize(800, 600)
        
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        toolbar = QToolBar('Main Toolbar')
        self.addToolBar(toolbar)
        
        help_menu = QMenu('Help', self)
        for name in ['About LibLog', 'How to use LibLog']:
            action = QAction(name, self)
            help_menu.addAction(action)
        help_button = QToolButton()
        help_button.setText('Help')
        help_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        help_button.setMenu(help_menu)
        toolbar.addWidget(help_button)
        
        title = QLabel('LibLog')
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title.setFont(title_font)
        self.layout.addWidget(title)
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search for a book, author, etc...')
        self.search_button = QPushButton('Search')
        self.add_book_button = QPushButton('Add')
        
        self.add_book_button.clicked.connect(self.open_add_book_dialog)
        self.search_button.clicked.connect(self.search_books)
        self.search_bar.textChanged.connect(self.on_search_text_changed)
        
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.add_book_button)
        self.layout.addLayout(search_layout)
        
        self.books_table = QTableWidget(0, 6)
        self.books_table.setHorizontalHeaderLabels(
            ['Title', 'Author', 'Genre', 'Review', 'Edit', 'Delete']
        )
        self.books_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.books_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.books_table.setMaximumHeight(400)
        self.layout.addWidget(self.books_table, stretch=1)

        self.update_table()
        
    def resizeEvent(self, event):
        max_table_height = self.height() - 100
        self.books_table.setMaximumHeight(max_table_height)
        super().resizeEvent(event)
    
    def open_add_book_dialog(self):
        dialog = AddBookDialog(self)
        if dialog.exec():
            self.update_table()
            self.search_bar.clear()
        
    def update_table(self):
        books = load_books()
        self._populate_table(books)
    
    def _populate_table(self, books):
        self.books_table.setRowCount(0)
        for row, book in enumerate(books):
            self.books_table.insertRow(row)
            self.books_table.setItem(row, 0, QTableWidgetItem(book.title))
            self.books_table.setItem(row, 1, QTableWidgetItem(book.author))
            self.books_table.setItem(row, 2, QTableWidgetItem(book.genre))
            self.books_table.setItem(row, 3, QTableWidgetItem(str(book.review)))
            edit_button = QPushButton('Edit')
            edit_button.clicked.connect(partial(self.edit_book_by_list, books, row))
            delete_button = QPushButton('Delete')
            delete_button.clicked.connect(partial(self.delete_book_by_list, books, row))
            self.books_table.setCellWidget(row, 4, edit_button)
            self.books_table.setCellWidget(row, 5, delete_button)
    
    def delete_book_by_list(self, books_list, row):
        all_books = load_books()
        book = books_list[row]
        try:
            index = all_books.index(book)
        except ValueError:
            return
        self.delete_book(index)
    
    def edit_book_by_list(self, books_list, row):
        all_books = load_books()
        book = books_list[row]
        try:
            index = all_books.index(book)
        except ValueError:
            return
        self.edit_book(index)
    
    def delete_book(self, row):
        books = load_books()
        if 0 <= row < len(books):
            reply = QMessageBox.question(
                self, "Confirm Delete",
                f"Are you sure you want to delete '{books[row].title}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                del books[row]
                save_books(books)
                self.update_table()
                self.search_bar.clear()

    def edit_book(self, row):
        books = load_books()
        if 0 <= row < len(books):
            book = books[row]
            dialog = AddBookDialog(self, book)
            if dialog.exec():
                updated_book = dialog.book
                books[row] = updated_book
                save_books(books)
                self.update_table()
                self.search_bar.clear()

    def search_books(self):
        query = self.search_bar.text().strip().lower()
        books = load_books()
        if not query:
            self.update_table()
            return
        filtered_books = [
            book for book in books
            if query in book.title.lower()
            or query in book.author.lower()
            or query in book.genre.lower()
            or query in str(book.review)
        ]
        self._populate_table(filtered_books)

    def on_search_text_changed(self, text):
        if not text.strip():
            self.update_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()