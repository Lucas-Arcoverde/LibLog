# 📚 LibLog

LibLog is a simple desktop application for managing your read books, built with **Python** and **PyQt6**.
It lets you **add, edit, remove, and search** books, saving everything locally in a **JSON file**.

---

## ✨ Features

* ➕ Add books with **title, author, genre, and rating**
* ✏️ Edit and 🗑️ remove registered books
* 🔍 Search books by **title, author, genre, or rating**
* 🖥️ Friendly and responsive graphical interface
* 💾 Data persistence in a JSON file inside the `data/` folder

---

## 📂 Project Structure

```
liblog/
│
├── models/
│   └── book.py            # 📖 Book class (book model)
│
├── ui/
│   ├── add_book_dialog.py # ➕ Dialog for adding/editing books
│   └── main_window.py     # 🪟 Main application window
│
├── utils/
│   └── book_storage.py    # 🛠️ Utility functions for loading books
│
└── __init__.py
data/
└── books.json             # 📂 Automatically generated file to store books
```

---

## 🚀 How to Run

1. **Install dependencies**
   Recommended: use a virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install pyqt6
   ```

2. **Run the application**

   ```bash
   python -m liblog.ui.main_window
   ```

---

## 📝 Notes

* The file `books.json` will be created automatically on the **first run** inside the `data/` folder.
* The project can be expanded with more features, such as 📤 export, 📥 import, or 🔗 integration with other services.

---

## 📜 License

This project is **free** for study and personal use.

---

👨‍💻 Developed by **Lucas Arcoverde**

<img width="1002" height="789" alt="image" src="https://github.com/user-attachments/assets/e031da83-bb89-4496-8362-008c8d2b2ad2" />
<img width="1002" height="789" alt="image" src="https://github.com/user-attachments/assets/cf7aab3a-b630-44eb-9cf1-ca15660bee54" />

