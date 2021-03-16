#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
import hashlib
from pathlib import Path
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))


dbfile = Path(os.getcwd()) / "data" / "sqlite3.db"
sql3 = sqlite3

hashed = lambda x: hashlib.md5(x.read_bytes()).hexdigest()

class Track:
    def __init__(self,path):
        self.path = str(path)
        self.obj = Path(path)
        self.name = self.obj.name
        self.suffix = self.obj.suffix
        self.size = self.obj.stat().st_size

    def format_output(self):
        dbdict = {
            "path" : self.path,
            "name" : self.name,
            "suffix" : self.suffix,
            "size" : self.size,
            "md5" : hashed(self.obj)
        }
        return dbdict

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


class Walker(SqlMixin):
    headers = ["path","name","suffix","size","md5"]
    def __init__(self,root1=None,root2=None,dbfile=None,table="tracks"):
        self.root1 = root1
        self.root2 = root2

        self.dbfile = dbfile
        if not self.dbfile.parent.exists():
            self.dbfile.parent.mkdir()

        self.table = table
        self.txt_file = None
        self.container = []
        self.cursor = SqlConnection(self.dbfile)
        self.configure_database()

    def sql_select_all(self):
        return list(self.select_all(self.table))

    def configure_database(self):
        self.create_table(self.table,self.headers)

    def save_to_db(self,item):
        item = Track(item)
        output = item.format_output()
        columns, values = [] , []
        for k,v in output.items():
            columns.append(k)
            values.append(v)
        size = len(output)
        columns = ", ".join(columns)
        self.add_row(self.table,columns,values,size)

    def compare(self,item):
        item = Track(item)
        rows = self.select_all_where(self.table,"name",item.name)
        for row in rows:
            if row["size"] == item.size and row["md5"] == hashed(item.obj):
                return
        self.container.append(item)
        if not self.txt_file:
            self.txt_file = open("IncludeTracks.txt","a",errors="replace")
        self.txt_file.write(item.path + "\n")

    def walk(self,root,action):
        for item in root.iterdir():
            if item.is_file():
                action(item)
            else:
                self.walk(item,action)


# if __name__ == '__main__':
    # walker = Walker(DROOT,CROOT,dbFile,table="tracks")
    # walker.walk(DROOT,walker.save_to_db)
    # walker.walk(CROOT,walker.compare)
