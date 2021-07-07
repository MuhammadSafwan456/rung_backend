import uuid
from rung.models.user import add_user
from rung.models.bot import get_bot_number


def create_user(user):
    if not user["name"]:
        if user["bot"]:
            user["name"] = generate_bot_name()
        else:
            print("ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRROR")
            return {"Error": "Error"}

    if not user.get("id", None):
        user["id"] = str(uuid.uuid4())
    add_user(user)


def generate_bot_name():
    number = get_bot_number()
    prefix = "Bot"  # TODO : Read From config
    return str(prefix + "_" + str(number))
