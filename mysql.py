import MySQLdb

def connect():
	return MySQLdb.connect (host="localhost", user="root", passwd="22546", db="rfid")

def newentry(uid, itemname, itemlocation):
	db = connect()
	cur = db.cursor()
	cur.execute("""INSERT INTO itemlocation (uid, name, location) VALUES(%s, %s, %s)""",(uid, itemname, itemlocation))
	db.commit()
	db.close()
	
