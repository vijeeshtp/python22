import mysql.connector as c

con = c.connect(
    host="localhost",
    user="root",
    passwd="admin123",
    database="db22")

print (con)

'''
qry="select * from product order by price;"

cur =con.cursor();
cur.execute(qry)
print(cur.fetchone())
print(cur.fetchone())

'''

try :
    qry = "insert into product values ('200','test',20000)"
    cur =con.cursor();
    cur.execute(qry)


    qry = "insert into product values ('300','test',20000)"
    cur.execute(qry)

    con.commit()
except Exception as e :
    print(e)
    con.rollback()