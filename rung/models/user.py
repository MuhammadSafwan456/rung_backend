from rung.database import database

user_collection = "user"


def add_user(user):
    """add user in database"""
    database.database_write_one(user_collection, user)


def get_user_by_id(_id):
    read_filter = {"id": _id}
    user = database.database_read_one(user_collection, read_filter)
    return user
