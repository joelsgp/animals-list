#!/usr/bin python3

import sqlite3


con = sqlite3.connect("lines.db")

con.execute("CREATE TABLE animals (name STRING);")
con.commit()

with open("lines.txt") as lines_file:
    for line in lines_file.readlines():
        line = line.removesuffix("\n")
        con.execute("INSERT INTO animals VALUES (?);", (line,))
con.commit()

con.close()
