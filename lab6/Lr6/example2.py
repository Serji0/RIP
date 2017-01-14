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

c.execute("INSERT INTO lr6_user (first_name, age, email, last_name) VALUES (%s, %s, %s, %s);",
          ('user2', 2, 'example2@email.com', 'Пользователь № 2'))
db.commit()
c.execute('Select * from lr6_user;')
goods = c.fetchall()
for i in goods:
    print(i)
c.close()
db.close()
