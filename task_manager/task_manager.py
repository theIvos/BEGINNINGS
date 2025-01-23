import json
import logging
from datetime import datetime 
from task_manager_fces import *
import os
import time

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

formatter = logging.Formatter("%(levelname)s: %(message)s")

file_handler = logging.FileHandler("todo.log","w")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)

header = ["TASK","DEADLINE","STATUS"]
# todo_content = {"task1": {"task": "posekat zahradu", "deadline": 18272633, "status": "in progress"},
#                 "task2": {"task": "posekat zahradu", "deadline": 18272633, "status": "in progress"},
                # }

# open("todo.json","w",encoding="utf-8").close()
os.system("cls")
if "todo.json" not in os.listdir():
    with open("todo.json","w",encoding="utf-8") as file:
        file.write("{}")
while True:
    with open("todo.json","r+",encoding="utf-8") as file:
        # file.write(f'{"task1":{"TASK":"Zalit zahradu","DEADLINE":"zitra","STATUS":"NEW"}}')
        content = json.load(file)

    todo_content = content

    task_n = len(todo_content)

    # logger.debug(f"pocet aktualnich tasku: {task_n}")

    secs = []

    for ky,vl in todo_content.items():
        secs.append((vl["DEADLINESECS"]))

    secs.sort()
    
    temp = []
    full_list_sorted = []
    deadline_n = 0
    current_time = (time.time() + 3600)
    

    for i in range(len(secs)):
        for ky,vl in todo_content.items():
                        
            if secs[i] == vl["DEADLINESECS"] and vl["STATUS"] != "DONE":
                deadline_breach =""
                if (vl["DEADLINESECS"] - current_time) < 0:
                    deadline_breach = "!!!DEADLINE BREACHED!!!"
                if (f">>| {vl['TASK']:<24} | DEADLINE: {vl['DEADLINE']} - STATUS: {vl['STATUS']:<13} {deadline_breach}") in temp:
                    continue
                else:
                    temp.append(f">>| {vl['TASK']:<24} | DEADLINE: {vl['DEADLINE']} - STATUS: {vl['STATUS']:<13} {deadline_breach}")
                    #temp.append(f"{deadline_n:2d}) {vl["TASK"]:<24} | DEADLINE: {vl["DEADLINE"]} - STATUS: {vl["STATUS"]}")
    
    for i in range(len(secs)):
        # deadline_breach = ""
        for ky,vl in todo_content.items():
            # deadline_breach = ""
            
            if secs[i] == vl["DEADLINESECS"]:
                deadline_breach =""
                if (vl["DEADLINESECS"] - current_time) < 0:
                    deadline_breach = "!!!DEADLINE BREACHED!!!"
                if (f") {vl['TASK']:<24} | DEADLINE: {vl['DEADLINE']} - STATUS: {vl['STATUS']:<13} {deadline_breach}") in full_list_sorted:
                    continue
                else:
                    full_list_sorted.append(f") {vl['TASK']:<24} | DEADLINE: {vl['DEADLINE']} - STATUS: {vl['STATUS']:<13} {deadline_breach}")
                    #temp.append(f"{deadline_n:2d}) {vl["TASK"]:<24} | DEADLINE: {vl["DEADLINE"]} - STATUS: {vl["STATUS"]}")
    

    pre_closest = temp[0:3]
    closest = ""

    for i in pre_closest:
        deadline_n +=1
        # closest += f"{deadline_n}{i}\n"
        closest += f"{i}\n"            

    # os.system("cls")
    if len(temp) == 0:
        print(f"""\
==========================================================================================
    WELCOME TO YOUR TASK MANAGER!       
==========================================================================================
1| ADD TASK   2| EDIT TASK   3| FULL LIST   4| EXPORT CURRENT TASK-LIST TO CSV   Q| QUIT
------------------------------------------------------------------------------------------

    NO DEADLINES IN SIGHT SO FAR!
              

""")
    else:
        print(f"""\
==========================================================================================
    WELCOME TO YOUR TASK MANAGER!       
==========================================================================================
1| ADD TASK   2| EDIT TASK   3| FULL LIST   4| EXPORT CURRENT TASK-LIST TO CSV   Q| QUIT
------------------------------------------------------------------------------------------

    *** {len(pre_closest)} closest DEADLINE(s) for you are: ***

{closest}
""")

    user_choice = "n"

    while user_choice.lower() not in "1234q":
        user_choice = input("Choose your action from the menu above: ")

    if user_choice == "":
        os.system("cls")

    if user_choice == "1":
        os.system("cls")
        add = "yes"

        while add.lower() in ("yes","y"):
            task_n +=1
            new_task = {}
            new_task["TASK"] = input("TASK name (max 25 chars, min 1): ")

            while len(new_task["TASK"]) > 25 or len(new_task["TASK"]) < 1:
                new_task["TASK"] = input("TASK name (max 25 chars, min 1): ")
            
            # year = ""
            # month = ""
            # day = ""
            # hour = 0
            # minute = 0
            # seconds = 0

            year = set_year()
            month = set_month()
            day = set_day(month)
            
            settime = set_time()
            koeficient = datetime(1970,1,1)

            pre_deadline = datetime(year,month,day,settime[0],settime[1],settime[2])
            deadline = str(datetime(year,month,day,settime[0],settime[1],settime[2]))
            
            deadline_pos = (pre_deadline - koeficient).total_seconds()
            
            deadline_rev = f"{deadline[8:10]}.{deadline[5:7]}.{deadline[0:4]} ({deadline[11:]})"
            

            new_task["DEADLINE"] = deadline_rev
                
            new_task["STATUS"] = 'NEW'

            new_task["DEADLINESECS"] = deadline_pos

            todo_content["task"+str(task_n)] = (new_task)
            add = input("Do you want to add another task? ")

        


        open("todo.json","w",encoding="utf-8").close()
        with open("todo.json","w",encoding="utf-8") as file:
            json.dump(todo_content,file)

        os.system("cls")
        print("SYS INFO: Task(s) successfully added!")

    if user_choice == "2":
        os.system("cls")
        if len(todo_content) == 0:
            print("SYS INFO: NOT POSSIBLE! No tasks yet!")
        else:
            deadline_n = 0
            pre_full = full_list_sorted
            full = ""

            for i in pre_full:
                deadline_n +=1
                full += f"{deadline_n}{i}\n"  

            print(f"LIST OF ALL CURRENT TASKS:\n\n{full}\n")

            list_choice = input("(M)ark task  |  (R)emove task  |  (B)ack to main menu: ")

            while list_choice.lower() not in "mrb" or list_choice == "":
                list_choice = input("(M)ark task  |  (R)emove task  |  (B)ack to main menu: ")

            if list_choice.lower() == "b":
                pass
                os.system("cls")

            if list_choice.lower() == "r":
                if len(todo_content) < 1:
                    print("Nothing to be removed!")
                else:
                    os.system("cls")
                    mark_task = ""
                    print(f"LIST OF ALL CURRENT TASKS:\n\n{full}\n")
                    new_mark = full.split("\n")
                    mark_task = input("Choose number of task you want to remove: ")

                    while not mark_task.isdigit():
                        mark_task = input("Choose number of task you want to remove: ")

                    mark_task = int(mark_task)
                    while int(mark_task) > (len(todo_content)) or int(mark_task) < 1:
                        mark_task = input("Not in the list.\nChoose number from the list: ")
                        if not mark_task.isdigit():
                            mark_task = 0
                    
                    mark_task = int(mark_task)

                    key_for_mark = new_mark[mark_task-1][2:27].strip()

                    # print(key_for_mark)
                    # print(todo_content)

                    to_remove = ""

                    for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    to_remove = ky
                    
                    if len(todo_content) < 1:
                        print("Not possible to remove task since there is only 1 remaining.") 
                    else:
                        todo_content.pop(to_remove)
                        os.system('cls')
                        print(f"SYS INFO: Task '{key_for_mark}' successfully removed!")
                    
                    open("todo.json","w",encoding="utf-8").close()
                    with open("todo.json","w",encoding="utf-8") as file:
                        json.dump(todo_content,file) 

                    


            if list_choice.lower() == "m":
                if len(todo_content) < 1:
                    print("Nothing to be marked!")
                else:
                    os.system("cls")
                    mark_task = ""
                    print(f"LIST OF ALL CURRENT TASKS:\n\n{full}\n")
                    new_mark = full.split("\n")
                    mark_task = input("Choose number of task you want to mark: ")

                    while not mark_task.isdigit():
                        mark_task = input("Choose number of task you want to mark: ")

                    mark_task = int(mark_task)
                    while int(mark_task) > (len(todo_content)) or int(mark_task) < 1:
                        mark_task = input("Not in the list.\nChoose number from the list: ")
                        if not mark_task.isdigit():
                            mark_task = 0
                    
                    mark_task = int(mark_task)

                    key_for_mark = new_mark[mark_task-1][2:27].strip()
                    
                    # print(key_for_mark)
                    # print(todo_content)
                    os.system("cls")
                    what_mark = input(f"Do you want task '{key_for_mark}' mark as (D)ONE, (I)N PROGRESS or (N)OT STARTED ('B' for back to main menu)? ")
                    while what_mark.lower() not in "dibn":
                        what_mark = input(f"You have to choose one of the options: (D)ONE, (I)N PROGRESS, (N)OT STARTED or (B)ACK: ")

                    if what_mark.lower() == "d": 

                        for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    todo_content[ky]["STATUS"] = "DONE"
                                    os.system("cls")
                                    print(f"SYS INFO: Task '{key_for_mark}' was marked as 'DONE'.")
                        open("todo.json","w",encoding="utf-8").close()
                        with open("todo.json","w",encoding="utf-8") as file:
                            json.dump(todo_content,file)

                    if what_mark.lower() == "i": 

                        for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    todo_content[ky]["STATUS"] = "IN PROGRESS"
                                    os.system("cls")
                                    print(f"SYS INFO: Task '{key_for_mark}' was marked as 'IN PROGRESS'.")
                        open("todo.json","w",encoding="utf-8").close()
                        with open("todo.json","w",encoding="utf-8") as file:
                            json.dump(todo_content,file)

                    if what_mark.lower() == "n": 

                        for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    todo_content[ky]["STATUS"] = "NOT STARTED"
                                    os.system("cls")
                                    print(f"SYS INFO: Task '{key_for_mark}' was marked as 'NOT STARTED'.")
                        open("todo.json","w",encoding="utf-8").close()
                        with open("todo.json","w",encoding="utf-8") as file:
                            json.dump(todo_content,file)
        

    if user_choice == "3":
        os.system("cls")
        if len(todo_content) == 0:
            print("SYS INFO: NOT POSSIBLE! No tasks yet!")
        else:

            deadline_n = 0
            pre_full = full_list_sorted
            full = ""

            for i in pre_full:
                deadline_n +=1
                full += f"{deadline_n}{i}\n"  

            print(f"LIST OF ALL CURRENT TASKS:\n\n{full}\n")

            list_choice = input("(M)ark task  |  e(X)port to CSV  |  (B)ack to main menu: ")

            while list_choice.lower() not in "mxb" or list_choice == "":
                list_choice = input("(M)ark task  |  e(X)port to CSV  |  (B)ack to main menu: ")

            if list_choice.lower() == "b":
                pass
                os.system("cls")

            if list_choice.lower() == "x":
                if len(todo_content) < 1:
                    print("Nothing to be exported!")
                else:
                    filetime = (time.ctime()).replace(" ","_").replace(":","_")
                    csv_filename = f"task_manager_{filetime}.csv"
                    with open(csv_filename,"w",encoding="utf-8") as file:
                        file.write(",".join(header)+"\n")
                        for i in full_list_sorted:
                            file.write(f"{i[2:25].strip()},{i[38:60].strip()},{i[70:85].strip()}\n")
                    os.system("cls")
                    print(f"SYS INFO: Current task list succefully exported to '{csv_filename}'.")
            
            if list_choice.lower() == "m":
                os.system("cls")
                if len(todo_content) < 1:
                    print("Nothing to be marked!")
                else:
                    mark_task = ""
                    print(f"LIST OF ALL CURRENT TASKS:\n\n{full}\n")
                    new_mark = full.split("\n")
                    mark_task = input("Choose number of task you want to mark: ")

                    while not mark_task.isdigit():
                        mark_task = input("Choose number of task you want to mark: ")

                    mark_task = int(mark_task)
                    while int(mark_task) > (len(todo_content)) or int(mark_task) < 1:
                        mark_task = input("Not in the list.\nChoose number from the list: ")
                        if not mark_task.isdigit():
                            mark_task = 0
                    
                    mark_task = int(mark_task)

                    key_for_mark = new_mark[mark_task-1][2:27].strip()

                    # print(key_for_mark)
                    # print(todo_content)
                    os.system("cls")
                    what_mark = input(f"Do you want task '{key_for_mark}' mark as (D)ONE, (I)N PROGRESS or (N)OT STARTED ('B' for back to main menu)? ")
                    while what_mark.lower() not in "dibn":
                        what_mark = input(f"You have to choose one of the options: (D)ONE, (I)N PROGRESS, (N)OT STARTED or (B)ACK: ")

                    if what_mark.lower() == "d": 

                        for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    todo_content[ky]["STATUS"] = "DONE"
                                    os.system("cls")
                                    print(f"SYS INFO: Task '{key_for_mark}' was marked as 'DONE'.")
                        open("todo.json","w",encoding="utf-8").close()
                        with open("todo.json","w",encoding="utf-8") as file:
                            json.dump(todo_content,file)

                    if what_mark.lower() == "i": 

                        for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    todo_content[ky]["STATUS"] = "IN PROGRESS"
                                    os.system("cls")
                                    print(f"SYS INFO: Task '{key_for_mark}' was marked as 'IN PROGRESS'.")
                        open("todo.json","w",encoding="utf-8").close()
                        with open("todo.json","w",encoding="utf-8") as file:
                            json.dump(todo_content,file)

                    if what_mark.lower() == "n": 

                        for ky,vl in todo_content.items():
                            for kyv,vlv in vl.items():
                                if vlv == key_for_mark:
                                    todo_content[ky]["STATUS"] = "NOT STARTED"
                                    os.system("cls")
                                    print(f"SYS INFO: Task '{key_for_mark}' was marked as 'NOT STARTED'.")
                        open("todo.json","w",encoding="utf-8").close()
                        with open("todo.json","w",encoding="utf-8") as file:
                            json.dump(todo_content,file)

                # print("newmark:",new_mark)
                # print("newmarklen",len(new_mark))
                # print(new_mark[0][2:25].strip())

        
    if user_choice == "4":
        os.system("cls")
        if len(todo_content) < 1:
                print("SYS INFO: NOT POSSIBLE! Nothing to be exported at the moment!")
        else:
            filetime = (time.ctime()).replace(" ","_").replace(":","_")
            csv_filename = f"task_manager_{filetime}.csv"
            with open(csv_filename,"w",encoding="utf-8") as file:
                file.write(",".join(header)+"\n")
                for i in full_list_sorted:
                    file.write(f"{i[2:25].strip()},{i[38:60].strip()},{i[70:85].strip()}\n")

            os.system("cls")
            print(f"SYS INFO: Current task list succefully exported to '{csv_filename}'.")

    if user_choice.lower() == "q":
        break




# print(f"""\
# WELCOME TO YOUR TODO APP!
    
#     3. CLOSEST DEADLINES:
#     {closest_deadlines}

#     """)