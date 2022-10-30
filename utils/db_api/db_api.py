import sqlite3

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
    
    async def check_uniq(funk):
        async def inner_error_check(self):
            try:
                funk()
            except sqlite3.IntegrityError:
                pass
        return inner_error_check

    @check_uniq
    async def add_new_info(self, add_where, add_what_info, exact_info):
        self.cursor.execute(f"INSERT INTO {add_where} ({add_what_info}) VALUES({exact_info})")
        self.connection.commit()
    

