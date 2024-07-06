from database import engine, Base
from models import Author, Books

Base.metadata.create_all(bind=engine)
