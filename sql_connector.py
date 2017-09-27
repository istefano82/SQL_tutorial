import MySQLdb



def connection():
	conn = MySQLdb.connect(host='localhost',
						   user='root',
						   passwd='ivailo82',
						   db='EpicDB' )

	c = conn.cursor()
	return c, conn

if __name__ == '__main__':
	c, conn = connection()
	print(' it worked!')