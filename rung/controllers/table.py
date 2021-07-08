from rung.models.user import add_user, get_user_by_id
from rung.models.table import add_table
from rung.models.bot import get_bot_number
from rung.services.helper.errors import Error
import uuid


def join_table(user_id, table_capacity):
    table = None
    user = get_user_by_id(user_id)
    table_id = find_table(table_capacity, None)
    if table_id is None:
        table = create_new_table(table_capacity)
        if not table:
            raise Error(message="Something went wrong", status_code=400)
        table_id = table["id"]
        set_user_in_table(table_id, [user])
    print(table)


def find_table(total_capacity, space):
    return space


def create_new_table(table_capacity):
    table = {
        "id": str(uuid.uuid4()),
        "table_capacity": table_capacity,
        "users": []
    }
    add_table(table)
    table.pop("_id")
    return table


def set_user_in_table(table_id, *users):
    return True
