def retrieve():
    fin=open("Reminder.txt","r")
    Str=fin.readlines()
    for j in Str:
        new_Str=""
        for k in j:
            if k not in "\n":
                new_Str+=k
        print(new_Str)
    return
