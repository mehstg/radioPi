import sqlite3
dbconn = sqlite3.connect('radioPi.db')
c = dbconn.cursor()

for row in c.execute('SELECT * FROM pi_stations'):
        print row
