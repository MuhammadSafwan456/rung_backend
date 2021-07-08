from rung.database import database

table_collection = "table"


def add_table(table):
    """add user in database"""
    database.database_write_one(table_collection, table)
