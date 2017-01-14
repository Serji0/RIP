import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='dbuser',
    passwd='123',
    db='first_db',
    use_unicode=True,
    charset='utf8'
)

c = db.cursor()

c.execute("INSERT INTO lr6_good (name, description) VALUES (%s, %s);", ('Товар 3', 'Товар № 3'))
db.commit()
c.execute('Select * from lr6_good;')
goods = c.fetchall()
for i in goods:
    print(i)
c.close()
db.close()
