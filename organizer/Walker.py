#! /usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
from pathlib import Path
from organizer.SqlMixin import SqlMixin, SqlConnection
from organizer.utils import DB_DIR, DB_FILE

hashed = lambda x: hashlib.md5(x.read_bytes()).hexdigest()

class Track:
    def __init__(self,path):
        self.path = str(path)
        self.obj = Path(path)
        self.name = self.obj.name
        self.suffix = self.obj.suffix
        self.size = self.obj.stat().st_size

    def format_order(self):
        seq = [
            self.path,
            self.name,
            self.suffix,
            self.size
        ]
        return seq

    def format_output(self):
        dbdict = {
            "path" : self.path,
            "name" : self.name,
            "suffix" : self.suffix,
            "size" : self.size,
            "md5" : hashed(self.obj)
        }
        return dbdict


class Walker(SqlMixin):
    headers = ["path","name","suffix","size"]
    track = Track
    def __init__(self,dbfile=DB_FILE,table="table"):
        self.dbfile = Path(dbfile)
        if not self.dbfile.parent.exists():
            self.dbfile.parent.mkdir()

        self.table = table
        self.txt_file = None
        self.container = []
        self.cursor = SqlConnection(self.dbfile)
        self.configure_database()

    def get_all(self):
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

    def send_to_gui(self,item):
        item = Track(item)
        output = item.format_order()


    def walk(self,root,action):
        for item in root.iterdir():
            if item.is_file():
                action(item)
            else:
                self.walk(item,action)


