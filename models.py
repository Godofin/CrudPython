from sqlalchemy import Column, Integer, String

from database import Base 

class Book(Base):
    __tablename__ = "Library"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(150), nullable=False)
    author: str = Column(String(150), nullable=False)
    narrativeType: str = Column(String(150), nullable=False)
    publisher: str = Column(String(150), nullable=False)
    description: str = Column(String(150), nullable=False)
    EAN: str = Column(String(13), nullable=False)
    pageQuantity: int = Column(Integer, nullable=False)
    stock: int = Column(Integer, nullable=False)    