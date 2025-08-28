import os
import json
from liblog.models.book import Book

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data')
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
        try:
            books_data = json.load(f)
            return [Book.from_dict(b) for b in books_data]
        except json.JSONDecodeError:
            return []