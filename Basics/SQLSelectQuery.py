import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="classicmodels")
    curs = con.cursor()
    # curs.execute("select * from students1")
    # for row in curs:
    #     print(row[0], row[1])

    print()
    curs.execute("select * from caldata")
    for row in curs:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

    con.close()
except:
    print("connection unsuccessful.......")

print("Finished.........")
