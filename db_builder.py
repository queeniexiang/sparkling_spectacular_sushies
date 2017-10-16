#Michael Ruvinshteyn
#SoftDev1 pd 7
#HW09 -- No Treble
#2017 - 10 - 14

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#---------------------courses.csv--------------------------
try:
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)") #creates table according to CSV
    with open("courses.csv") as csvfile:
        r = csv.DictReader(csvfile)
        for row in r:
            #creates variable for each item in the row
            code = row['code']
            mark = row['mark']
            idee = row['id']
            
            command = "INSERT INTO courses VALUES ('" + code + "'," + mark + "," + idee + ")" #inserts variables above into table
            c.execute(command)
except:
    print "ERROR FOR courses.csv"
#----------------------------------------------------------
    
#----------------------peeps.csv---------------------------
try:
    c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)") #creates table according to CSV
    with open("peeps.csv") as csvfile:
        r = csv.DictReader(csvfile)
        for row in r:
            #creates variable for each item in the row
            name = row['name']
            age = row['age']
            idee = row['id']
            
            command = "INSERT INTO peeps VALUES ('" + name + "'," + age + "," + idee + ")" #inserts variables above into table
            c.execute(command)
except:
    print "ERROR FOR peeps.csv"
#----------------------------------------------------------
    
#-------------------------DIAG-----------------------------
print "\n\n\n"
    
print "courses table:"
rows = c.execute("SELECT * FROM courses") #obtains every row in courses table as a list
for row in rows:
    code = row[0]
    mark = str(row[1])
    idee = str(row[2])
    print " | ".join([code,mark,idee]) #prints every row in courses table

print "\n\n"

print "peeps table:" #obtains every row in peeps table as a list
rows = c.execute("SELECT * FROM peeps")
for row in rows:
    name = row[0]
    age = str(row[1])
    idee = str(row[2])
    print " | ".join([name,age,idee]) #prints every row in peeps table
#----------------------------------------------------------

#==========================================================
db.commit() #save changes
db.close()  #close database


