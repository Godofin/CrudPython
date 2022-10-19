from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    narrativeType: str
    publisher: str
    description: str
    EAN: str
    pageQuantity: int
    stock: int

class BookRequest(BookBase):
    ...

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True