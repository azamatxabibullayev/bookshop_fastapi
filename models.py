from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, Float
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.utils import ChoiseType


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    birth_date = Column(String, nullable=False)
    death_date = Column(String, nullable=True)
    books = relationship("Book_Author", back_populates="author")

    def __repr__(self):
        return f'<Author {self.id}: {self.name}>'


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship("Books", back_populates="category")

    def __repr__(self):
        return f'<Category {self.id}: {self.name}>'


class Books(Base):
    BOOK_GENRE = (
        ('FICTION', 'fiction'),
        ('NON-FICTION', 'non-fiction'),
        ('BIOGRAPHY', 'biography'),
        ('THRILLER', 'thriller')
    )
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    genre = Column(ChoiceType(BOOK_GENRE), default='FICTION')
    publication_year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    is_available = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    author = relationship("Author", back_populates="books")
    category = relationship("Category", back_populates="books")
    reviews = relationship("Review", back_populates="book")
    book_authors = relationship("Book_Author", back_populates="book")

    def __repr__(self):
        return f'<Book {self.id}: {self.name}>'


class Book_Author(Base):
    __tablename__ = 'book_author'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)

    book = relationship("Books", back_populates="book_authors")
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f'<Book_Author Book ID {self.book_id} - Author ID {self.author_id}>'


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    book = relationship("Books", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

    def __repr__(self):
        return f'<Review {self.id}: {self.comment}>'
