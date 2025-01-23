import json
import os
import time
import shutil

def reset_chat():
    os.system("cls")
    if "chat.txt" not in os.listdir():
        input("There is no chat yet to be reset.\n\nPress any key to continue to main screen...")
        return main()
    backup = input(f"Do you want to make a copy of the chat file before reset? (Yes/No):\n")
    while backup.lower() not in ["y","n","yes","no"]:
        backup = input("You have to answer only 'yes' or 'no': ")
    
    if backup.lower() == "yes" or backup.lower() == "y":
        arch_chat = f"chat_history/chat_history_{(time.ctime().replace(" ","_").replace(":","_"))[4:]}.txt"
        if "chat_history" in os.listdir():
            shutil.copy("chat.txt",arch_chat)
            
        else:
            os.mkdir("chat_history")
            shutil.copy("chat.txt",arch_chat)
        os.system("cls")
        print(f"Chat history saved in '{arch_chat}'.")

    print("")

    reset = input("Do you really want to reset chat? (Yes/No): ")

    while reset.lower() not in ["y","n","yes","no"]:
        reset = input("You have to answer only 'yes' or 'no': ")

    if reset.lower() == "yes" or reset.lower() == "y":
        os.system("cls")
        chatfile = open("chat.txt","w",encoding="utf-8")
        chatfile.write(f"BEGINNING OF THE CHAT HISTORY\n")
        chatfile.close()
        print("Chat reset!")
        print("")
        input("Press any key to continue to main screen...")
    else:
        print("Chat NOT reset!")
        print("")
        input("Press any key to continue to main screen...")

    return main()



def chatroom(x,y):
    os.system("cls")

    if "chat.txt" not in os.listdir():
        chatfile = open("chat.txt","w",encoding="utf-8")
        chatfile.write(f"BEGINNING OF THE CHAT HISTORY\n")
        chatfile.close()

    with open("chat.txt","a+",encoding="utf-8") as file:
        file.write(f"\n\n{x} joined the chat on {time.ctime()}")
        file.seek(0)
                
        while True:
            file.seek(0)

            content = file.read()
            os.system("cls")
            print(content)

            print("\n\n" + str(50*"-"))

            message = input(f"{x}: ")

            if message.startswith("&"):
                file.write(f"\n\n{x} tried some magic in VSC on {time.ctime()}")
                os.system("cls")

            elif message == "":
                file.write(f"\n\n{x} ...")
                os.system("cls")

            elif message.lower() in ["quit","cancel","exit"] :
                file.write(f"\n\n{x} left the chat on {time.ctime()}")
                print("""You are leaving the chat!""")
                input("Press any key to continue to main screen...")
                break
            else:
                file.write(f"\n\n{x} [{time.ctime()}]:\n{message}")
                os.system("cls")

  
    return main()


def main():
    if "users.json" not in os.listdir():
        usersfile = open("users.json","w",encoding="utf-8")
        usersfile.write("{}")
        usersfile.close()

    os.system("cls")
    print(f"""
  ================================
   WELCOME TO THE CHAT FOR LOSERS          
  ================================
          
Start with login or register new user:
          
          1) LOGIN
          2) REGISTER NEW USER
          
          R) RESET CHAT
          Q) QUIT
          
---------------------------------------
TIP: To exit in chat use "exit".
---------------------------------------
""")
    choice = input("Choose login(1),register new user(2) or (Q)uit:\n")

    while choice.lower() not in "12qr":
        print("Please choose: '1', '2', 'R' or 'Q':")
        choice = input("")

    if choice == "1":
        return login()
    elif choice == "2":
        return register_user("")
    elif choice == "r":
        return(reset_chat())
    else:
        os.system("cls")
        print("See ya next time!")
        exit()

def login_pass(x):

    password = input("password: ")

    with open("users.json","r",encoding="utf-8") as file:
        content = json.load(file)

    if password.lower() == "cancel":
        return main()
    
    while password != content[x]:
        if password.lower() == "cancel":
            return main()
        print("Incorrect password!")
        password = input("password: ")

    return chatroom(x,password)

    
def login():
    os.system("cls")
    with open("users.json","r",encoding="utf-8") as file:
        content = json.load(file)
        print(f"Choose your username or 'CANCEL' for cancel:")
        username = input("username: ")

        if username.lower() == "cancel":
            return main()

        while username not in content:
            new_reg = input(f"User not registered. Do you want to register new user {username}? (Yes/No)\n")

            while new_reg.lower() not in ("yes","no","y","n"):
                new_reg = input("Please answer only 'yes' or 'no':\n")

            if new_reg.lower() == "yes" or new_reg.lower() == "y":
                return register_user(username)
            else:
                return main()
    
    return login_pass(username)



def register_user(x):
    with open("users.json","r",encoding="utf-8") as users_file:
        reg_users = json.load(users_file)
   
  
    wrong_username = f"Choose your username or 'CANCEL' for cancel:"
    
    # check the user name
    while x == "":
        os.system("cls")
        print(wrong_username)
        x = input("username: ")

        if x == "":
            wrong_username = f"Username cannot be empty. Choose your username or 'CANCEL' for cancel:"
        elif x not in reg_users.keys():
            break
        else:
            wrong_username = f"Username {x} already exists! Choose another username or 'CANCEL' for cancel:"
            x = ""
    return interlogin(x,"nopass")


def interlogin(x,y):
    if x.lower() == "cancel" or y.lower() == "cancel":
        return main()
    elif y == "nopass":
        return register_password(x)
    else:
        return register_account(x,y)

    
def register_password(x):
    os.system("cls")
    print(f"Choose your password for user {x} or 'CANCEL' for cancel:")
    password = input("password: ")

    return interlogin(x,password)

def register_account(x,y):
    os.system("cls")
    with open("users.json","r",encoding="utf-8") as file:
        content = json.load(file)

        content[x] = y

    with open("users.json","w",encoding="utf-8") as file:
        json.dump(content,file)

        print(f"""Thank you for your registration!
              
              
Your username is: {x}
Your password is: {y}


""")
        input("Press any key to continue to the home screen...")

    return main()


main()    



