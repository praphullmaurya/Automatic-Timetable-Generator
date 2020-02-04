#!C:/ProgramData/Anaconda3/python.exe
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 21:19:02 2019

@author: pmjnp
"""

import mysql.connector
import cgi, cgitb 

class data:
    def __init__(self):
        form = cgi.FieldStorage()
        print("Content-type: text/html \r\n\r\n")
        self.email = form.getvalue('email')
        self.passwd = form.getvalue('password')

        #self.usernam = input("Enter user name: ")
        #self.password= input("Enter Password: ")

a=data()
mydb = mysql.connector.connect(
         host='localhost',
         user='root',passwd='',
         database='timetableschedular')


loadname= "select email from users where email=%s and passwd = %s"

mycursor=mydb.cursor()
mycursor.execute(loadname,(a.email,a.passwd,))
c=mycursor.fetchall()
print(len(c))
#print(c[0]);

if len(c)==1:
    print("<script>window.location='hod.html';</script>")

else:
    print("hello")
    
mydb.commit()
mydb.close()
