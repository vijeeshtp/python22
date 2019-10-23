
import mysql.connector as c;

def getConnection():
    con = c.connect(
        host="localhost",
        user="root",
        passwd="admin123",
        database="db22")
    print (con)
    return con

def getAllProduct():
    qry = "select * from product"
    cur= getConnection().cursor()
    cur.execute(qry)
    return cur.fetchall()

def getProductById(pid):
    qry = "select * from product where id= %s"
    cur = getConnection().cursor()
    cur.execute(qry, (id,))
    return cur.fetchone()

def deleteProductById(pid):
    qry = "delete  from product where id= %s"
    con = getConnection()
    cur = con.cursor()
    cur.execute(qry, (pid,))
    con.commit()

def insertProduct(a, b, c):
    qry= "insert into product values (%s, %s, %s)"
    con= getConnection()
    cur = con.cursor()
    cur.execute(qry, (a,b, c))
    con.commit()


def insertAllProduct(plist):
    qry= "insert into product values (%s, %s, %s)"
    con= getConnection()
    cur = con.cursor()
    cur.executemany(qry, plist)
    con.commit()

def updateProduct (id, name, price):
    qry = "update  product set " \
          "pname= %s ," \
          "price = %s " \
          "where id= %s"
    con = getConnection()
    cur = con.cursor()
    cur.execute(qry, ( name, price,id))
    con.commit()


def main ():

    products = [("x1", "pppppp", 100),
                ("x2", "pppppp", 100),
                ("x3", "pppppp", 100),
                ("x4", "pppppp", 100),
                ("x5", "pppppp", 100),
                ("x6", "pppppp", 100)]

    #insertAllProduct(products)

    #updateProduct("x1", "ssssssss", 200)
    deleteProductById("x6")

main ()

