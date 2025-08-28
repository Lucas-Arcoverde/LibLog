# LibLog

LibLog é um aplicativo desktop simples para gerenciamento de livros lidos, desenvolvido em Python com PyQt6. Ele permite adicionar, editar, remover e buscar livros, salvando os dados localmente em um arquivo JSON.

## Funcionalidades

- Adicionar livros com título, autor, gênero e nota (review)
- Editar e remover livros cadastrados
- Buscar livros por título, autor, gênero ou nota
- Interface gráfica amigável e responsiva
- Persistência dos dados em arquivo JSON na pasta `data/`

## Estrutura do Projeto

```
liblog/
│
├── models/
│   └── book.py           # Classe Book (modelo de livro)
│
├── ui/
│   ├── add_book_dialog.py # Diálogo para adicionar/editar livros
│   └── main_window.py     # Janela principal do aplicativo
│
├── utils/
│   └── book_storage.py    # Funções utilitárias para carregar livros
│
└── __init__.py
data/
└── books.json             # Arquivo gerado automaticamente para armazenar os livros
```

## Como executar

1. **Instale as dependências**  
   Recomendado usar um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install pyqt6
   ```

2. **Execute o aplicativo**
   ```bash
   python -m liblog.ui.main_window
   ```

## Observações

- O arquivo `books.json` será criado automaticamente na primeira execução, dentro da pasta `data/`.
- O projeto pode ser expandido com novas funcionalidades, como exportação, importação, ou integração com outros serviços.

## Licença

Este projeto é livre para fins de estudo e uso pessoal.

---
Desenvolvido por Lucas Arcoverde
