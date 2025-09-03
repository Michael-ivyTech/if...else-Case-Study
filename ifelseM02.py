'''
Michael Baker
ifelseM02.py

This program accepts a student's first and last name and GPAs, then tests whether the student qualifies for the Dean's List or Honor Roll. This is done by using a while loop that continuously asks for the last name, first name, and GPA until the user inputs 'ZZZ' for the last name.

'''

        
while (True):
    last_name = input("What is the student's last name? ")
    
    if (last_name == "ZZZ"): 
        
        break
    first_name = input("What is the student's first name? ")
    gpa = input("What is " + first_name + "'s GPA? ")
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
    
    print(first_name + " " + last_name + " with a GPA of " + str(gpa) + ", qualifies for " + stu_roll)

'''
Test Input:
Will
John
4.0
Orta
Jack
2.0
Baker
Will
3.0
VanGor
Jenna
3.33
Carl
Carl
-0.66
Layman
Gabe
5.45
ZZZ

'''