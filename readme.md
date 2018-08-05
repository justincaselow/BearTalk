Snippet to query sqlite3 database

import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('select * FROM sqlite_master') # all tables
res=c.execute('select * FROM ui_message')