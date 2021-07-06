from Add import *
from Retrieve import *
from Delete import *
import os.path
if os.path.isfile("Reminder.txt") != True:
    fout=open("Reminder.txt","a")
    fout.close()
def homepage():
    while True:
        print("*********************Reminders*********************")
        print()
        print("             ********Homepage********              ")
        print()
        print("Your Reminders:")
        retrieve()
        print()
        print("             ********Menu********              ")
        print("1.Add Reminder")
        print("2.Delete Reminder")
        print("3.Exit")
        ques=int(input("Enter your choice: "))
        if ques == 1:
            add()
        elif ques == 2:
            delete()
        else:
            return
homepage()


