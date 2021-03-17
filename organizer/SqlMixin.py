import sqlite3

class SqlMixin:

    def create_table(self,table_name,headers):
        with self.cursor as cursor:
            statement = f'CREATE TABLE {table_name} ({", ".join(headers)})'
            try:
                cursor.execute(statement)
            except sqlite3.OperationalError:
                pass #table already exists
        return

    def select_all(self,table):
        with self.cursor as cursor:
            statement = f"SELECT * FROM {table}"
            r = cursor.execute(statement)
            rows = r.fetchall()
        return rows

    def select_all_where(self,table,field,val):
        with self.cursor as cursor:
            statement = f"SELECT * FROM {table} WHERE {field} = ?"
            r = cursor.execute(statement,(val,))
            rows = r.fetchall()
        return rows

    def add_row(self,table,columns,values,size):
        with self.cursor as cursor:
            vals = ("?, "*size)[:-2]
            statement = f"INSERT INTO {table} ({columns}) VALUES ({vals})"
            cursor.execute(statement,values)
        return

class SqlConnection:
    def __init__(self,fname):
        self.path = fname
        self.init_connection()

    def init_connection(self):
        connection = sqlite3.connect(str(self.path))
        connection.close()

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self,*args,**kwargs):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

