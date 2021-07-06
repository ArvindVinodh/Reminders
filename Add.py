def add():
    print("             ********New Reminder********              ")
    fout=open("Reminder.txt","a")
    I=1
    N=Line()
    while True:
        n=str(N)
        i=str(I)
        rem=input("Enter Reminder "+i+": ")
        fout.write(n+"). "+rem+"\n")
        ques1=input("Do you want to enter another reminder? Y/N")
        if ques1 in "Yy":
            I+=1
            N+=1
            continue
        else:
            break
    fout.close()
    print("Reminder(s) entered")
    ques2=input("Press Any Key to go back to Homepage")
    return

def Line():
    fin=open("Reminder.txt","r")
    count=len(fin.readlines())
    fin.close()
    return count+1
        
