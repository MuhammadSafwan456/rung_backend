from rung.database import database

bot_number_collection = "bot_number"


def increment_bot_number(increment):
    read_filter = {}
    update_filter = {
        "$inc": {"number": increment}
    }
    data = database.database_find_and_modify(bot_number_collection, read_filter, update_filter, upsert=True)
    print("---------->", data)


def get_bot_number():
    increment_bot_number(1)
    read_filter = {}
    data = database.database_read_one(bot_number_collection, read_filter)
    print("************************888888", data)
    return data["number"]
