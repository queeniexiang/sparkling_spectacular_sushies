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

except:
    print "E R R O R -- check if:"
    print "(1)the database of the appropriate name is in the same directory"
    
    
#obtain all marks matched with each ID ('construct' step)
def match(): 
    try:
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

    except:
         print "E R R O R -- check if the database contains the proper tables (peeps and courses) with the proper fields"


         
#Computes the average of each student
def compute_average(): 
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
def print_dict(): 
    print "--------------------------------------"
    for ID in sorted(d.iterkeys()):
        name = d[ID][0]
        avg = d[ID][1]
        print "ID:", ID
        print "Name:",name
        print "Average:",avg
        print "--------------------------------------"



#Create a table of IDs and associated averages
def insert():
    try: 
        #To avoid adding duplicate values 
        c.execute("DROP TABLE IF EXISTS peeps_avg")

        #Create a new table with columns id and avg 
        c.execute("CREATE TABLE peeps_avg (id INTEGER, avg REAL)")

        #Add values to the table in their appropriate columns from the dictionary
        for ID in d:
            avg = d[ID][1]
            c.execute("INSERT INTO peeps_avg VALUES(" + str(ID) + "," + str(avg) + ")")
            #print ID,avg
    except:
        print "E R R O R -- check if the table was created and called properly"
        


#Add in a new row into the courses table 
def add_courses(new_ID, new_code, new_mark,):
    try:
        c.execute("INSERT INTO courses VALUES(?, ?, ?)", (new_code, new_mark, new_ID))

    except:
        print "E R R O R -- Check to see if inputs are valid"



#Add in a new grade for a student
def add_mark():
    end = False
    d_courses = {}
    d_courses_temp = c.execute("SELECT * FROM courses")
    
    for row in d_courses_temp:
        ID = int(row[2])
        print ID
        code = str(row[0])
        print code
        mark = long(row[1])
        print mark
        
        d_courses[ID] = [code,mark]
    

    #for person in d_courses:
        #print d_courses[person]
    
    #while (not end):
    #try: 
    input_id = int(raw_input("Which student are you looking for? Enter the ID: "))
    input_code = str(raw_input("Which course are you looking for? Enter the code: ")).lower() 
    input_mark = long(raw_input("What grade are you entering? Enter the grade: "))
    terminate = str(raw_input("Are you done? Type y for yes, n for no: ")).lower() 

    if(input_id not in d_courses or input_code not in d_courses[input_id]):
        add_courses(input_id, input_code, input_mark)

    if(input_code in d_courses[input_id]):
        d_courses[input_id][0] = input_mark
        c.execute("UPDATE courses SET mark = ? where id = ? AND code = ?", (input_mark, input_id, input_code))
        
                
    if terminate == "y":
        end = True
        #break
            
    #except:
    #print "E R R O R -- Incorrect format in input(s). Please try again."
    #break
    
    
        
        

        
        

#=======================TESTING AREA==========================
#add_courses("Chorus", 100, 10)
add_mark()

db.commit()
db.close()





