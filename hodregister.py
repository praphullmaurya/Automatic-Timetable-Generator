#!C:/ProgramData/Anaconda3/python.exe
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:21:26 2019

@author: pmjnp
"""

# Import modules for CGI handling 
import cgi, cgitb 
import dbcode
# Create instance of FieldStorage 
form = cgi.FieldStorage()
print("Content-type: text/html \r\n\r\n")

# Get data from fields
fname = form.getvalue('fullname')
email  = form.getvalue('email')
mobno = form.getvalue('mobile')
deptt = form.getvalue('dropdown')
passwd = form.getvalue('password')
# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO users(fname,email,mobno,deptt,passwd,ishod) VALUES ('{0}','{1}','{2}','{3}','{4}',0);".format(fname,email,mobno,deptt,passwd)
dbcode.db.runQuery(sql)
#print(sql)




# disconnect from server
