#Counting Organizations
#This application will read the mailbox data (E_mbox.txt) and count the number of email messages per organization
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
#CREATE TABLE Counts (org TEXT, count INTEGER)

import sqlite3

conn = sqlite3.connect('E_emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'E_mbox.txt'
fh = open(fname)
adding = 0
for line in fh:
    if not line.startswith('From: '): continue
    adding += 1
    pieces = line.split()
    org = pieces[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    if adding < 10:continue
    adding = 0
    conn.commit()
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
