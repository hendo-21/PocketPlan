from sqlalchemy.orm import Mapped, mapped_column    # For model creation
from datetime import date                           # For transaction timestamp
from database import db                             # Gives access to db.Model to define database models
from sqlalchemy_serializer import SerializerMixin   # Allows for serialization of models (to_dict() method). Serialized models need to include in model def
from sqlalchemy import Date, func, select

# Define Summary database model. SerializerMixin adds a .to_dict() method to model instance.
class Summaries(db.Model, SerializerMixin):
    __tablename__ = "summary"

    id: Mapped[int] = mapped_column(primary_key=True)
    budget: Mapped[int] = mapped_column(default=600)
    last_updated: Mapped[date] = mapped_column(default=date.today)

    '''
    Create a summary.
    '''
    @classmethod
    def create_summary(cls):
        new_summary = cls()
        db.session.add(new_summary)
        db.session.commit()
        return new_summary

    '''
    Get summary.
    '''
    @classmethod
    def get_summary(cls, id: int):
        current_summary = cls.query.get(id)
        if current_summary:
            return current_summary
        return None
    
    '''
    Get all summaries.
    '''
    @classmethod
    def get_all_summaries(cls):
        all_summaries = cls.query.all()
        as_dict_array = []
        for summary in all_summaries:
            as_dict_array.append(summary.to_dict())
        return as_dict_array
        
    '''
    Update summary
    '''
    @classmethod
    def update_summary(cls, id: int, req_body: dict):
        current_summary = cls.query.get(id)
        if current_summary:
            current_summary.budget, current_summary.last_updated = req_body['budget'], date.fromisoformat(req_body['last_updated'])
            db.session.commit()
            return current_summary
        return None
    
    '''
    Delete summary
    '''
    @classmethod
    def delete_summary(cls, id: int):
        to_delete = cls.query.get(id)
        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return 0
        return 1
    
    '''
    Delete all summaries
    '''
    @classmethod
    def delete_all_summaries(cls):
        db.session.query(cls).delete()
        db.session.commit()


# Define Transactions database model. SerializerMixin adds a .to_dict() method to model instances.
class Transactions(db.Model, SerializerMixin):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date_added: Mapped[date] = mapped_column(Date, default=date.today)
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
            # Build the formatted string from body
        #    tr_params['date'] = req_body['date'][5] + req_body['date'][6] + '/' + req_body['date'][8] + req_body['date'][9] + '/' + req_body['date'][2] + req_body['date'][3]
            # Parse to date object
            parsed = date.fromisoformat(req_body['date'])
            tr_params['date_added'] = parsed

        # Create a new transaction using the params then add to db
        new_transaction = cls(**tr_params)
        db.session.add(new_transaction)
        db.session.commit()

        return new_transaction
    
    '''
    Retrieves all transactions from the db, sorted in ascending order by date.
    :returns trs_as_dict: an array of dicts representing each of the transaction instances
    '''
    @classmethod
    def get_all_transactions(cls):
        # Query for all transactions and order by date (ascending). Query returns a list
        all_trs = cls.query.order_by(cls.date_added).all()

        # Add the instances as dicts to a new array
        trs_as_dict = []
        for transaction in all_trs:
            trs_as_dict.append(transaction.to_dict())

        # Return the array of transactions as dicts
        return trs_as_dict

    '''
    Retrieves one transaction.
    :param id:
    :returns: 
    '''
    @classmethod
    def get_transaction(cls, id: int):
        transaction = cls.query.get(id)
        return transaction

    '''
    Updates a transaction.
    :param id: an int representing the unique id assigned by SQLite of the transaction to update
    :param req_body: a dict containing the attributes to be updated
    :returns: the updated transaction instance or None if not found
    '''
    @classmethod
    def update_transaction(cls, id: int, req_body: dict):
        tr_to_update = cls.query.get(id)
        if tr_to_update:
            tr_to_update.amount =  req_body['amount']
            db.session.commit()
            return tr_to_update
        return None

    '''
    Delete all transactions.
    '''
    @classmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    '''
    Delete transaction by Id.
    :param id: id of the transaction - automatically assigned
    :returns:
    '''
    @classmethod
    def delete_one(cls, id: int):
        to_delete = cls.query.get(id)
        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return 0    

    '''
    Sums the values in amount column and returns the result. Uses SQLAlchemy core aggregate method SUM.
    :returns result: a float representing the sum of values in "amount" column of transactions table or 0.
    '''
    @classmethod
    def get_total_spend(cls):
        # Construct SQL statement
        sql_statement = select(func.sum(cls.amount))

        # Execute sends the statement to the DBMS and runs it. Scalar extracts the value without iterating over returned query result.
        result = db.session.execute(sql_statement).scalar()
        if result:
            return result
        return 0
    
    '''
    Computes the remaining funds available.
    :param budget: an int representing the user's stated monthly budget
    :returns: a float representing the remaining amount available to spend
    '''
    @classmethod
    def get_remaining(cls, budget: int):
        spent = cls.get_total_spend()
        return budget - spent