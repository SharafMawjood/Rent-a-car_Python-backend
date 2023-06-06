import sqlite3

con = sqlite3.connect('cab_db.db')
cur = con.cursor()
cur.execute("""CREATE TABLE vehicle()""")

