import sqlite3
con = sqlite3.connect("lecture.db")
cur = con.cursor()

sql = "select * from student"
result = cur.execute(sql)
print (f" first row: {result.fetchone()}")

sql = "insert into student values ('joe', 'DA', 'Male')"
cur.execute(sql)
cur.commit()
sql = "select * from student"
result = cur.excute(sql)
print (f" first row: {result.fetchone()}")

#sql = "select * from student"
#result = cur.execute(sql)
#print (f" first row: {result.fetchone()}")


con.close()