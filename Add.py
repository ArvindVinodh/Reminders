def add(N):
    fout=open("Reminder.txt","a")
    for i in range(N):
        n=str(i+1)
        rem=input("Enter Reminder "+n+": ")
        fout.write(n+"). "+rem+"\n")
    print("Reminder entered")
    ques=input("Press Any Key to Continue")
    
add(2)
