#sparkling_spectacular_sushies {Queenie Xiang and Michael Ruvinshteyn}
#SoftDev1 pd 7
#HW10 -- Average
#2017 - 10 - 16

import sqlite3   #enable control of an sqlite database

#connect to the database
try:
    f = "discobandit.db"

    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    d = {} #dictionary for storing student data

except:
    print "E R R O R -- check if the database of the appropriate name is in the same directory"

    
    
'''The following three functions use a general 3-step method: construct, modify, display.
   1. The 'construct' step creates the keys within a dictionary and adds all
   respective data for each key (the key being the ID and the values being
   the name and the marks for the student). 
   2. The 'modify' step removes all marks for every student and replaces them 
   with a single value equal to the average of all of the student's marks. 
   3. The 'display' step shows the user the IDs, names, and averages of each 
   student.'''
 
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


         
#computes the average of each student ('modify' step)
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


'''The following four functions allow the user to insert a grade for an ID and course of their choice.
   insert() creates a new table for accessing the averages for their respective IDs much more easily.
   add_courses() adds the provided code and mark for the given ID (all are parameters)
   add_mark() allows the user to choose what mark gets inserted for which code and ID (utilizes add_course())
   print_avg() prints the peeps_avg table created by insert() and modified by add_mark()'''

#create a table of IDs and associated averages
def insert():
    try: 
        #to avoid adding duplicate values, remove any preexisting peeps_avg table
        c.execute("DROP TABLE IF EXISTS peeps_avg")

        #create a new table with columns id and avg 
        c.execute("CREATE TABLE peeps_avg (id INTEGER, avg REAL)")

        #add values to the table in their appropriate columns from the dictionary
        for ID in d:
            avg = d[ID][1]
            c.execute("INSERT INTO peeps_avg VALUES(?,?)",(ID,avg))
            #print ID,avg
    except:
        print "E R R O R -- check if the table was created and called properly"
        


#add in a new row into the courses table 
def add_courses(new_ID, new_code, new_mark,):
    try:
        c.execute("INSERT INTO courses VALUES(?, ?, ?)", (new_code, new_mark, new_ID))

    except:
        print "E R R O R -- Check to see if inputs are valid"



#add in a new grade for a student
def add_mark():
    success = False #boolean variable that determines whether the given ID is valid
    
    while True:
        #end function if user does not wish to add a grade
        terminate = str(raw_input("Would you like to add a grade? Type y for yes, n for no: ")).lower()

        while terminate != "y" and terminate != "n":
            terminate = raw_input("Please enter a valid input (y or n): ")
            
        if terminate == "n":
            break
            
        #collect valid ID
        while not success:
            try:
                input_id = int(raw_input("Which student are you looking for? Enter the ID: "))
                while input_id not in d:
                    input_id = int(raw_input("That ID is not in our database, please try again: "))
                success = True;
            except:
                print "Please enter a valid integral value"
        success = False #reset to False in case user wants to enter another grade
        
        input_code = str(raw_input("Which course are you looking for? Enter the code: ")).lower() #course to add grade for
        input_mark = long(raw_input("What grade are you entering? Enter the grade: ")) #grade for the given course ^
        

        #add course to courses table if the course was not previously there
        if(input_code not in d[input_id]):
            add_courses(input_id, input_code, input_mark)

        #update grade for course,ID if course already exists
        if(input_code in d[input_id]):
            d[input_id][0] = input_mark
            c.execute("UPDATE courses SET mark = ? WHERE id = ? AND code = ?", (input_mark, input_id, input_code))
                

#print peeps_avg table
def print_avg():
    values = c.execute("SELECT * FROM peeps_avg")
    for row in values:
        ID = row[0]
        avg = row[1]
        print ID," | ",avg

#=======================TESTING AREA==========================
#add_courses("Chorus", 100, 10)
#add_mark()

match()
compute_average()
print_dict()

print "\n\n"

insert()
print_avg()

add_mark()

db.commit()
db.close()





