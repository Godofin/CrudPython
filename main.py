from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models import Book
from database import engine, Base, get_db
from repositories import BookRepository
from schemas import BookRequest, BookResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create(request: BookRequest, db: Session = Depends(get_db)):
    book = BookRepository.save(db, Book(**request.dict()))
    return BookResponse.from_orm(book)

@app.get("/api/books", response_model=list[BookResponse])
def find_all(db: Session = Depends(get_db)):
    books = BookRepository.find_all(db)
    return [BookResponse.from_orm(book) for book in books]

@app.get("/api/books/{id}", response_model=BookResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    book = BookRepository.find_by_id(db, id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found"
        )
    return BookResponse.from_orm(book)

@app.delete("/api/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not BookRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    BookRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/books/{id}", response_model=BookResponse)
def update(id: int, request: BookRequest, db: Session = Depends(get_db)):
    if not BookRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    book = BookRepository.save(db, Book(id=id, **request.dict()))
    return BookResponse.from_orm(book)
