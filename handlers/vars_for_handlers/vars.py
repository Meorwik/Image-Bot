
temp_category_name = "None"
message_id_to_del = 0


async def set_temp_category(name: str):
    global temp_category_name
    temp_category_name = name


async def get_temp_category():
    global temp_category_name
    return temp_category_name


async def set_message_id_to_edit(message_id: int):
    global message_id_to_del
    message_id_to_del = message_id


async def get_message_id_to_edit():
    global message_id_to_del
    return message_id_to_del
