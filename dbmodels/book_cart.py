from sqlalchemy import  Column, ForeignKey, Table
from core.base import Base


BookCartTable = Table(
    "book_cart",
    Base.metadata,
    Column("books_id", ForeignKey("books.id"), primary_key=True),
    Column("carts_id", ForeignKey("carts.id", ondelete="CASCADE"), primary_key=True)    
)
