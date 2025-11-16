from sqlalchemy.orm import Mapped, mapped_column    # For model creation
from datetime import date                           # For transaction timestamp
from database import db                             # Gives access to db.Model to define database models
from sqlalchemy_serializer import SerializerMixin   # Allows for serialization of models. Serialized models need to include in model def


# Define database model. SerializerMixin adds a .to_dict() method to model instances.
class Transactions(db.Model, SerializerMixin):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(default=date.today().strftime("%D"))
    amount: Mapped[float] = mapped_column(default=0.0)
    memo: Mapped[str] = mapped_column(default="")
