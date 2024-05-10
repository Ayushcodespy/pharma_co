import pyodbc

class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-F82IRCQF;DATABASE=flaskapp;')
        self.cursor = self.conn.cursor()

    def get_items(self):
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        print(result)

    def set_items(self, arg1, arg2, arg3):
        self.cursor.execute("INSERT INTO user_info(email, name, password) VALUES (?, ?, ?)",(arg1, arg2, arg3))
        self.conn.commit()







db = ItemDatabase()
# db.get_items()
# db.set_items('ayush.jnv54@gmail.com', 'Ayush Patel', 'ayush7085')
