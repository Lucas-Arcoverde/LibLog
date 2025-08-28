import json

class Book:
    def __init__(self, title, author, genre, review: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.review = review

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "review": self.review
        }
        
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.title == other.title
            and self.author == other.author
            and self.genre == other.genre
            and self.review == other.review
        )

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            author=data.get("author", ""),
            genre=data.get("genre", ""),
            review=data.get("review", 0)
        )

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls.from_dict(data)

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)
