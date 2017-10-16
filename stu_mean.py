import sqlite3   #enable control of an sqlite database

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

d = {}
try:
    peep_values = c.execute("SELECT id,name FROM peeps")
    for row in peep_values:
        print str(row[0]),row[1]
    course_values = c.execute("SELECT id,mark FROM courses")
    for row in course_values:
        print str(row[0]),str(row[1])
    
        
except:
    print "E R R O R"
