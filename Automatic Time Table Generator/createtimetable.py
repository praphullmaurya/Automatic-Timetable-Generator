# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:26:20 2019

@author: pmjnp
"""
import mysql.connector

class sub:
    def __init__(self,subCode,facCode,subcount):
        self.subcount=int(subcount)
        self.subCode=subCode
        self.facCode=facCode
        self.isAssign=False
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                )
        mc = mydb.cursor()
        mc.execute("use timetableschedular")
        mc.execute("select * from subinfo where subCode = '{0}'".format(subCode))
        res = mc.fetchall()
        mydb.close()
        for row in res:
            self.type = row[1]
            self.subcode = row[2]
            self.subname = row[3]
            self.sem = row[4]
            self.dept = row[5]
    def issubcount(self):
        if self.subcount>0:
            return True
        return False

def sortsub(l):
    subject = {}
    for i in range(0,len(l)):
        if(l[i].sem in subject):
            subject[l[i].sem].append(l[i])
        else:
            subject[l[i].sem]=[]
            subject[l[i].sem].append(l[i])
    return subject
        
       

ts = { "ts1" : "9:30AM-10:20AM", "ts2" : "10:20AM-11:10AM", "ts3" : "11:10AM-12:00PM",
       "ts4" : "12:00PM-12:50PM", "ts5" : "02:00PM-02:50PM", "ts6" : "02:50PM-03:40PM",
       "ts7" : "03:40PM-04:30PM" }



