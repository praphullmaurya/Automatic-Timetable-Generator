import mysql.connector

class db:
    __host = "localhost"
    __user = "root"
    __passwd = ""
    __dbName = 'timetableschedular'
    
    @staticmethod    
    def createDb():
        mc=db.runQueryres("show databases like '{0}'".format(db.__dbName))
        if(len(mc)==0):
            db.runQuery("create database {0}".format(db.__dbName))
            db.__createTables()
    
    @staticmethod  
    def __createTables():
        db.runQuery("create table subinfo( \
                                             id int(10) AUTO_INCREMENT PRIMARY KEY,\
                                             subtype VARCHAR(10) NOT NULL,\
                                             subCode VARCHAR(10) UNIQUE NOT NULL,\
                                             subName VARCHAR(50) NOT NULL,\
                                             sem INT(5) NOT NULL,\
                                             dept VARCHAR(20) NOT NULL)")
    
        db.runQuery("create table users( \
                                           id int(10) AUTO_INCREMENT PRIMARY KEY,\
                                           fname VARCHAR(30) UNIQUE NOT NULL,\
                                           email VARCHAR(50) NOT NULL,\
                                           mobno VARCHAR(15) NOT NULL,\
                                           deptt VARCHAR(20) NOT NULL,\
                                           passwd VARCHAR(30) NOT NULL,\
                                           ishod int(1) NOT NULL DEFAULT 0 )")

    def runQuery(sql):
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                )
        mc = mydb.cursor()
        m=db.runQueryres("show databases like '{0}'".format(db.__dbName))
        if(len(m)==1):
            mc.execute("use {0}".format(db.__dbName))
        mc.execute(sql)
        mydb.commit()
        mydb.close()
        
    def runQueryres(sql):
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                )
        mc = mydb.cursor()
        
        mc.execute(sql)
        mydb.close()
        return mc.fetchall()
    

    
db.createDb()
#db.runQuery("drop database timetableschedular")
    