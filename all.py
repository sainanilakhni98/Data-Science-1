import MySQLdb as sql
try:
    db = sql.connect(host="172.25.5.10", port=3306, user="yogesh", password="redhat", database="python")
    cur=db.cursor()
except Exception as e:
    print("checkdatabase connection")
    exit(0)
cmd ="select * from student;"
cur.execute(cmd)
data=cur.fetchall()
print("id\tname")
for each_tuple in data:
    print(*each_tuple,sep='\t')
cur.close()
db.close()

