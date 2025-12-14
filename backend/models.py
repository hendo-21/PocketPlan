from sqlalchemy.orm import Mapped, mapped_column, session    # For model creation
from datetime import date                           # For transaction timestamp
from database import db                             # Gives access to db.Model to define database models
from sqlalchemy_serializer import SerializerMixin   # Allows for serialization of models (to_dict() method). Serialized models need to include in model def


# Define database model. SerializerMixin adds a .to_dict() method to model instances.
class Transactions(db.Model, SerializerMixin):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(default=date.today().strftime("%D"))
    amount: Mapped[float] = mapped_column(default=0.0)
    memo: Mapped[str] = mapped_column(default="")

    '''
    Adds a new transaction to the db.
    :param req_body: a dict containing the attributes for the creation of the new transaction
    :returns new_transaction: the newly created transaction - an instance of the Transactions class
    '''
    @classmethod
    def create_transaction(cls, req_body: dict):
        # Save the body fields in an dict
        tr_params = {
            'amount': req_body['amount'],
            'memo': req_body['memo']
        }
        if 'date' in req_body:
            tr_params['date'] = req_body['date']

        # Create a new transaction using the params
        new_transaction = Transactions(**tr_params)

        # Add the new transaction to the db and commit the change
        db.session.add(new_transaction)
        db.session.commit()

        # Return the new transaction
        return new_transaction
    

    '''
    Retrieves all transactions from the db.
    :returns trs_as_dict: an array of dicts representing each of the transaction instances
    '''
    @classmethod
    def get_all_transactions(cls):
        # Query for all transactions. Query returns a list
        all_trs = Transactions.query.all()

        # Add the instances as dicts to a new array
        trs_as_dict = []
        for transaction in all_trs:
            trs_as_dict.append(transaction.to_dict())

        # Return the array of transactions as dicts
        return trs_as_dict
    

    '''
    Updates a transaction.
    :param id: an int representing the unique id assigned by SQLite of the transaction to update
    :param req_body: a dict containing the attributes to be updated
    :returns: the updated transaction instance or None if not found
    '''
    @classmethod
    def update_transaction(cls, id: int, req_body: dict):
        tr_to_update = Transactions.query.get(id)
        if tr_to_update:
            tr_to_update.amount =  req_body['amount']
            db.session.commit()
        return tr_to_update