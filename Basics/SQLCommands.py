import mysql.connector

insert_query = "insert into students1 values(105, 'Mary')"
update_query = "update students1 set sname = 'abc' where sid =103"
delete_query = "delete from students1 where sid = 105"

# create connection
con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="classicmodels")
curs = con.cursor()

# inertion
# curs.execute(insert_query)
# curs.execute(update_query)
# curs.execute(delete_query)
con.commit()

con.close()
