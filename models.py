from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from .app import db

class Settings(db.Model):
    # Set the name of the table
    __tablename__ = "settings"

    # Create column for unique ID - needed
    id: Mapped[int] = mapped_column(primary_key=True)

    # Create columns for settings, defaulting to $0 
    budget: Mapped[int] = mapped_column(default=0)
    spent: Mapped[int] = mapped_column(default=0)
    remaining: Mapped[int] = mapped_column(default=0)