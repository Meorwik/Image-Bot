import json

with open('workflow_2\data\config.ini', 'r') as file:
    tg_data = json.load(file)

with open("workflow_2\data\Her_special_data\SomeSpecialData", "r") as file:
    id = int(file.readline())

admins  = []
for adm in tg_data["admins"].split():
    admins.append(adm)

BOT_TOKEN = tg_data["token"]
ADMINS = admins
HER_ID = id


async def IS_ADMIN(id):
    if int(ADMINS[0]) == id:
        return True
    else:
        return False


async def IS_HER(id):
    if int(HER_ID) == id:
        return True
    else:
        return False