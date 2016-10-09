#coding:utf-8

import MySQLdb, datetime

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "001828", \
                     db = "dic", charset = "utf8")

cursor = db.cursor()

while True:
    startTime = datetime.datetime.now()
    print startTime
    wordInput = raw_input("word:")
    wordQuery = "select * from dic where Word like '%" + wordInput + "%'"
    print wordQuery
    cursor.execute(wordQuery)

    results = cursor.fetchall()
    for row in results:
        print row[0], '->', row[1], '->', row[2]

    endTime = datetime.datetime.now()
    print 'Cost time :', endTime - startTime
    print '-----------------------'
    
    

