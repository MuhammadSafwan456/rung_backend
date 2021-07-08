import uuid
from rung.models.user import add_user
from rung.models.bot import get_bot_number
from rung.services.helper.errors import Error


def create_user(user):
    if not user["name"]:
        if user["bot"]:
            user["name"] = generate_bot_name()
        else:
            raise Error(message="Name not found", status_code=400)
    if not user.get("id", None):
        user["id"] = str(uuid.uuid4())
    if not user.get("coins", None):
        user["coin"] = 0  # TODO: get it from config
    add_user(user)
    user.pop("_id")
    return user


def generate_bot_name():
    number = get_bot_number()
    prefix = "Bot"  # TODO : Read From config
    return str(prefix + "_" + str(number))
