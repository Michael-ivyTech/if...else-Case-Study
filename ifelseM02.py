'''
Michael
ifelseM02.py

This program accepts a student's first name and GPAs, then tests whether the student qualifies for the Dean's List or Honor Roll. This is done by using a while loop that continuously asks for the name and GPA until the user inputs 'ZZZ'.

'''

        
while (True):
    name = input("What is the student's first name? ")
    
    if (name == "ZZZ"): 
        break

    gpa = input("What is " + name + "'s GPA? ")
    gpa = float(gpa)
    if (gpa < 0):
        print("Please enter a valid GPA.")
        continue
    elif (gpa > 5.0):
        print("Please enter a valid GPA.")
        continue

    stu_roll = None
    
    if (gpa >= 3.5):
        stu_roll = "Dean's List"
    elif (gpa >= 3.25):
        stu_roll = "Honor Roll"
    else:
        stu_roll = "neither the Dean's List or Honor Roll."
    
    print(name + " with a GPA of " + str(gpa) + ", qualifies for " + stu_roll)

'''
Test Input:
John
4.0
Jack
2.0
Will
3.0
Jenna
3.33
Carl
-0.66
Gabe
5.45
ZZZ

'''