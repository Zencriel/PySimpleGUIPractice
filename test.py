import sqlite3

connect = sqlite3.connect("records.db")

forgraph = connect.execute("Select Percentage from Marks")
percentagess = forgraph.fetchall()

print (percentagess)

for eachvalue in percentagess:
    print (eachvalue[0])


