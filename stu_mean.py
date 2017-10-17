#sparkling_spectacular_sushies {Queenie Xiang and Michael Ruvinshteyn}
#SoftDev1 pd 7
#HW10 -- Average
#2017 - 10 - 16

import sqlite3   #enable control of an sqlite database

'''The code below uses a general 3-step method: construct, modify, display.
   1. The 'construct' step creates the keys within a dictionary and adds all
   respective data for each key (the key being the ID and the values being
   the name and the marks for the student). 
   2. The 'modify' step removes all marks for every student and replaces them 
   with a single value equal to the average of all of the student's marks. 
   3. The 'display' step shows the user the IDs, names, and averages of each 
   student.'''

try:
    f = "discobandit.db"

    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    d = {} #dictionary for storing student data

    #obtain all marks matched with each ID ('construct' step)
    values = c.execute("SELECT peeps.id,name,mark FROM peeps,courses WHERE peeps.id = courses.id")
    for row in values:
        ID = row[0]
        name = str(row[1])
        mark = row[2]

        #if ID is not in the dictionary yet, create a key for it
        if ID not in d:
            d[ID] = [name,mark]
        #otherwise, add to the key with the proper ID
        else:
            d[ID].append(mark)

        #print ID,":",d[ID]
    
    #print "\n"

    #compute averages for each ID and replace marks with said average ('modify' step)
    for ID in d:
        marks = d[ID][1:len(d[ID])] #list of all marks for each ID
        avg = sum(marks) / float(len(marks)) #average of marks for each ID

        #remove all marks to be replaced by their average
        while len(d[ID]) > 1:
            d[ID].pop()
        d[ID].append(avg) #insert average to the value

        #print ID,":",d[ID]

    
    #display IDs, names, and averages ('display' step)
    print "--------------------------------------"
    for ID in sorted(d.iterkeys()):
        name = d[ID][0]
        avg = d[ID][1]
        print "ID:", ID
        print "Name:",name
        print "Average:",avg
        print "--------------------------------------"
except:
    print "E R R O R -- check if:"
    print "(1)the database of the appropriate name is in the same directory"
    print "(2)the database contains the proper tables (peeps and courses) with the proper fields"

c.execute("CREATE TABLE IF NOT EXISTS peeps_avg (id INTEGER, avg REAL)")
for ID in d:
    avg = d[ID][1]
    c.execute("INSERT INTO peeps_avg VALUES(" + str(ID) + "," + str(avg) + ")")
    print ID,avg
