#sparkling_spectacular_sushies {Queenie Xiang and Michael Ruvinshteyn}
#SoftDev1 pd 7
#HW10 -- Average
#2017 - 10 - 16

import sqlite3   #enable control of an sqlite database

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

d = {} #dictionary for storing student data

#obtain all marks matched with each ID
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

#compute averages for each ID and replace marks with said average
for ID in d:
    marks = d[ID][1:len(d[ID])] #list of all marks for each ID
    avg = sum(marks) / float(len(marks)) #average of marks for each ID

    #remove all marks to be replaced by their average
    while len(d[ID]) > 1:
        d[ID].pop()
    d[ID].append(avg) #insert average to the value

    #print ID,":",d[ID]

#display IDs, names, and averages
print "--------------------------------------"
for ID in sorted(d.iterkeys()):
    name = d[ID][0]
    avg = d[ID][1]
    print "ID:", ID
    print "Name:",name
    print "Average:",avg
    print "--------------------------------------"
