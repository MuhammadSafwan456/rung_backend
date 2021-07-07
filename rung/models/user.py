from rung.database import database

user_collection = "user"


def add_user(user):
    """add user in database"""
    database.database_write_one(user_collection, user)
