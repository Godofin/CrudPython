from sqlalchemy.orm import Session

from models import Book

class BookRepository:
    @staticmethod
    def find_all(db: Session) -> list[Book]:
        return db.query(Book).all()

    @staticmethod
    def save(db: Session, book: Book) -> Book:
        if book.id:
            db.merge(book)
        else:
            db.add(book)
        db.commit()
        return book

    @staticmethod
    def find_by_id(db: Session, id: int) -> Book:
        return db.query(Book).filter(Book.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Book).filter(Book.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        book = db.query(Book).filter(Book.id == id).first()
        if book is not None:
            db.delete(book)
            db.commit()