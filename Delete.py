from Retrieve import *
import os
def delete():
    print("             ********Delete Reminder********              ")
    print("Your Reminders:")
    retrieve()
    n=int(input("Which Reminder do you want to Delete? "))
    
    fin=open("Reminder.txt","r")
    r=fin.readlines()
    R=[]
    for k in range(len(r)):
        if k!=(n-1):
            R.append(r[k])
            
    Rem=[]
    for i in R:
        Rem.append(i[4:])

    l=[]
    for j in Rem:
        new_Rem=""
        for k in j:
            if k not in "\n":
                new_Rem+=k
        l.append(new_Rem)
    fin.close()
    os.remove("Reminder.txt")

    fout=open("Reminder.txt","a")
    I=1
    for k in l:
            i=str(I)
            fout.write(i+"). "+k+"\n")
            I+=1
    fout.close()
    
    
    
