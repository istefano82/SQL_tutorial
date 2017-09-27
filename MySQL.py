from bs4 import BeautifulSoup
import time
import urllib2
from sql_connector import connection



def parse_links():

    req = urllib2.urlopen('http://www.bloombergtv.bg/rss/main')


    xml = BeautifulSoup(req, 'xml')

    c, conn = connection()
    for item in xml.findAll('link')[3:]:
        url = item.text
        c.execute("SELECT * FROM links WHERE link = (%s)",
                  (url,))

        rows = c.fetchall()

        if len(rows) == 0:
            c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
                      (time.time(), url))
            conn.commit()
            print("Found a new link!")
        else:
            print("Link already in database")
        time.sleep(10)

        

    conn.close()

while True:
    parse_links()