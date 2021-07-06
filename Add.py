def add():
    print("             ********New Reminder********              ")
    fout=open("Reminder.txt","a")
    i=1
    while True:
        n=str(i)
        rem=input("Enter Reminder "+n+": ")
        fout.write(n+"). "+rem+"\n")
        ques1=input("Do you want to enter another reminder? Y/N")
        if ques1 == "Yy":
            i+=1
            continue
        else:
            break
    print("Reminder(s) entered")
    ques2=input("Press Any Key to go back to Homepage")
    return
