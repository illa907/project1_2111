import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
connection.commit()
connection.close()
