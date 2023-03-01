# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#
import calendar
from datetime import date
from datetime import time
from datetime import datetime

def countdays(theyear, themonth, whichday):
    daycount = 0
    weeklist = calendar.monthcalendar(theyear, themonth)
    for week in weeklist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

print ("--Day Counter Program--\n")

run = True
while(run):
    try:    
        print ("Which day of the week do you like to count?")
        days = ["0: Monday","1: Tuesday","2: Wednesday","3: Thursday","4: Friday", "5: Saturday", "6: Sunday"]
        for d in days:
            print (d)
        print ("Or 'exit' to quit")
        
        dayoftheweek  = input("?")
        if dayoftheweek == "exit":
            print ("\n-----------\n")
            run = False
            break
        day = int(dayoftheweek)

        yearanswer = input("Enter year: ")
        year = int(yearanswer)

        monthanswer = input("Enter month: ")
        month = int(monthanswer)

        result = countdays(year, month, day)
        print ("There are " + str(result) + " of those days in the month and year specified")
        print ("\n-----------\n")
    
    # except Exception as e:
    #     print (e)
    #     print ("Sorry, that's not valid input")
    
    except Exception as e:
        print(e)
        print("Sorry, that's not valid input")

    finally: 
        print ("Thank you for counting with us, see you next time.")
        run = False
