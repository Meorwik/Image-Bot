import sqlite3

def check_uniq(funk):
    async def inner_error_check(*args):
        try:
            await funk(*args)
        except sqlite3.IntegrityError:
            pass
    return inner_error_check

class DataBaseManager:
    async def connect(self, db_name):
        con = sqlite3.connect(f"data/DataBase/{db_name}.db")
        cur =con.cursor()
        self.connection = con 
        self.cursor = cur

    async def disconnect(self):
        self.cursor.close()
        self.connection.close()
        
    async def get_info(self, get_what, get_from):
        self.cursor.execute(f"SELECT {get_what} FROM {get_from}")
        return self.cursor.fetchall()

    @check_uniq
    async def add_new_info(self, add_where, add_what_info, exact_info):
        self.cursor.execute(f"INSERT INTO {add_where} ({add_what_info}) VALUES({exact_info})")
        self.connection.commit()
        
        
async def getting_info_from_the_same_databse(db_name: str, get_what: str, get_from: str):
    DataBaseManagerObject = DataBaseManager()
    await DataBaseManagerObject.connect(f"{db_name}")
    db = await DataBaseManagerObject.get_info(f"{get_what}", f"{get_from}")
    await DataBaseManagerObject.disconnect()
    del DataBaseManagerObject
    return db
