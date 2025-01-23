import os
from soul_eater_forms import *
from soul_eater_attacks import *
import random
from copy import deepcopy
from time import sleep

class Player:

    def __init__(self,mark,user_name):
        self.no_form = {"name": "NO FORM","speed":10,"hp": 450,"current_hp": 450,"hp_coef": 1.3,"level":0,"attack_coef": 1.3,"attack_list": [{"name": "FIRE PUNCH", "power":10,"accuracy":4},{"name": "ICE KICK","power":12,"accuracy":3},{"name": "FLAMETHROWER","power":20,"accuracy":2}]}
        
        self.form_0 = {"name": "","speed":0,"hp": 0,"current_hp": 0,"level":0,"attack_list":[]}
        self.form_1 = {"name": "","speed":0,"hp": 0,"current_hp": 0,"level":0,"attack_list":[]}
        self.form_2 = {"name": "","speed":0,"hp": 0,"current_hp": 0,"level":0,"attack_list":[]}
        self.form_3 = {"name": "","speed":0,"hp": 0,"current_hp": 0,"level":0,"attack_list":[]}
        self.form_4 = {"name": "","speed":0,"hp": 0,"current_hp": 0,"level":0,"attack_list":[]}

        self.acquired = [self.form_0,self.form_1,self.form_2,self.form_3,self.form_4]

        self.forms = [self.no_form]            

        self.current_form = self.forms[0]["name"]
        self.speed = self.forms[0]["speed"]
        self.level = self.forms[0]["level"]

        self.name = mark
        self.where = [450]
        self.mark = f"|{mark}"
        self.backout = self.where[0]
        self.run = "NO"

        self.action_done = "NO"

        self.user_name = user_name
       
        self.dimension = "OUT"
        self.item_used = "NO"
        self.items = [potion,potion,max_potion,antidote,antidote,antidote,]
        
        self.hp = self.forms[0]["hp"]
        self.current_hp = self.forms[0]["current_hp"]
        
        self.status = " OK"
               
        self.attack_list = self.forms[0]["attack_list"]

        self.pc = "NO"

        players.append(self)

        while mapa[self.where[0]] != "|_":
            # self.where[0] += 1
            self.where[0] = random.randint(1,900)

        # print(self.where)    
        update_map(self)

    

    def new_attack(self,attack_name,power,accuracy,who):

        for i in self.forms:
            # print(i)
            if i["name"] == who:
                for j in i["attack_list"]:
                    if j["name"] == attack_name:
                        print(f"{who} already knows {attack_name}.\nNo changes.")
                        break
                    else:                        
                        i["attack_list"].append({"name":attack_name,"power":power,"accuracy":accuracy})
                        break


    def upgrade_attack(self,attack_name,power,accuracy,who):

        for i in self.forms:
            # print(i)
            if i["name"] == who:
                for j in i["attack_list"]:
                    if j["name"] == attack_name:
                        # print(j)
                        # print("this is it",j)
                        j["power"] += power
                        j["accuracy"] += accuracy
                        break
                    else:                        
                        print(f"{who} doesn't even know this attack you are trying to upgrade.\nNo changes.")
                        break
    
          

    def remove_form(self):
        self.forms = []

    def acquire_form(self,form):
        form_to_acq = deepcopy(form)

        attacks_to_not_dupl = []
        for i in form_to_acq["attack_list"]:
            attacks_to_not_dupl.append(i["name"])

        # print("attacks not to dupl",attacks_to_not_dupl)
        
        
        for ky,vl in form_to_acq["level_list"].items():
            if form_to_acq["level"] >= ky and vl["name"] not in attacks_to_not_dupl:
                form_to_acq["attack_list"].append(vl)

        # print("attack list",form_to_acq["attack_list"])


        naming_colors = ["I","II","I","I","I"]
        naming = 0
        for i in self.acquired:
            if i["name"] == form_to_acq["name"]:
                naming += 1
                form_to_acq["name"] = f"{form_to_acq['name']} {naming_colors[naming]}"

        for ky,vl in experience_levels.items():
            if ky == form_to_acq["level"]:
                form_to_acq["exp"] = vl

        for i in self.acquired:
            if i["name"] == "":
                i["name"] = form_to_acq["name"]
                i["level"] = form_to_acq["level"]
                i["speed"] = form_to_acq["speed"]
                # i["current_hp"] = form["current_hp"]
                # i["current_hp"] = form["current_hp"] * round((form["hp_coef"] * form["level"]))
                i["current_hp"] = round(form_to_acq["hp"] /2)
                i["extra_hp"] = form_to_acq["extra_hp"]
                i["hp"] = form_to_acq["hp"]
                # i["hp"] = (form_to_acq["hp"] * round((form_to_acq["hp_coef"] * form_to_acq["level"])))
                i["attack_coef"] = form_to_acq["attack_coef"]
                # i["attack_list"] = form["attack_list"]
                i["attack_list"] = form_to_acq["attack_list"]
                i["exp"] = form_to_acq["exp"]
                # i["exp"] = 999
                i["level_list"] = form_to_acq["level_list"]
                i["hp_coef"] = form_to_acq["hp_coef"]
                i["OG_NAME"] = form_to_acq["OG_NAME"]
                i["base_hp"] = form_to_acq["base_hp"]
                i["extra_def"] = form_to_acq["extra_def"]
                i["extra_atk"] = form_to_acq["extra_atk"]
                i["atk"] = form_to_acq["atk"]
                i["dfk"] = form_to_acq["dfk"]
                i["nature"] = "acquired"
                i["extra_acc"] = form_to_acq["extra_acc"]
                i["OG_atk"] = form_to_acq["OG_atk"]
                i["OG_dfk"] = form_to_acq["OG_dfk"]
                i["extra_speed"] = form_to_acq["extra_speed"]
                i["OG_speed"] = form_to_acq["OG_speed"]
                i["DBP"] = form_to_acq["DBP"]
                i["type"] = form_to_acq["type"]
                
                

                # print(i["attack_list"])                    
                self.forms.append(i)
                break
             
    def pc_turn(self):
        update_map(self)


    def player_turn(self):
        # game_logo()
        # print("")
        print(f"{self.user_name}'s turn!")
        input("")
        update_map(self)
        self.item_used = "NO"

        for i in self.forms:
            if i["current_hp"] < 1:
                self.forms.remove(i)
                clean_acquired(self,i)
    
        check_status(self)
        if self in players:
            if self.status == "SLP":
                still_sleep(self)
            
            if self.status != "SLP":
                player_menu(self)

    
    def move(self):
        clean()
        
        warn_message = ""
        warning2 = "Set your direction from the menu below!"        
        warning = "Not possible to go there! Try again!"
        
        steps = self.speed               
        direction = 0

        
        while steps > 0:
                        
            clean()
            togo = 0
            while togo not in ("1","2","3","4","6","7","8","9","s","S"):
                clean()

                show_map(mapa)
                print(f"| remaining steps: {steps}")
                player_title(self)
                
                print(warn_message)
                
                togo = input(f"""                
                Where do you want to go?
                (7) (8) (9)
                (4)  {self.name}  (6)
                (1) (2) (3)

                S) STOP HERE!
                
                """)
            

            if togo == "7":
                if self.where[0] < 31 or (self.where[0]-1) in borders:
                    direction = 0
                    warn_message = warning
                else:
                    direction = -31
                    steps -= 1
                    warn_message = ""
            elif togo == "8":
                if self.where[0] < 31:
                    direction = 0
                    warn_message = warning
                else:
                    direction = -30
                    steps -= 1
                    warn_message = ""
            elif togo == "9":
                if self.where[0] < 31 or self.where[0] in borders:
                    direction = 0
                    warn_message = warning
                else:
                    direction = -29
                    steps -= 1
                    warn_message = ""
            elif togo == "4":
                if self.where[0] == 1 or (self.where[0]-1) in borders:
                    direction = 0
                    warn_message = warning
                else:
                    direction = -1
                    steps -= 1
                    warn_message = ""
            elif togo == "6":
                if self.where[0] in borders:
                    direction = 0
                    warn_message = warning
                else:
                    direction = 1
                    steps -= 1
                    warn_message = ""
            elif togo == "1":
                if self.where[0] > 870 or (self.where[0]-1) in borders:
                    direction = 0
                    warn_message = warning
                else:
                    direction = 29
                    steps -= 1
                    warn_message = ""
            elif togo == "2":
                if self.where[0] > 870:
                    direction = 0
                    warn_message = warning
                else:
                    direction = 30
                    steps -= 1
                    warn_message = ""
            elif togo == "3":
                if self.where[0] > 870 or self.where[0] in borders:
                    direction = 0
                    warn_message = warning
                else:
                    direction = 31
                    steps -= 1
                    warn_message = ""
            elif togo.lower() == "s":
                
                    direction = 0
                    # print("OK.")
                    steps = 0
                 
            else:
                
                clean()                
                

            self.backout = self.where[0]

            clean()                        
            if mapa[self.where[0]] == f"{self.mark}|\n":
                mapa[self.where[0]] = "|_|\n"
            else:
                mapa[self.where[0]] = "|_"
            
            self.where[0] = self.where[0] + direction
            # print(self.where)

            if mapa[self.where[0]] == f"|*":
                mapa[self.where[0]] = "|_"
                found_item = self.items.append(item_list[random.randint(0,len(item_list)-1)])
                clean()
                player_title(self)
                print(f"""{line}
        {self.user_name}'s ITEMS:               
                """)
                print(f"{self.user_name} have found {self.items[-1]['name']}!")
                input("")
                create_item()

            if mapa[self.where[0]] in [i.mark for i in players]:
                enemy = []
                for i in players:
                    if mapa[self.where[0]] == i.mark:
                        enemy.append(i)
                battle(self,enemy[0])
                steps = 0
            
            elif mapa[self.where[0]] in [f"{i.mark}|\n" for i in players]:
                enemy = []
                for i in players:
                    if mapa[self.where[0]] == f"{i.mark}|\n":
                        enemy.append(i)
                battle(self,enemy[0])
                steps = 0

            elif mapa[self.where[0]] in [i.mark for i in pcs]:
                enemy = []
                for i in pcs:
                    if mapa[self.where[0]] == i.mark:
                        enemy.append(i)
                battle(self,enemy[0])
                steps = 0

            elif mapa[self.where[0]] in [f"{i.mark}|\n" for i in pcs]:
                enemy = []
                for i in pcs:
                    if mapa[self.where[0]] == f"{i.mark}|\n":
                        enemy.append(i)
                battle(self,enemy[0])
                steps = 0

            else:
                lost_soul_attacks = random.randint(-7,1)
                if lost_soul_attacks >= 0:
                    lost_soul_battle(lost_souls[random.randint(0,len(lost_souls)-1)],self)
                    steps = 0
            clean()
            update_map(self)
            # update_map(players)

def battle_menu():
    print(f"""{line}
    A) ATTACK       F) FORM CHANGE
    I) ITEMS        R) RUN               
            """)

def player_menu(player):
    # player.item_used = "NO"
    # check_status(player)
    warn_message = ''
    warning = "You have to specify one of the options from the menu below (or type 'quit' for quit): "
    while True:
        clean()
        show_map(mapa)    
        
        player_title(player)
        print(f"""{line}
        M) MOVE         F) FORMS
        I) ITEMS        H) HEAL               
                """)
        print(warn_message)
        player_choice = input("CHOOSE YOUR ACTION: ")

        if player_choice.lower() == "m":
            warn_message = ''
            player.move()
            break

        elif player_choice.lower() == "i":
            warn_message = ''
            show_items(player)
            if player.item_used == "YES":
                warn_message = ''
                break

        elif player_choice.lower() == "h":
            warn_message = ''
            for i in player.forms:
                i["current_hp"] += round(i["hp"] * 0.4)
                check_hp(i)
            player.status = " OK"
            clean()
            print(f"{player.user_name} is healing itself.") 
            input("")
            clean()
            break

        elif player_choice.lower() == "f":
            warn_message = ''
            forms_menu(player)
        
        elif player_choice.lower() == "quit":
            exit()
        
        else:
            warn_message = warning



def show_items(player):
    # clean()
    warn_message = ''
    while True:
        clean()
        player_title(player)
        print(f"""{line}
        {player.user_name}'s ITEMS:               
                """)
        item_number = 0
        if len(player.items) < 1:
            print("--- no items at the moment ---")
        else:
            for i in player.items:
                item_number += 1
                print(f"{item_number:2d}) {i['name']:<16}  - {i['info']}")
           
        print("\nB) BACK\n")
        print(warn_message)
        item_choice = input("CHOOSE THE ITEM: ")

        if item_choice.lower() == "b":
            break

        elif not item_choice.isdigit():
            warn_message = f"Not in the list. Choose from the list!"

        elif int(item_choice) > len(player.items) or int(item_choice) == 0:
            warn_message = f"Not in the list. Choose from the list!"

        else:
            chosen_item(player,player.items[int(item_choice) -1])
            if player.item_used == "YES":                
                break


def chosen_item(player,item):
    # clean()
    player_title(player)
    print(f"""{line}
        {player.user_name}'s ITEMS:               
                """)
    warn_message = ""
    while True:
        clean()
        print(line)
        print(f"{item['name']}  - {item['info']}")
        print(f"""{line}
        U) USE 
        T) TOSS         B) BACK 
                """)
        print(warn_message)
        choice_what = input(f"CHOOSE THE ACTION FOR {item['name']}: ")

        if choice_what.lower() == "u":
            if item["dimension"] == player.dimension or item["dimension"] == "BOTH":
                clean()
                use_item(player,item)
                
                break
            else:
                clean()
                player_title(player)
                print(f"""{line}
        {player.user_name}'s ITEMS:               
                        """) 
                print(f"Sorry, you cannot use {item['name']} here!")
                input("")
                
        
        elif choice_what.lower() == "t":
            clean()
            player.items.remove(item)
            player_title(player)
            print(f"""{line}
        {player.user_name}'s ITEMS:               
                        """)            
            print(f"{item['name']} was tossed away.")
            input("")
            clean()
            break
            
            
        elif choice_what.lower() == "b":
            clean()
            break

        else:
            warn_message = f"Not in the menu! Choose again!"
        
        

def use_item(player,item):
    # clean()
    warn_message = ""

    while True:
        clean()
        player_title(player)
        print(f"""{line}
        {player.user_name}'s ITEMS:               
                """)
        print(line)
        show_player_forms(player)
        print("")
        print("B) BACK")
        print(warn_message)
        form_choice = input(f"CHOOSE THE FORM TO WHICH YOU WANT TO USE THE {item['name']}: ")

        if form_choice.isdigit():
            clean()
            form_choice = int(form_choice)
            
            if form_choice > len(player.forms) or form_choice == 0:
                warn_message = f"Not in the list. Choose the number of one of your forms!"
            else:
                clean()
                break

        elif form_choice.lower() == "b":
            clean()
            return

        else:
            
            warn_message = f"Not in the list. Choose the number of one of your forms!"
    clean()
    player_title(player)
    print(f"""{line}
        {player.user_name}'s ITEMS:               
                """)
    item_effect(player,item,form_choice - 1)
    input("")
    player.item_used = "YES"
    player.items.remove(item)



def show_player_forms(player):
    clean()
    player_title(player)
    print(f"""{line}
        {player.user_name}'s FORMS:               
                """)
    form_number = 0
    for i in player.forms:
        form_number += 1
        # print(f"{form_number}) {i['name']:<20}L: {i['level']:2d} HP: {i['current_hp']:3d}/{i['hp']:3d}")
        print(f"{form_number}) {i['name']:<26} L:{i['level']:2d}   HP:{i['current_hp']:4d}/{i['hp']:4d}")

def lost_soul_battle(lost_soul,player):
    title_count = len(player.user_name)
    battle_lost_soul = ""
    player.dimension = "INBATTLE"
    battle_lost_soul = deepcopy(lost_soul)
    battle_lost_soul["level"] = random.randint(1,20)
    clean()
    attacked()
    input("")

    clean()
    print(f"""
    {"":<{title_count}}   _    _______
    {"":<{title_count}}  | |  / / ___/
    {player.user_name}  | | / /\__ \  {lost_soul['name']}
    {"":<{title_count}}  | |/ /___/ / 
    {"":<{title_count}}  |___//____/  
    """)
    input("")

    on_turn = player
    off_turn = battle_lost_soul


    attacks_not_to_dupl = []
    for i in battle_lost_soul["attack_list"]:
        attacks_not_to_dupl.append(i["name"])


    for ky,vl in battle_lost_soul["level_list"].items():
        if battle_lost_soul["level"] >= ky and vl["name"] not in attacks_not_to_dupl:
            battle_lost_soul["attack_list"].append(vl)


    battle_lost_soul["current_hp"] = battle_lost_soul["current_hp"] * round((battle_lost_soul["level"] * battle_lost_soul["hp_coef"]))
    battle_lost_soul["hp"] = battle_lost_soul["hp"] * round((battle_lost_soul["level"] * battle_lost_soul["hp_coef"]))

    if player.forms[0]['name'] != "NO FORM":
        if battle_lost_soul["speed"] > player.speed:
            on_turn,off_turn = off_turn,on_turn

    while player.form_0["current_hp"] > 0 and battle_lost_soul["current_hp"] > 0:
        

        on_turn_status = battle_lost_soul["status"]

        if on_turn == player:
            on_turn_status = player.status
        

        if on_turn_status == "SLP":           
            still_sleep(on_turn)
        clean()
        on_turn_status = battle_lost_soul["status"]

        if on_turn == player:
            on_turn_status = player.status
   
        

        if on_turn_status != "SLP":        

            if player.forms[0]["current_hp"] <= 0:
                print(f"{player.forms[0]['name']} fainted!")
                input("")
                
                clean_acquired(player,player.forms[0])
                player.forms.pop(0)
                                
                battle_choice_form_change(player)

            battle_lost_soul_title(player,battle_lost_soul)
            
            if on_turn == player:

                battle_menu()

                battle_choice = input(f"{on_turn.user_name}: What do you want to do? ")
                if battle_choice.lower() == "a":
                    
                    battle_choice_attack_lost_soul(on_turn,off_turn,player,battle_lost_soul)
                    if on_turn.action_done == "YES":
                        on_turn.action_done = "NO"
                        check_status(on_turn,off_turn)
                        check_status(off_turn,on_turn)
                        on_turn,off_turn = off_turn,on_turn
                
                elif battle_choice.lower() == "f":                    
                    battle_choice_form_change(on_turn)
                    if on_turn.action_done == "YES":
                        on_turn.action_done = "NO"
                        on_turn,off_turn = off_turn,on_turn

                elif battle_choice.lower() == "i":
                    show_items(on_turn)
                    if on_turn.item_used == "YES":
                        on_turn.item_used = "NO"
                        on_turn,off_turn = off_turn,on_turn

                elif battle_choice.lower() == "r":
                    on_turn.run = "YES"
                    break
                
            else:
                # print(f"{battle_lost_soul['name']} attacks!")
                print(line)
                print("")
                lost_soul_landing_attack(battle_lost_soul,player)
                
                # input("")
                check_status(on_turn,off_turn)
                check_status(off_turn,on_turn)
                on_turn,off_turn = off_turn,on_turn
        else:
            on_turn,off_turn = off_turn,on_turn

    if battle_lost_soul["current_hp"] <= 0:
        get_experiences(player,battle_lost_soul)
        
        devour = devouring_soul(player,battle_lost_soul)
        print(devour)
        if devour == "YES":
            player.acquire_form(battle_lost_soul)
    elif player.form_0["current_hp"] <= 0:
            print(f"{player.user_name} has been killed by {battle_lost_soul['name']}!")
            input("")
            kill_player(player)
            # update_map(player)
      
    after_battle_reset_extras(player)
    after_battle_reset_extras(battle_lost_soul)

    player.dimension = "OUT"
    

def devouring_soul(player,lost_soul):
    warn_message = ''
    warning = "You have to choose Y(es) or N(o). Try again!"
    while True:
        print(warn_message)
        devour_ans = input(f"Do you want to devour {lost_soul['name']}'s soul now and make it one of your forms? (Y/N) ")

        if devour_ans.lower() not in ("y","n"):
            warn_message = warning
        elif devour_ans.lower() == "y":
            if len(player.forms) < 5:
                return "YES"
            else:
                return inbattle_release(player)
        else:
            break

def inbattle_release(player):
    warn_message = ""
    warning = "You have to choose (Y)es or (N)o. Try again!"
    while True:
        print(warn_message)
        release_choice = input(f"You can have only 4 forms (exclusive your basic form)\n Do you wish to release some of your forms to devour this new one? (Y/N) ")
        if release_choice.lower() not in ("y","n"):
            warn_message = warning
        elif release_choice.lower() == "n":
            return "NO"
        else:
            rel_forms = []
            for i in player.forms:
                if i["name"] == "NO FORM":
                    continue
                else:
                    rel_forms.append(i)

            while True:
                warn_message = ""
                warning = "Choose the number of form you want to release: "
                rel_forms_nr = 0
                clean()
                player_title(player)
                print(f"""{line}
        {player.user_name}'s FORMS:               
                """)
                for i in rel_forms:
                    rel_forms_nr += 1
                    # print(f"{form_number}) {i['name']:<26} L:{i['level']:2d}   HP:{i['current_hp']:4d}/{i['hp']:4d}")
                    print(f"{rel_forms_nr}) {i['name']:<29}L:{i['level']:2d} HP:{i['current_hp']:4d}/{i['hp']:4d}")
                print(warn_message)
                which_form = input("WHICH FORM YOU WANT TO RELEASE? ")

                form_for_rel = []
                if which_form.isdigit():
                    which_form = int(which_form)
                    if which_form > len(rel_forms):
                        warn_message = warning
                    else:
                        for i in player.forms:
                            if i["name"] == rel_forms[which_form -1]["name"]:
                                form_for_rel.append(i)
                        
                        release_form(player,form_for_rel[0])
                        if len(player.forms) < 5:
                            return "YES"
                        else:
                            return "NO"

                else:
                    warn_message = warning        



                





def check_status(player,opponent="NONE"):
    

    if type(player) == dict:
        if player["current_hp"] > 0:
            if player["status"] == "PSN":
                print(f"{player['name']} is hurt by poison!")
                input("")
                player["current_hp"] = player["current_hp"] - round(player["hp"] * 0.05)
        

    else:
        
        if player.status == "PSN" and player.form_0["current_hp"] > 0:

            # print("")
            to_be_poped_out = []
            to_vain = []
            forms_nr = len(player.forms)
            print(f"{player.user_name} is hurt by poison!")
            input("")

            for i in player.forms:
                i["current_hp"] = i["current_hp"] - round(i["hp"] * 0.05)

            # if player.form_0["current_hp"] < 1:
            #     return
            
            for i in range(len(player.forms)):
                # print("player forms",player.forms[i]["current_hp"])
                if player.forms[i]["current_hp"] < 1:
                   
                    # print("player forms",player.forms[i]["current_hp"])
                    
                    to_be_poped_out.append(player.forms[i])
                    to_vain.append(player.forms[i])

                    if player.forms[i]["name"] == "NO FORM":
                        print(f"{player.user_name} died!")
                        
                    else:
                        print(f"{player.forms[i]['name']} fainted!")
                    player.forms[0]['DBP'] = "YES"
                    input("")
                    
                    
                    clean_acquired(player,player.forms[i])

                   
                    
                    if player.dimension == "INBATTLE":
                        if type(opponent) != dict:
                            if opponent.pc == "NO":                                      
                                get_experiences(opponent,player,to_be_poped_out)
                        #  if player.pc == "NO":                                      
                        #     get_experiences(opponent,player,to_be_poped_out)
                    else:
                        if player.forms[i]["name"] == "NO FORM":
                            pass
                        else:
                            print(f"{player.forms[i]['name']} vanished into the void!")
                            input("")

                    
                    to_be_poped_out.remove(player.forms[i])

            # print(player.forms)

            no_form_og_pos = []        
            vain_nr = -1

            for i in player.forms:
                vain_nr += 1
                # print(i["name"])
                if i["name"] == "NO FORM":
                    no_form_og_pos.append(vain_nr)
            
            for i in to_vain:
                # vain_nr += 1
                # print(i["name"])
                # if i["name"] == "NO FORM":
                #     no_form_og_pos.append(vain_nr)                
                
                player.forms.remove(i)

            # for i in player.forms:
            #     vain_nr += 1
            #     print(i["name"])
            #     if i["name"] == "NO FORM":
            #         no_form_og_pos.append(vain_nr)

            # print("no form og pos:",no_form_og_pos)

            # print(player.forms)
                     
            if len(player.forms) < forms_nr:
                survive = "NO"
                for i in player.forms:
                    if i["name"] == "NO FORM":
                        survive = "YES"
                        if no_form_og_pos[0] != 0:
                            if player.pc == "NO":
                                battle_choice_form_change(player)
                        break
                    else:
                        continue
                    
                if survive == "NO":
                    if player.dimension == "INBATTLE":
                        pass
                    else:
                        print(f"{player.user_name} died!")
                        kill_player(player)
                        input("")

 
            
                        
                            

                

            
               
               


def get_experiences(winner,loser,remove_list = [{"name":"NO FORM"}]):

    if len(remove_list) > 0:
    
        if type(loser) == dict:
            print(f"{loser['name']} fainted!")
            
            expoints = round((loser["hp"] + loser["speed"]) * (loser["level"]* loser["attack_coef"]))
            input("")

        else:        
            if remove_list[0]['DBP'] == "NO":
                if remove_list[0]['name'] == "NO FORM":
                        print(f"{loser.user_name} fainted!")
                        
                else:
                    print(f"{remove_list[0]['name']} fainted!")    
                input("")
            expoints = round((remove_list[0]["hp"] + remove_list[0]["speed"]) * (remove_list[0]["level"] * remove_list[0]["attack_coef"]))
                    
                
            
        if type(winner) == dict:
            pass     
        else:
            winner.forms[0]["exp"] += expoints

            if winner.forms[0]["name"] == "NO FORM":
                print(f"{winner.user_name} gains {expoints} experience points!")
                
            else:    
                print(f"{winner.forms[0]['name']} gains {expoints} experience points!")
            input("")

            level_up(winner,winner.forms[0])    

    # print("get experiences done")
    # input("")


def level_up(player,form):
    level_comparison = form["level"]
    leveling_up = 0 
    attacks_to_learn = []
    attacks_learned = []

    
    for i in form["attack_list"]:
        attacks_learned.append(i["name"])

   

    for ky,vl in experience_levels.items():
        if vl <= form["exp"]:
            form["level"] = ky
            if form["level"] != level_comparison:
                leveling_up += 1
                # print(form)
                for ky,vl in form["level_list"].items():
                    if form["level"] == ky:
                        attacks_to_learn.append(vl)
                 

    if leveling_up >= level_comparison:

        coef_for_curr_hp = form["current_hp"] / form["hp"]
        form["hp"] = (form["base_hp"] * round(form["hp_coef"] * form["level"])) + form["extra_hp"]
        # form["current_hp"] = form["hp"] - round(coef_for_curr_hp * form["hp_coef"])
        form["current_hp"] = round(form["hp"] * coef_for_curr_hp)

        # print("attacks learned",attacks_learned) 
        # print("attacks to learn",attacks_to_learn)

        if form["name"] == "NO FORM":
            print(f"{player.user_name} leveled up to level {form['level']}!")
            input("")
        else:
            print(f"{form['name']} leveled up to level {form['level']}!")
            input("")

        if len(attacks_to_learn) > 0:
            for i in attacks_to_learn:

                if i["name"] in attacks_learned:
                    continue
                else:
                                
                    if form["name"] == "NO FORM":
                        print(f"{player.user_name} have learned {i['name']}!")
                        input("")
                    else:
                        print(f"{form['name']} have learned {i['name']}!")
                        input("")
                    
                    form["attack_list"].append(i)
                    attacks_learned.append(i["name"])
 

def clean_acquired(player,form):
    # print(form)
    to_be_changed = []
    # print(player.acquired)
    form_nums = -1
    for i in player.acquired:
        form_nums += 1
 
        if i["name"] == form["name"]:
            to_be_changed.append(form_nums)
    # print(to_be_changed)
    player.acquired[to_be_changed[0]] = {"name":""}

# def clean_acquired(player,form):
#     to_be_changed = []
#     # print(player.acquired)
#     form_nums = -1
#     for i in player.acquired:
#         form_nums += 1
 
#         if i["name"] == form["name"]:
#             to_be_changed.append(form_nums)

#     player.acquired[to_be_changed[0]] = {"name":""}
    # print(player.acquired)
    # print("clean acquired done")

def attacked():
    print("""
        ___  _______________   ________ __ __________  __
       /   |/_  __/_  __/   | / ____/ //_// ____/ __ \/ /
      / /| | / /   / / / /| |/ /   / ,<  / __/ / / / / / 
     / ___ |/ /   / / / ___ / /___/ /| |/ /___/ /_/ /_/  
    /_/  |_/_/   /_/ /_/  |_\____/_/ |_/_____/_____(_)   
    """)


def battle_anim(attacker, defender):
    title_count = len(attacker.user_name)

    for _ in range(3):

        print(f"""
    {"":<{title_count}}   _    _______
    {"":<{title_count}}  | |  / / ___/
    {attacker.user_name}  | | / /\__ \  {defender.user_name}
    {"":<{title_count}}  | |/ /___/ / 
    {"":<{title_count}}  |___//____/  
        """)
        sleep(0.3)
        clean()
        sleep(0.3)    

def battle(attacker,defender):
    title_count = len(attacker.user_name)

    attacker.dimension = "INBATTLE"
    defender.dimension = "INBATTLE"
    on_turn = attacker
    off_turn = defender
    print("""
        ____  ___  ______________    ________
       / __ )/   |/_  __/_  __/ /   / ____/ /
      / __  / /| | / /   / / / /   / __/ / / 
     / /_/ / ___ |/ /   / / / /___/ /___/_/  
    /_____/_/  |_/_/   /_/ /_____/_____(_)    
    """)
    input("")
    
    # battle_anim(attacker,defender)    
    clean()
    print(f"""
    {"":<{title_count}}   _    _______
    {"":<{title_count}}  | |  / / ___/
    {attacker.user_name}  | | / /\__ \  {defender.user_name}
    {"":<{title_count}}  | |/ /___/ / 
    {"":<{title_count}}  |___//____/  
    """)
    input("")
    # print(on_turn.forms[0]["extra_atk"])
    # print(on_turn.forms[0]["extra_def"])

    while attacker.form_0["current_hp"] > 0 and defender.form_0["current_hp"] > 0:
        
        if on_turn.status == "SLP":
            still_sleep(on_turn)

        # clean()
        if on_turn.status != "SLP":

        
            if attacker.forms[0]["current_hp"] <= 0:
                
                print(f"{attacker.forms[0]['name']} fainted!")
                attacker.forms[0]["DBP"] = "YES"
                input("")
                if defender.pc == "NO":
                    get_experiences(defender,attacker,attacker.forms)
               
                clean_acquired(attacker,attacker.forms[0])
                attacker.forms.pop(0)
                
                if attacker.pc == "NO":
                    battle_choice_form_change(attacker)

            if defender.forms[0]["current_hp"] <= 0:
                
                print(f"{defender.forms[0]['name']} fainted!")
                defender.forms[0]["DBP"] = "YES"
                input("")
                if attacker.pc == "NO":
                    get_experiences(attacker,defender,defender.forms)
                
                clean_acquired(defender,defender.forms[0])
                defender.forms.pop(0)

                if defender.pc == "NO":
                    battle_choice_form_change(defender)

            clean()

            battle_title(attacker,defender)

            if on_turn.pc == "NO":
                
                battle_menu()

                battle_choice = input(f"{on_turn.user_name}: What do you want to do? ")
                if battle_choice.lower() == "a":
                    battle_choice_attack(on_turn,off_turn,attacker,defender)
                    if on_turn.action_done == "YES":
                        on_turn.action_done = "NO"
                        if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
                            check_status(on_turn,off_turn)
                            if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
                                check_status(off_turn,on_turn)
                        on_turn,off_turn = off_turn,on_turn
                
                elif battle_choice.lower() == "f":
                    battle_choice_form_change(on_turn)
                    if on_turn.action_done == "YES":
                        on_turn.action_done = "NO"
                        if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
                            check_status(on_turn,off_turn)
                            if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
                                check_status(off_turn,on_turn)
                        on_turn,off_turn = off_turn,on_turn

                elif battle_choice.lower() == "i":
                    show_items(on_turn)
                    if on_turn.item_used == "YES":
                        on_turn.item_used = "NO"
                        on_turn,off_turn = off_turn,on_turn


                elif battle_choice.lower() == "r":
                    if off_turn.user_name == "HELLKING":
                        print("There is no escape from HELL KING!")
                        input("")
                    else:
                        on_turn.run = "YES"
                        update_map(on_turn)
                        update_map(off_turn)
                        break

            else:
                pc_attack = on_turn.forms[0]["attack_list"][random.randint(0,len(on_turn.forms[0]["attack_list"])-1)]
                print(line)
                print("")
                if on_turn.forms[0]['name'] == "NO FORM":
                    print(f"{on_turn.user_name} used {pc_attack['name']}!")
                else:
                    print(f"{on_turn.forms[0]['name']} used {pc_attack['name']}!")
                input("")
                landing_attack(pc_attack,off_turn,on_turn)
                if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
                        check_status(on_turn,off_turn)
                        if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
                            check_status(off_turn,on_turn)
                on_turn,off_turn = off_turn,on_turn
            
        else:
            on_turn,off_turn = off_turn,on_turn

    

    if attacker.form_0["current_hp"] <= 0:
        if defender in pcs:
            print(f"{attacker.user_name} was killed by {defender.user_name}!")
            input("")
            kill_player(attacker)        
        if defender in players:
            # print("HEEEEEEEEEEJ")
            get_experiences(defender,attacker,attacker.forms)
            kill_player(attacker)
    elif defender.form_0["current_hp"] <= 0:
        if attacker in players:
            # print(defender.form_0)
            # print("JEEEEEEEEEEEEEEH")
            # print(defender.forms)
            get_experiences(attacker,defender,defender.forms)
            kill_player(defender)

    after_battle_reset_extras(attacker)
    after_battle_reset_extras(defender)

    attacker.dimension = "OUT"
    defender.dimension = "OUT"



# def battle(attacker,defender):
#     attacker.dimension = "INBATTLE"
#     defender.dimension = "INBATTLE"
#     on_turn = attacker
#     off_turn = defender
#     print(f"There is gonna be a battle!\n{attacker.name} VS {defender.name}!!!")
#     # print(on_turn.forms[0]["extra_atk"])
#     # print(on_turn.forms[0]["extra_def"])

#     while attacker.form_0["current_hp"] > 0 and defender.form_0["current_hp"] > 0:
#         if on_turn.status == "SLP":
#             still_sleep(on_turn)

#         if on_turn.status != "SLP":

        
#             if attacker.forms[0]["current_hp"] <= 0:
#                 print(f"{attacker.forms[0]['name']} perished!")

#                 get_experiences(defender,attacker,attacker.forms)
               
#                 clean_acquired(attacker,attacker.forms[0])
#                 attacker.forms.pop(0)
#                 battle_choice_form_change(attacker)

#             if defender.forms[0]["current_hp"] <= 0:
#                 print(f"{defender.forms[0]['name']} perished!")
                
#                 get_experiences(attacker,defender,defender.forms)
                
#                 clean_acquired(defender,defender.forms[0])
#                 defender.forms.pop(0)
#                 battle_choice_form_change(defender)



#             battle_title(attacker,defender)

            
#             battle_menu()

#             battle_choice = input(f"{on_turn.user_name}: What do you want to do? ")
#             if battle_choice.lower() == "a":
#                 battle_choice_attack(on_turn,off_turn,attacker,defender)
#                 if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
#                     check_status(on_turn,off_turn)
#                     if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
#                         check_status(off_turn,on_turn)
#                 on_turn,off_turn = off_turn,on_turn
            
#             elif battle_choice.lower() == "f":
#                 battle_choice_form_change(on_turn)
#                 if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
#                     check_status(on_turn,off_turn)
#                     if on_turn.form_0["current_hp"] > 0 and off_turn.form_0["current_hp"] > 0:
#                         check_status(off_turn,on_turn)
#                 on_turn,off_turn = off_turn,on_turn

#             elif battle_choice.lower() == "i":
#                 show_items(on_turn)
#                 if on_turn.item_used == "YES":
#                     on_turn.item_used = "NO"
#                     on_turn,off_turn = off_turn,on_turn


#             elif battle_choice.lower() == "r":
#                 on_turn.run = "YES"
#                 break
            
#         else:
#             on_turn,off_turn = off_turn,on_turn

    

#     if attacker.form_0["current_hp"] <= 0:
#         if defender in players:
#             print("HEEEEEEEEEEJ")
#             get_experiences(defender,attacker,attacker.forms)
#             kill_player(attacker)
#     elif defender.form_0["current_hp"] <= 0:
#         if attacker in players:
#             print(defender.form_0)
#             print("JEEEEEEEEEEEEEEH")
#             print(defender.forms)
#             get_experiences(attacker,defender,defender.forms)
#             kill_player(defender)

#     after_battle_reset_extras(attacker)
#     after_battle_reset_extras(defender)

#     attacker.dimension = "OUT"
#     defender.dimension = "OUT"

def kill_player(player):
    # print(player.user_name)
    if player.user_name == "HELLKING":
        winner.append("YES")
    
    # print("killing player!")
    # print(player.mark)
    all_player_marks = all_marks() 

    
    if player.pc == "YES":
        pcs.remove(player)
    else:
        players.remove(player)

    # for i in mapa:
    #     if i in all_player_marks:

    for i in range(1,901):
        # print(mapa[i],end="")
        if mapa[i] == f"{player.mark}":
            # print("normal",mapa[i])
            mapa[i] = "|_"
        elif mapa[i] == f"{player.mark}|\n":
            # print("zalomeni",mapa[i])
            mapa[i] = "|_|\n"
    # print("KILLING")

    # for i in range(1,901):
    #     print(mapa[i],end="")
    # update_map(player)
    # input("")

    # for i in mapa:
    #     if mapa[i] == f"{player.mark}":
    #         print("normal",mapa[i])
    #         mapa[i] = "|_"
    #     elif mapa[i] == f"{player.mark}|\n":
    #         print("zalomeni",mapa[i])
    #         mapa[i] = "|_|\n"
        
            
            # print("hovno",mapa[i])



    # for i in mapa:
    #     if i == f"{player.mark}":
    #         i = "|_"
    #         print("Iam here!",i)
    #     elif i == f"{player.mark}|\n":
    #         print("I am here!",i)
    #         i = "|_|\n"
    #     else:
    #         print("I am h e r e",i)
    #         i = "|hovno\n"

    # update_map(player)

def all_marks():
    all_player_marks = []
    for i in players:
        all_player_marks.append(i.mark)

    return all_player_marks


def after_battle_reset_extras(player):
    if type(player) == dict:
        player["extra_atk"] = 0
        player["extra_def"] = 0
        player["extra_acc"] = 0
        player["extra_speed"] = 0

    else:
        for i in player.forms:
            i["extra_atk"] = 0
            i["extra_def"] = 0
            i["extra_acc"] = 0
            i["extra_speed"] = 0



def still_sleep(player):
    sleeping = random.randint(1,7)
    if sleeping > 5:
        
        if type(player) == dict:
            player["status"] = " OK"
            print(f"{player['name']} woke up!")
            input("")
        else:
            player.status = " OK"
            print(f"{player.user_name} woke up!")
            input("")
            
    else:
        if type(player) == dict:
            print(f"{player['name']} is sleeping!")
            input("")
        else:
            print(f"{player.user_name} is sleeping!")
            input("")
                


def battle_lost_soul_title(player,lost_soul):
    player_title(player)
    lost_soul_title(lost_soul)        

def battle_title(attacker,defender):
    player_title(attacker)
    player_title(defender)

def battle_choice_attack_lost_soul(attacking_one, defending_one, attacker, defender):
    # os.system('cls')
    
    attack_choice = ""
    warn_message = ""
    
    while attack_choice == "":
        clean()
        attack_number = 0
        battle_lost_soul_title(attacker,defender)
        print(line)
        print(f"""            {attacking_one.user_name}'s attack list:
                """)
        for i in attacking_one.attack_list:
            attack_number += 1
            print(f"{attack_number:2d}) {i['name']:<21} pwr: {i['power']:1d}  acc: {i['accuracy']:1d}   {i['type']}")
        print("\nB) BACK")
        print(line)
        print(warn_message)
        attack_choice = input(f"{attacking_one.user_name}: CHOOSE YOUR ATTACK: ")

        if attack_choice.isdigit():
            attack_choice = int(attack_choice)
        elif attack_choice.lower() == "b":
            attacking_one.action_done = "NO"
            return 
        else:
            attack_choice = 666

        if attack_choice > len(attacking_one.forms[0]["attack_list"]) or attack_choice == 0:
            warn_message = f"Not in list, choose a number of one of your attacks!"
            attack_choice = ""

    attack = []
    attack_number = 0
    for i in attacking_one.attack_list:
        attack_number +=1
        for ky,vl in i.items():
            if attack_number == attack_choice:
                attack.append(i)
                break
    attack = attack[0]
    clean()
    battle_lost_soul_title(attacker,defender)
    print(line)
    print("")
    if attacking_one.forms[0]["name"] == "NO FORM":
        print(f"{attacking_one.user_name} used {attack['name']}!")
    else:
        print(f"{attacking_one.forms[0]['name']} used {attack['name']}!")
    input("")


    attacking_one.action_done = "YES"
    return landing_attack(attack,defending_one,attacking_one)
    



def battle_choice_attack(attacking_one, defending_one, attacker, defender):
    # os.system('cls')

    attack_choice = ""
    warn_message = ""

    while attack_choice == "":
        clean()
        attack_number = 0
        battle_title(attacker,defender)
        print(line)
        print(f"""        {attacking_one.user_name}'s attack list:
                """)
        for i in attacking_one.attack_list:
            attack_number += 1
            print(f"{attack_number:2d}) {i['name']:<21} pwr: {i['power']:1d}  acc: {i['accuracy']:1d}   {i['type']}")
        print("\nB) BACK")
        print(line)
        print(warn_message)
        attack_choice = input(f"{attacking_one.user_name}: CHOOSE YOUR ATTACK: ")

        if attack_choice.isdigit():
            attack_choice = int(attack_choice)
        elif attack_choice.lower() == "b":
            attacking_one.action_done = "NO"
            return 
        else:
            attack_choice = 666

        if attack_choice > len(attacking_one.forms[0]["attack_list"]) or attack_choice == 0:
            warn_message = f"Not in list, choose a number of one of your attacks!"
            attack_choice = ""


    attack = []
    attack_number = 0
    for i in attacking_one.attack_list:
        attack_number +=1
        for ky,vl in i.items():
            if attack_number == attack_choice:
                attack.append(i)
                break
    attack = attack[0]
    clean()
    battle_title(attacker,defender)
    print(line)
    print("")
    if attacking_one.forms[0]['name'] == "NO FORM":
        print(f"{attacking_one.user_name} used {attack['name']}!")
    else: 
        print(f"{attacking_one.forms[0]['name']} used {attack['name']}!")
    input("")

    attacking_one.action_done = "YES"
    return landing_attack(attack,defending_one,attacking_one)

def battle_choice_form_change(changing_one):
    warn_message = ""
    form_change = ""

    while form_change == "":
        clean()
        player_title(changing_one)
        print(f"""{line}
        {changing_one.user_name}'s FORMS:               
                """)
        form_number = 0
        for i in changing_one.forms:
            form_number += 1
            print(f"{form_number}) {i['name']:<26} L:{i['level']:2d}   HP:{i['current_hp']:4d}/{i['hp']:4d}")
        print(f"\nB) BACK")
        # form_change = int(input("CHOOSE YOUR FORM: "))
        print(warn_message)
        form_change = input("CHOOSE YOUR FORM: ")
        print("")
        if form_change.isdigit():
            form_change = int(form_change)
        elif form_change.lower() == "b":
            changing_one.attack_list = changing_one.forms[0]["attack_list"]
            return 
        else:
            form_change = 666

        if form_change > len(changing_one.forms):
            warn_message = f"Not in list, choose a number of one of your forms!"
            form_change = ""
               
       
    form_number = 0
    for i in changing_one.forms:
        form_number += 1
        if form_number == form_change:
            form_index = changing_one.forms.index(i)
            changing_one.forms[0],changing_one.forms[form_index] = changing_one.forms[form_index],changing_one.forms[0]
            
            changing_one.hp = changing_one.forms[0]["hp"]
            changing_one.level = changing_one.forms[0]["level"]
            changing_one.current_hp = changing_one.forms[0]["current_hp"]
            changing_one.current_form = changing_one.forms[0]["name"]
            changing_one.speed = changing_one.forms[0]["speed"]
            changing_one.attack_list = changing_one.forms[0]["attack_list"]

    changing_one.action_done = "YES"
    
def lost_soul_landing_attack(lost_soul,player):
    # hit = attack["accuracy"] + lost_soul["extra_acc"] + random.randint(1,12)
    
    og_status = ""
    og_status = player.status
    attack = lost_soul["attack_list"][random.randint(0,(len(lost_soul["attack_list"])-1))]
    print(f"{lost_soul['name']} used {attack['name']}!")
    input("")

    OG_def_one = player.forms[0]["current_hp"]
    damage = 0

    hit = attack["accuracy"] + lost_soul["extra_acc"] + random.randint(1,12)
    # print(hit)
    hit += round(((lost_soul["speed"] + lost_soul["extra_speed"]) - (player.forms[0]["speed"] + player.forms[0]["extra_speed"]))/1.5) 
    # print(hit)
    if hit > 7:

        if lost_soul["status"] == "PSN" and attack["antidote"] == "YES":
            print(f"{lost_soul['name']} was cured by {attack['name']}!")
            input("")
            lost_soul["status"] = " OK"
        elif attack["antidote"] == "YES":
            print(f"No effect! {lost_soul['name']} is not currently poisoned.")
            input("")

        if player.status == " OK":
                player.status = attack["status"]

        power_coef = 1

        if attack['type'] == "natural":
            if player.forms[0]["type"] == "violent":
                power_coef = 0.5
                if attack["power"] != 0:
                    print("Not very effective!")
                    input("")

        if attack['type'] == "chaotic":
            if player.forms[0]["type"] == "natural":
                power_coef = 0.5
                if attack["power"] != 0:
                    print("Not very effective!")
                    input("")
            if player.forms[0]["type"] == "violent":
                power_coef = 1.5
                if attack["power"] != 0:
                    print("Extra damage!")
                    input("")
            if player.forms[0]["type"] == "suicide":
                power_coef = 1.5
                if attack["power"] != 0:
                    print("Extra damage!")
                    input("")
        
        if attack['type'] == "violent":
            if player.forms[0]["type"] == "natural":
                power_coef = 1.5
                if attack["power"] != 0:
                    print("Extra damage!")
                    input("")
            if player.forms[0]["type"] == "chaotic":
                power_coef = 0.5
                if attack["power"] != 0:
                    print("Not very effective!")
                    input("")

        if attack["type"] == "suicide":
            if player.forms[0]["type"] == "violent":
                power_coef = 1.5
                if attack["power"] != 0:
                    print("Extra damage!")
                    input("")

        for_def_comp = player.forms[0]["current_hp"]
        player.forms[0]["current_hp"] -= round((lost_soul["level"]*lost_soul["attack_coef"])*(round(attack["power"]*power_coef)+lost_soul["atk"]+lost_soul["extra_atk"]))
        # player.forms[0]["current_hp"] -= round((lost_soul["attack_coef"]*lost_soul["level"])*lost_soul["extra_atk"])
        # player.forms[0]["current_hp"] -= round((lost_soul["attack_coef"]*lost_soul["level"])*lost_soul["atk"])
        player.forms[0]["current_hp"] += round(player.forms[0]["extra_def"] * (player.forms[0]["level"] * player.forms[0]["hp_coef"]))
        player.forms[0]["current_hp"] += round(player.forms[0]["dfk"] * (player.forms[0]["level"] * player.forms[0]["hp_coef"]))
        
        if attack["power"] == 0:
                player.forms[0]["current_hp"] = for_def_comp
        
        if player.forms[0]["current_hp"] >= for_def_comp:
            if attack["power"] == 0:
                player.forms[0]["current_hp"] = for_def_comp
            else:
                player.forms[0]["current_hp"] = for_def_comp -1

        lost_soul["current_hp"] += round(lost_soul["hp"] * attack["heals"])
        # lost_soul["current_hp"] += attack["heals"]
        if attack["heals"] > 0:
            heals_string = str(attack["heals"])[2:]
            if heals_string == ".1" or heals_string == "1":
                heals_string = "10"
            print(f"{lost_soul['name']} recovered by {heals_string} percent of its HP!")
            input("")
        if attack["heals"] < 0:
            heals_string = str(attack["heals"])[3:]
            if heals_string == ".1" or heals_string == "1":
                heals_string = "10"
            print(f"{lost_soul['name']} hurts itself by {heals_string} percent of its HP!")
            input("")

        check_hp(lost_soul)
        if og_status != player.status:
            if attack["status"] == "SLP":
                print(f"{player.user_name} fell asleep!")
            else:    
                print(f"{player.user_name} was poisoned!")

        if OG_def_one > player.forms[0]["current_hp"]:
                damage  =  abs(player.forms[0]["current_hp"] - OG_def_one)


        # EXTRA SPEED
        if attack["extra_speed"] > 0:
            lost_soul["extra_speed"] += attack["extra_speed"]
            if lost_soul["extra_speed"] < 6:
                print(f"{lost_soul['name']}'s speed was improved!")
            input("")
        
        if lost_soul["extra_speed"] > 5:
            print(f"{lost_soul['name']}'s speed cannot be more improved!")
            lost_soul["extra_speed"] = 5
            input("")


        if attack["extra_speed"] < 0:
            player.forms[0]["extra_speed"] += attack["extra_speed"]
            if player.forms[0]["extra_speed"] > -6:
                if player.forms[0]["name"] == "NO FORM":
                    print(f"{player.user_name}'s speed was lowered!")
                else:
                    print(f"{player.forms[0]['name']}'s speed was lowered!")
            input("")

        if player.forms[0]["extra_speed"] < -5:
            if player.forms[0]["name"] == "NO FORM":
                print(f"{player.user_name}'s speed cannot be lowered more!")
            else:
                print(f"{player.forms[0]['name']}'s speed cannot be lowered more!")
            player.forms[0]["extra_speed"] = -5
            input("")

        # EXTRA ACC
        if attack["extra_acc"] > 0:
            lost_soul["extra_acc"] += attack["extra_acc"]
            if lost_soul["extra_acc"] < 6:
                print(f"{lost_soul['name']}'s accuracy was improved!")
            input("")
        
        if lost_soul["extra_acc"] > 5:
            print(f"{lost_soul['name']}'s accuracy cannot be more improved!")
            lost_soul["extra_acc"] = 5
            input("")


        if attack["extra_acc"] < 0:
            player.forms[0]["extra_acc"] += attack["extra_acc"]
            if player.forms[0]["extra_acc"] > -6:
                if player.forms[0]["name"] == "NO FORM":
                    print(f"{player.user_name}'s accuracy was lowered!")
                else:
                    print(f"{player.forms[0]['name']}'s accuracy was lowered!")
            input("")

        if player.forms[0]["extra_acc"] < -5:
            if player.forms[0]["name"] == "NO FORM":
                print(f"{player.user_name}'s accuracy cannot be lowered more!")
            else:
                print(f"{player.forms[0]['name']}'s accuracy cannot be lowered more!")
            player.forms[0]["extra_acc"] = -5
            input("")


        # EXTRA DEF
        if attack["extra_def"] > 0:
            lost_soul["extra_def"] += attack["extra_def"]
            if lost_soul["extra_def"] < 6:
                print(f"{lost_soul['name']}'s defence was improved!")
            input("")
        
        if lost_soul["extra_def"] > 5:
            print(f"{lost_soul['name']}'s defence cannot be more improved!")
            lost_soul["extra_def"] = 5
            input("")


        if attack["extra_def"] < 0:
            player.forms[0]["extra_def"] += attack["extra_def"]
            if player.forms[0]["extra_def"] > -6:
                if player.forms[0]["name"] == "NO FORM":
                    print(f"{player.user_name}'s defence was lowered!")
                else:
                    print(f"{player.forms[0]['name']}'s defence was lowered!")
            input("")

        if player.forms[0]["extra_def"] < -5:
            if player.forms[0]["name"] == "NO FORM":
                print(f"{player.user_name}'s defence cannot be lowered more!")
            else:
                print(f"{player.forms[0]['name']}'s defence cannot be lowered more!")
            player.forms[0]["extra_def"] = -5
            input("")


        # EXTRA ATTACK
        if attack["extra_atk"] > 0:
            lost_soul["extra_atk"] += attack["extra_atk"]
            if lost_soul["extra_atk"] < 6:
                print(f"{lost_soul['name']}'s attack was improved!")
            input("")
        
        if lost_soul["extra_atk"] > 5:
            print(f"{lost_soul['name']}'s attack cannot be more improved!")
            lost_soul["extra_atk"] = 5
            input("")


        if attack["extra_atk"] < 0:
            player.forms[0]["extra_atk"] += attack["extra_atk"]
            if player.forms[0]["extra_atk"] > -6:
                if player.forms[0]["name"] == "NO FORM":
                    print(f"{player.user_name}'s attack was lowered!")
                else:
                    print(f"{player.forms[0]['name']}'s attack was lowered!")
            input("")

        if player.forms[0]["extra_atk"] < -5:
            if player.forms[0]["name"] == "NO FORM":
                print(f"{player.user_name}'s attack cannot be lowered more!")
            else:
                print(f"{player.forms[0]['name']}'s attack cannot be lowered more!")
            player.forms[0]["extra_atk"] = -5
            input("")

        if damage > 0:

            if player.forms[0]['name'] == "NO FORM":
                print(f"{player.user_name} suffered {damage} HP damage!")
            else:
                print(f"{player.forms[0]['name']} suffered {damage} HP damage!")
            input("")

    else:        
        print(f"{lost_soul['name']} attack missed!")
        input("")

    # print(hit)
    



    
def landing_attack(attack,defending_one,attacking_one):
    # print("defending_one user_name:",defending_one.user_name)
    # print("len attacking one forms",len(attacking_one.forms))
    # print("defending one status",defending_one.status)
    # input("")
    OG_def_one = 0    
    damage = 0

    if type(defending_one) != dict:
        if defending_one.user_name == "HELLKING" and len(attacking_one.forms) == 1 and defending_one.status != "PSN":
            attacking_one.forms[0]["current_hp"] = -1
            print(f"Basic forms cannot attack straight on each other! Nothing happened!\n Considering {attacking_one.user_name} cannot escape of this battle, he commited a suicide!")
            input("")
            return
        
        if defending_one.forms[0]["name"] == "NO FORM" and attacking_one.forms[0]["name"] == "NO FORM" and attacking_one.forms[0]["OG_NAME"] != "HELLKING":
            print("Basic forms cannot attack straight on each other! Nothing happened!")
            input("")
            return
        
        
    hit = attack["accuracy"] + attacking_one.forms[0]["extra_acc"] + random.randint(1,12)
    # print(hit)
    if type(defending_one) == dict:
        OG_def_one = defending_one["current_hp"]

        hit += round(((attacking_one.forms[0]["speed"] + attacking_one.forms[0]["extra_speed"]) - (defending_one["speed"] + defending_one["extra_speed"]))/1.5)
        # print(hit)
    else:
        OG_def_one = defending_one.forms[0]["current_hp"]

        hit += round(((attacking_one.forms[0]["speed"] + attacking_one.forms[0]["extra_speed"]) - (defending_one.forms[0]["speed"] + defending_one.forms[0]["extra_speed"]))/1.5)
        
        # print(hit)
    if hit > 7:

        if attacking_one.status == "PSN" and attack["antidote"] == "YES":
            print(f"{attacking_one.user_name} was cured by {attack['name']}!")
            input("")
            attacking_one.status = " OK"
        elif attack["antidote"] == "YES":
            print(f"No effect! {attacking_one.user_name} is not currently poisoned!")
            input("")

        og_status= ""
        if type(defending_one) == dict:

            power_coef = 1

            if attack['type'] == "natural":
                if defending_one["type"] == "violent":
                    power_coef = 0.5
                    if attack["power"] != 0:
                        print("Not very effective!")
                        input("")

            if attack['type'] == "chaotic":
                if defending_one["type"] == "natural":
                    power_coef = 0.5
                    if attack["power"] != 0:
                        print("Not very effective!")
                        input("")
                if defending_one["type"] == "violent":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")
                if defending_one["type"] == "suicide":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")
            
            if attack['type'] == "violent":
                if defending_one["type"] == "natural":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")
                if defending_one["type"] == "chaotic":
                    power_coef = 0.5
                    if attack["power"] != 0:
                        print("Not very effective!")
                        input("")

            if attack["type"] == "suicide":
                if defending_one["type"] == "violent":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")


            og_status = defending_one["status"]

            for_def_comp = defending_one["current_hp"]
            defending_one["current_hp"] -= round((attacking_one.forms[0]["level"]*attacking_one.forms[0]["attack_coef"])*(round(attack["power"] * power_coef)+attacking_one.forms[0]["extra_atk"]+attacking_one.forms[0]["atk"]))
            # defending_one["current_hp"] -= round(attacking_one.forms[0]["extra_atk"] * (attacking_one.forms[0]["level"] * attacking_one.forms[0]["attack_coef"]))
            # defending_one["current_hp"] -= round(attacking_one.forms[0]["atk"] * (attacking_one.forms[0]["level"] * attacking_one.forms[0]["attack_coef"]))
            defending_one["current_hp"] += round(defending_one["extra_def"] * (defending_one["hp_coef"] * defending_one["level"]))
            defending_one["current_hp"] += round(defending_one["dfk"] * (defending_one["hp_coef"] * defending_one["level"]))
            
            if attack["power"] == 0:
                    defending_one["current_hp"] = for_def_comp
            
            if defending_one["current_hp"] >= for_def_comp:
                if attack["power"] == 0:
                    defending_one["current_hp"] = for_def_comp
                else:
                    defending_one["current_hp"] = for_def_comp - 1
            

                    
            attacking_one.forms[0]["current_hp"] += round(attacking_one.forms[0]["hp"] * attack["heals"])
            # attacking_one.forms[0]["current_hp"] += attack["heals"]

            

            if attack["heals"] > 0:
                heals_string = str(attack["heals"])[2:]
                if heals_string == ".1" or heals_string == "1":
                    heals_string = "10"
                if attacking_one.forms[0]["name"] == "NO FORM":
                    print(f"{attacking_one.user_name} recovered by {heals_string} percent of its HP!")
                else:
                    print(f"{attacking_one.forms[0]['name']} recovered by {heals_string} percent of its HP!")
                input("")

            if attack["heals"] < 0:
                heals_string = str(attack["heals"])[3:]
                if heals_string == ".1" or heals_string == "1":
                    heals_string = "10"
                if attacking_one.forms[0]["name"] == "NO FORM":
                    print(f"{attacking_one.user_name} hurt itself by {heals_string} percent of its HP!")
                else:
                    print(f"{attacking_one.forms[0]['name']} hurt itself by {heals_string} percent of its HP!")
                input("")
            check_hp(attacking_one)
            if defending_one["status"] == " OK":
                defending_one["status"] = attack["status"]
            if og_status != defending_one["status"]:
                if defending_one["status"] == "SLP":
                    print(f"{defending_one['name']} fell asleep!")
                else:
                    print(f"{defending_one['name']} was poisoned!")

            if OG_def_one > defending_one["current_hp"]:
                damage  =  abs(defending_one["current_hp"] - OG_def_one)
                
        else:

            power_coef = 1

            if attack['type'] == "natural":
                if defending_one.forms[0]["type"] == "violent":
                    power_coef = 0.5
                    if attack["power"] != 0:
                        print("Not very effective!")
                        input("")

            if attack['type'] == "chaotic":
                if defending_one.forms[0]["type"] == "natural":
                    power_coef = 0.5
                    if attack["power"] != 0:
                        print("Not very effective!")
                        input("")
                if defending_one.forms[0]["type"] == "violent":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")
                if defending_one.forms[0]["type"] == "suicide":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")
            
            if attack['type'] == "violent":
                if defending_one.forms[0]["type"] == "natural":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")
                if defending_one.forms[0]["type"] == "chaotic":
                    power_coef = 0.5
                    if attack["power"] != 0:
                        print("Not very effective!")
                        input("")

            if attack["type"] == "suicide":
                if defending_one.forms[0]["type"] == "violent":
                    power_coef = 1.5
                    if attack["power"] != 0:
                        print("Extra damage!")
                        input("")

            og_status = defending_one.status

            for_def_comp = defending_one.forms[0]["current_hp"]
            defending_one.forms[0]["current_hp"] -= round((attacking_one.forms[0]["level"]*attacking_one.forms[0]["attack_coef"])*(round(attack["power"]*power_coef)+attacking_one.forms[0]["extra_atk"]+attacking_one.forms[0]["atk"]))
            # defending_one.forms[0]["current_hp"] -= round(attacking_one.forms[0]["extra_atk"] * (attacking_one.forms[0]["level"]*attacking_one.forms[0]["attack_coef"]))
            # defending_one.forms[0]["current_hp"] -= round(attacking_one.forms[0]["atk"] * (attacking_one.forms[0]["level"]*attacking_one.forms[0]["attack_coef"]))
            defending_one.forms[0]["current_hp"] += round(defending_one.forms[0]["extra_def"] * (defending_one.forms[0]["hp_coef"]*defending_one.forms[0]["level"]))
            defending_one.forms[0]["current_hp"] += round(defending_one.forms[0]["dfk"] * (defending_one.forms[0]["hp_coef"]*defending_one.forms[0]["level"]))
            
            if attack["power"] == 0:
                defending_one.forms[0]["current_hp"] = for_def_comp
            
            if defending_one.forms[0]["current_hp"] >= for_def_comp:
                if attack["power"] == 0:
                    defending_one.forms[0]["current_hp"] = for_def_comp
                else:
                    defending_one.forms[0]["current_hp"] = for_def_comp - 1
        
            if type(attacking_one) == dict:
                attacking_one["current_hp"] += round(attacking_one["hp"] * attack["heals"])
                check_hp(attacking_one)
            else:
                attacking_one.forms[0]["current_hp"] += round(attacking_one.forms[0]["hp"] * attack["heals"])
                check_hp(attacking_one)
            if defending_one.status == " OK":
                defending_one.status = attack["status"]
            if og_status != defending_one.status:
                if defending_one.status == "SLP":
                    print(f"{defending_one.user_name} fell asleep!")
                else:
                    print(f"{defending_one.user_name} was poisoned!")

            if OG_def_one > defending_one.forms[0]["current_hp"]:
                damage  =  abs(defending_one.forms[0]["current_hp"] - OG_def_one)

        # EXTRA SPEED
        if attack["extra_speed"] < 0:
            if type(defending_one) == dict:
                defending_one["extra_speed"] =+ attack["extra_speed"]
                if defending_one["extra_speed"] > -6:
                    print(f"{defending_one['name']}'s speed was lowered!")

                if defending_one["extra_speed"] < -5:
                    print(f"{defending_one['name']}'s speed cannot be lowered more!")
                    defending_one["extra_speed"] = -5

            else:
                defending_one.forms[0]["extra_speed"] += attack["extra_speed"]
                if defending_one.forms[0]["extra_speed"] > -6:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s speed was lowered!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s speed was lowered!")
                
                if defending_one.forms[0]["extra_speed"] < -5:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s speed cannot be lowered more!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s speed cannot be lowered more!")
                    defending_one.forms[0]["extra_speed"] = -5
            input("")

        if attack["extra_speed"] > 0:
            attacking_one.forms[0]["extra_speed"] += attack["extra_speed"]
            if attacking_one.forms[0]["extra_speed"] < 6:
                if attacking_one.forms[0]["name"] == "NO FORM":
                    print(f"{attacking_one.user_name}'s speed was improved!")
                else:
                    print(f"{attacking_one.forms[0]['name']}'s speed was improved!")
            input("")

            
        if attacking_one.forms[0]["extra_speed"] > 5:
            if attacking_one.forms[0]['name'] == "NO FORM":
                print(f"{attacking_one.user_name}'s speed cannot be more improved!") 
            else:
                print(f"{attacking_one.forms[0]['name']}'s speed cannot be more improved!")  
            attacking_one.forms[0]["extra_speed"] = 5
            input("")


        # EXTRA ACC
        if attack["extra_acc"] < 0:
            if type(defending_one) == dict:
                defending_one["extra_acc"] =+ attack["extra_acc"]
                if defending_one["extra_acc"] > -6:
                    print(f"{defending_one['name']}'s accuracy was lowered!")

                if defending_one["extra_acc"] < -5:
                    print(f"{defending_one['name']}'s accuracy cannot be lowered more!")
                    defending_one["extra_acc"] = -5
            

            else:
                defending_one.forms[0]["extra_acc"] += attack["extra_acc"]
                if defending_one.forms[0]["extra_acc"] > -6:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s accuracy was lowered!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s accuracy was lowered!")
                
                if defending_one.forms[0]["extra_acc"] < -5:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s accuracy cannot be lowered more!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s accuracy cannot be lowered more!")
                    defending_one.forms[0]["extra_acc"] = -5
            input("")

        if attack["extra_acc"] > 0:
            attacking_one.forms[0]["extra_acc"] += attack["extra_acc"]
            if attacking_one.forms[0]["extra_acc"] < 6:
                if attacking_one.forms[0]["name"] == "NO FORM":
                    print(f"{attacking_one.user_name}'s accuracy was improved!")
                else:
                    print(f"{attacking_one.forms[0]['name']}'s accuracy was improved!")
            input("")

            
        if attacking_one.forms[0]["extra_acc"] > 5:
            if attacking_one.forms[0]['name'] == "NO FORM":
                print(f"{attacking_one.user_name}'s accuracy cannot be more improved!") 
            else:
                print(f"{attacking_one.forms[0]['name']}'s accuracy cannot be more improved!")  
            attacking_one.forms[0]["extra_acc"] = 5
            input("")


        # EXTRA DEF
        if attack["extra_def"] < 0:
            if type(defending_one) == dict:
                defending_one["extra_def"] =+ attack["extra_def"]
                if defending_one["extra_def"] > -6:
                    print(f"{defending_one['name']}'s defence was lowered!")

                if defending_one["extra_def"] < -5:
                    print(f"{defending_one['name']}'s defence cannot be lowered more!")
                    defending_one["extra_def"] = -5

            else:
                defending_one.forms[0]["extra_def"] += attack["extra_def"]
                if defending_one.forms[0]["extra_def"] > -6:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s defence was lowered!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s defence was lowered!")
                
                if defending_one.forms[0]["extra_def"] < -5:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s defence cannot be lowered more!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s defence cannot be lowered more!")
                    defending_one.forms[0]["extra_def"] = -5
            input("")

        if attack["extra_def"] > 0:
            attacking_one.forms[0]["extra_def"] += attack["extra_def"]
            if attacking_one.forms[0]["extra_def"] < 6:
                if attacking_one.forms[0]["name"] == "NO FORM":
                    print(f"{attacking_one.user_name}'s defence was improved!")
                else:
                    print(f"{attacking_one.forms[0]['name']}'s defence was improved!")
            input("")

            
        if attacking_one.forms[0]["extra_def"] > 5:
            if attacking_one.forms[0]['name'] == "NO FORM":
                print(f"{attacking_one.user_name}'s defence cannot be more improved!") 
            else:
                print(f"{attacking_one.forms[0]['name']}'s defence cannot be more improved!")  
            attacking_one.forms[0]["extra_def"] = 5
            input("")
                


        # EXTRA ATTACK
        if attack["extra_atk"] < 0:
            if type(defending_one) == dict:
                defending_one["extra_atk"] += attack["extra_atk"]
                if defending_one["extra_atk"] > -6:
                    print(f"{defending_one['name']}'s attack was lowered!")

                if defending_one["extra_atk"] < -5:
                    print(f"{defending_one['name']}'s attack cannot be lowered more!")
                    defending_one["extra_atk"] = -5
            else:
                defending_one.forms[0]["extra_atk"] += attack["extra_atk"]
                if defending_one.forms[0]["extra_atk"] > -6:
                    if defending_one.forms[0]["name"] == "NO FORM":
                        print(f"{defending_one.user_name}'s attack was lowered!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s attack was lowered!")

                if defending_one.forms[0]["extra_atk"] < -5:
                    if defending_one.forms[0]['name'] == "NO FORM":
                        print(f"{defending_one.user_name}'s attack cannot be lowered more!")
                    else:
                        print(f"{defending_one.forms[0]['name']}'s attack cannot be lowered more!")
                    defending_one.forms[0]["extra_atk"] = -5
            input("")
        
            

        if attack["extra_atk"] > 0:
            attacking_one.forms[0]["extra_atk"] += attack["extra_atk"]
            if attacking_one.forms[0]["extra_atk"] < 6:
                if attacking_one.forms[0]["name"] == "NO FORM":
                    print(f"{attacking_one.user_name}'s attack was improved!")
                else:
                    print(f"{attacking_one.forms[0]['name']}'s attack was improved!")
            input("")

            
        if attacking_one.forms[0]["extra_atk"] > 5:
            if attacking_one.forms[0]['name'] == "NO FORM":
                print(f"{attacking_one.user_name}'s attack cannot be more improved!") 
            else:
                print(f"{attacking_one.forms[0]['name']}'s attack cannot be more improved!")  
            attacking_one.forms[0]["extra_atk"] = 5
            input("")
        
        if damage > 0:
            if type(defending_one) == dict:
                print(f"{defending_one['name']} suffered {damage} HP damage!")
                input("")
            else:
                if defending_one.forms[0]['name'] == "NO FORM":
                    print(f"{defending_one.user_name} suffered {damage} HP damage!")
                else:
                    print(f"{defending_one.forms[0]['name']} suffered {damage} HP damage!")
                input("")


    else:
        if attacking_one.forms[0]["name"] == "NO FORM":
            print(f"{attacking_one.user_name} attack missed!")
            input("")
        else:
            print(f"{attacking_one.forms[0]['name']} attack missed!")
            input("")

    # print(hit)

def check_hp(player):
    
    if type(player) == dict:
        if player["current_hp"] > player["hp"]:
            player["current_hp"] = player["hp"]
    else:
        if player.forms[0]["current_hp"] > player.forms[0]["hp"]:
            player.forms[0]["current_hp"] = player.forms[0]["hp"]    
        

def lost_soul_title(lost_soul):
    ls_hp = lost_soul["hp"]
    ls_level = lost_soul["level"]
    ls_speed = lost_soul["speed"]
    ls_current_hp = lost_soul["current_hp"]
    
    print(f"""{line}
{lost_soul["name"]:<38}status: {lost_soul["status"]:<4}
{"wandering soul":<26}level:{ls_level:2d}   HP:{ls_current_hp:4d}/{ls_hp:4d}""")   

    # print(lost_soul["exp"])
    # print(lost_soul["attack_list"])
    # print("extra atk:",lost_soul["extra_atk"])
    # print("extra def:",lost_soul["extra_def"])
    # print("extra acc:",lost_soul["extra_acc"])
    # print("atk:",lost_soul["atk"])
    # print("dfk:",lost_soul["dfk"])
    # print("speed:",lost_soul["speed"])
    # print("extra speed:",lost_soul["extra_speed"])
    


def player_title(player):
    player.hp = player.forms[0]["hp"]
    player.level = player.forms[0]["level"]
    player.current_hp = player.forms[0]["current_hp"]
    player.current_form = player.forms[0]["name"]
    player.speed = player.forms[0]["speed"]
       

    print(f"""{line}    
({player.name}) {player.user_name:<34}status: {player.status:<4}
{player.current_form:<26}level:{player.level:2d}   HP:{player.current_hp:4d}/{player.hp:4d}""")    
    # print(player.forms[0]["exp"])
    # print("current",player.where[0])
    # print("backup",player.backout)

    # print("extra atk:",player.forms[0]["extra_atk"])
    # print("extra def:",player.forms[0]["extra_def"])
    # print("extra acc:",player.forms[0]["extra_acc"])
    # print("atk:",player.forms[0]["atk"])
    # print("dfk:",player.forms[0]["dfk"])
    # print("speed:",player.forms[0]["speed"])
    # print("extra speed:",player.forms[0]["extra_speed"])
    
def forms_menu(player):
    warn_message = ""
    while True:
        show_player_forms(player)
                
        print("\nB) BACK")
        print(warn_message)
        form_choice = input("CHOOSE YOUR FORM: ")

        if form_choice.isdigit():
            form_choice = int(form_choice)
            if form_choice > len(player.forms) or form_choice == 0:
                warn_message = "Not in the list. Try again!"
            else:
                warn_message = ""
                break     
        elif form_choice.lower() == "b":
            return
        else:
            warn_message = "Not in the list. Try again!" 

    for i in player.forms:
        if i["name"] == player.forms[form_choice -1]["name"]:
            form_options(player,i)
            
def form_options(player,form):
    warn_message = ''
    warning = "Not in the menu. Try again!"
    while True:
        clean()
        player_title(player)
        print(f"""{line}
        {player.user_name}'s FORMS:               
                    """)        
        if form["name"] == "NO FORM":
            player_info(player)
        else:
            print(line)
            print(f"{player.user_name}'s {form['name']} INFO:\n{line}")
            print(f"{'':>2}KIND: {form['OG_NAME'].upper()}")
            print(f"{'':>2}TYPE: {form['type'].upper()}")
            print(f"{'':>2}HP: {form['current_hp']:3d}/{form['hp']:3d}{'':>6}STATUS:{player.status}")
            print(f"{'':>2}LEVEL: {form['level']:2d}")
            print(f"{'':>2}EXP Points to level {form['level'] +1}: {experience_levels[form['level'] +1] - form['exp']}")
            # print(f"this is base hp: {form['base_hp']} and this is hp: {form['hp']}")

            print("\nSTATS:")
            print(f"{'':>2}SPEED:   {form['speed']:2d}")
            print(f"{'':>2}ATTACK:  {form['atk']:2d}")
            print(f"{'':>2}DEFENCE: {form['dfk']:2d}")

            
            print("\nMOVELIST: ")
            attacks = 0
            for i in form["attack_list"]:
                attacks += 1
                if attacks == len(form["attack_list"]):
                    print(" ",i["name"]+"\n")
                elif attacks % 3 == 0:
                    print(" ",i["name"]+",")
                else:
                    print(" ",i["name"]+",",end="")
            
            print(line)
            print("")

        if form["name"] == "NO FORM":
            if form != player.forms[0]:
                print("T) TAKE THIS FORM")
            else:
                print(f"{player.user_name} is currently in this form.")
            print("\nB) BACK")
            
        else:
            if form != player.forms[0]:
                print("T) TAKE THIS FORM")
                print("R) RELEASE THIS FORM")
            else:
                print(f"{player.user_name} is currently in this form.")
            
            print("\nB) BACK")

        print(warn_message)    
        form_action = input("CHOOSE YOUR ACTION: ")

        if form_action.lower() not in ("t","r","b"):
            warn_message = warning
        elif form_action.lower() == "b":
            warn_message = ''
            break
        elif form_action.lower() == "r":
            if form != player.forms[0] or form["name"] != "NO FORM":
                # print(f"{player.user_name} have released {form['name']}!")                
                release_form(player,form)
                input("")
                break
            else:
                warn_message = warning
        elif form_action.lower() == "t":
            if form != player.forms[0] or form["name"] != "NO FORM":
                print("taking form!")

                form_number = -1
                for i in player.forms:
                    form_number += 1
                    if i == form:
                        player.forms[0],player.forms[form_number] = player.forms[form_number],player.forms[0]
                
                player.hp = player.forms[0]["hp"]
                player.level = player.forms[0]["level"]
                player.current_hp = player.forms[0]["current_hp"]
                player.current_form = player.forms[0]["name"]
                player.speed = player.forms[0]["speed"]
                player.attack_list = player.forms[0]["attack_list"]

                clean()
                player_title(player)
                print(f"""{line}
        {player.user_name}'s FORMS:               
                    """)        
                if player.forms[0]["name"] == "NO FORM":
                    print(f"{player.user_name} have changed form to its basic form!")
                else:
                    print(f"{player.user_name} have changed form to {form['name']}!")
                input("")

                break
            else:
                warn_message = warning

def release_form(player,form):
    # clean()
    warn_message = ''
    warning = "You have to choose (Y)es or (N)o! Try again!"
    while True:
        clean()
        player_title(player)
        print(f"""{line}
        {player.user_name}'s FORMS:               
                    """)
        
        print(warn_message)
        release_choice = input(f"Do you really want to release {form['name']}? (Y/N) ")

        if release_choice.lower() not in ("y","n"):
            warn_message = warning
        elif release_choice.lower() == "y":
            clean()
            player_title(player)
            print(f"""{line}
        {player.user_name}'s FORMS:               
                    """)
            print(f"\nOk, releasing {form['name']}!")
            input("")
            break
        else:
            clean()
            player_title(player)
            print(f"""{line}
        {player.user_name}'s FORMS:               
                    """)
            print(f"\n{form['name']} stays as one of {player.user_name}'s forms!")
            input("")
            return
    

    for i in player.forms:
        if i == form:
            player.forms.remove(form)
            clean_acquired(player,form)

def player_info(player):
    print(line)
    print(f"{player.user_name}'s BASE FORM INFO:\n{line}")
    print(f"{'':>2}HP: {player.form_0['current_hp']:3d}/{player.form_0['hp']:3d}{'':>6}STATUS:{player.status}")
    print(f"{'':>2}LEVEL: {player.form_0['level']:2d}")
    print(f"{'':>2}EXP Points to level {player.form_0['level'] +1}: {experience_levels[player.form_0['level'] +1] - player.form_0['exp']}")
    # print(f"this is base hp: {player.form_0['base_hp']} and this is hp: {player.form_0['hp']}")

    print("\nSTATS:")
    print(f"{'':>2}SPEED:   {player.form_0['speed']:2d}")
    print(f"{'':>2}ATTACK:  {player.form_0['atk']:2d}")
    print(f"{'':>2}DEFENCE: {player.form_0['dfk']:2d}")

    print("\nMOVELIST: ")
    attacks = 0
    for i in player.form_0["attack_list"]:
        attacks += 1
        if attacks == len(player.form_0["attack_list"]):
            print(" ",i["name"]+"\n")
        elif attacks % 3 == 0:
            print(" ",i["name"]+",")
        else:
            print(" ",i["name"]+",",end="")

    print(line)
    print("")
   

    
        

def create_map():
    mapa = {}
    item_fields = []

    for i in range(900):
        mapa[i+1] = "|_"

    for i in range(1,31):
        mapa[i*30] = "|_|\n"
   
    return mapa

def create_item():
    item_fields = []

    for i in range(1,900):
        if mapa[i] == "|_":
            item_fields.append(i)
        
    mapa[item_fields[random.randint(1,len(item_fields)-1)]] = "|*" 

def update_map(player):
    # others = []
    # others_end = []
    
    # for i in players:
    #     if i.mark != player.mark:
    #         others.append(i.mark)

    # for i in players:
    #     if i.mark != player.mark:
    #         others_end.append(f"{i.mark}|\n")

    # print("others",others)
    # print("others end",others_end)
    # input("")
    clean()
    if player in players or player in pcs:
        if player.run == "YES":
            re_back = player.where[0]
            if mapa[player.where[0]] == f"{player.mark}|\n":
                mapa[player.where[0]] = "|_|\n"
            elif mapa[player.where[0]] == player.mark:
                mapa[player.where[0]] = "|_"

            player.where[0] = player.backout
            player.run = "NO"
            if mapa[player.where[0]] == "|_|\n":
                mapa[player.where[0]] = f"{player.mark}|\n"
                player.backout = re_back
            else:
                mapa[player.where[0]] = player.mark
                player.backout = re_back

            # for i in others:
            #     if i == re_back:
            #         mapa[re_back] = i

            # for i in others_end:
            #     if i == re_back:
            #         mapa[re_back] = i


        else:
            if mapa[player.where[0]] == "|_|\n":
                mapa[player.where[0]] = f"{player.mark}|\n"
            elif mapa[player.where[0]] == "|_":             
                mapa[player.where[0]] = player.mark
            else:
                pass



def create_player(player_name,symbol):
    

    Player(symbol, player_name)            
    
    game_logo()
    print(f"\nPlayer {player_name} was created. Its symbol in the game will be {symbol}!")
    input("")
    

def main_game_mode():
    clean()
    dm_active = "NO"
    if len(deathmatch) > 0:
        dm_active = "YES"

    if dm_active == "NO":
        natural_master = Player("≡","NATURAL MASTER")    
        natural_master.pc = "YES"

        violent_master = Player("×","VIOLENT MASTER")    
        violent_master.pc = "YES"
    
        chaotic_master = Player("▒","CHAOTIC MASTER")    
        chaotic_master.pc = "YES"
    
        suicide_master = Player("¤","SUICIDE MASTER")    
        suicide_master.pc = "YES"
    
    for i in players:
        i.remove_form()
        
        if i.user_name == "NATURAL MASTER":
            i.acquire_form(no_form_natural_master)
            i.attack_list = i.forms[0]["attack_list"]
            
            i.forms[0]["hp"] = no_form_natural_master["hp"] * round(no_form_natural_master["hp_coef"] * no_form_natural_master["level"]) + no_form_natural_master["extra_hp"]
            i.forms[0]["current_hp"] = no_form_natural_master["hp"] * round(no_form_natural_master["hp_coef"] * no_form_natural_master["level"]) + no_form_natural_master["extra_hp"] 
        elif i.user_name == "VIOLENT MASTER":
            i.acquire_form(no_form_violent_master)
            i.attack_list = i.forms[0]["attack_list"]
            
            i.forms[0]["hp"] = no_form_violent_master["hp"] * round(no_form_violent_master["hp_coef"] * no_form_violent_master["level"]) + no_form_violent_master["extra_hp"]
            i.forms[0]["current_hp"] = no_form_violent_master["hp"] * round(no_form_violent_master["hp_coef"] * no_form_violent_master["level"]) + no_form_violent_master["extra_hp"] 
        elif i.user_name == "CHAOTIC MASTER":
            i.acquire_form(no_form_chaotic_master)
            i.attack_list = i.forms[0]["attack_list"]
            
            i.forms[0]["hp"] = no_form_chaotic_master["hp"] * round(no_form_chaotic_master["hp_coef"] * no_form_chaotic_master["level"]) + no_form_chaotic_master["extra_hp"]
            i.forms[0]["current_hp"] = no_form_chaotic_master["hp"] * round(no_form_chaotic_master["hp_coef"] * no_form_chaotic_master["level"]) + no_form_chaotic_master["extra_hp"] 
        elif i.user_name == "SUICIDE MASTER":
            i.acquire_form(no_form_suicide_master)
            i.attack_list = i.forms[0]["attack_list"]
            
            i.forms[0]["hp"] = no_form_suicide_master["hp"] * round(no_form_suicide_master["hp_coef"] * no_form_suicide_master["level"]) + no_form_suicide_master["extra_hp"]
            i.forms[0]["current_hp"] = no_form_suicide_master["hp"] * round(no_form_suicide_master["hp_coef"] * no_form_suicide_master["level"]) + no_form_suicide_master["extra_hp"] 
        else:    
            i.acquire_form(no_form)
            i.attack_list = i.forms[0]["attack_list"]
            
            i.forms[0]["hp"] = no_form["hp"] * round(no_form["hp_coef"] * no_form["level"]) + no_form["extra_hp"]
            i.forms[0]["current_hp"] = no_form["hp"] * round(no_form["hp_coef"] * no_form["level"]) + no_form["extra_hp"] 

    if dm_active == "NO":
        
        natural_master.acquire_form(hound_natural)
        natural_master.acquire_form(viper_natural)
        natural_master.acquire_form(giraffe_natural)
        natural_master.acquire_form(panda_natural)               


        violent_master.acquire_form(ostrich_violent)
        violent_master.acquire_form(scorpion_violent)
        violent_master.acquire_form(stag_violent)
        violent_master.acquire_form(rat_violent)
        # violent_master.acquire_form(no_form_master)
        

        chaotic_master.acquire_form(anteater_chaotic)
        chaotic_master.acquire_form(alligator_chaotic)
        chaotic_master.acquire_form(eagle_chaotic)
        chaotic_master.acquire_form(platypus_chaotic)
        # chaotic_master.acquire_form(no_form_master)
        

        suicide_master.acquire_form(bullfrog_suicide)
        suicide_master.acquire_form(lion_suicide)
        suicide_master.acquire_form(rat_suicide)
        suicide_master.acquire_form(boar_suicide)
        # suicide_master.acquire_form(no_form_master)        

    
    # print("players before:",players)

    for i in players:
        if i.pc == "YES":    
            print(i.user_name)    
            pcs.append(i)        
    
    for i in pcs: 
        if i in players:
            players.remove(i)

    # print("players after:",players)

    for i in players:
        pass
        # print(i.user_name)
        # i.acquire_form(polar_bear)

    # player3.acquire_form(polar_bear)
    

    for i in pcs:
        i.forms[0],i.forms[-1] = i.forms[-1],i.forms[0]
        

    # for i in pcs:
        
    #     i.forms.pop(0)

          

    # print(natural_master.forms)
    # print(violent_master.forms)
    # print(chaotic_master.forms)
    # print(suicide_master.forms)

    # input("")

    for i in pcs:
        for j in i.forms:
            # j["current_hp"] = j["hp"]
            if j["name"] != "NO FORM":
                j["hp"] = j["hp"] * round(j["hp_coef"] * j["level"]) + j["extra_hp"]
                j["current_hp"] = j["hp"]

    # for i in pcs:
    #     for j in i.forms:
    #         # j["current_hp"] = j["hp"]
    #         # if j["name"] != "NO FORM":
    #         j["hp"] = j["hp"] * round(j["hp_coef"] * j["level"]) + j["extra_hp"]
    #         j["current_hp"] = j["hp"]

    # for i in pcs:
    #     for j in i.forms:
    #         # j["current_hp"] = j["hp"]
    #         if j["name"] == "NO FORM II":
    #             j["name"] = "NO FORM"



    # player3.where[0] = 40


    # print("players",players)
    # print("pcs",pcs)

    while True:
        clean()
        if len(players) > 0:
            if len(pcs) > 0:
                for i in pcs:
                    i.pc_turn()

            
            for i in players:
                if dm_active == "YES":
                    if len(players) == 1:
                        print(f"{i.user_name} is the DEATHMATCH WINNER!")   
                        return exit()     
                # print(f"{i.user_name}'s TURN!")
               
                i.player_turn()

                hell_king = ""
                
                if dm_active == "NO":
                    if i in players and len(pcs) == 0:
                        if len(boss_fight) < 1:

                            # print("boss fight:",boss_fight)

                            # print(pcs)
                            
                            hell_king = Player("^","HELLKING")
                            pcs.append(hell_king)
                            boss_fight.append(hell_king)
                            
                            players.remove(hell_king)
                            hell_king.pc = "YES"
                            # hell_king.backout = i.where
                            # hell_king.where = i.where

                            hell_king.remove_form()
                            hell_king.acquire_form(no_form_hellking)
                            hell_king.attack_list = hell_king.forms[0]["attack_list"]
                            
                            hell_king.forms[0]["hp"] = no_form_hellking["hp"] * round(no_form_hellking["hp_coef"] * no_form_hellking["level"]) + no_form_hellking["extra_hp"]
                            hell_king.forms[0]["current_hp"] = no_form_hellking["hp"] * round(no_form_hellking["hp_coef"] * no_form_hellking["level"]) + no_form_hellking["extra_hp"] 
                            
                            hell_king.acquire_form(pegasus_suicide)
                            hell_king.acquire_form(retriever_chaotic)
                            hell_king.acquire_form(python_natural)
                            hell_king.acquire_form(elephant_violent)

                            hell_king.forms[0],hell_king.forms[-1] = hell_king.forms[-1],hell_king.forms[0]

                            for k in hell_king.forms:
                                if k['name'] != "NO FORM":
                                    k["hp"] = k["hp"] * round(k["hp_coef"] * k["level"]) + k["extra_hp"]
                                    k["current_hp"] = k["hp"]

                            battle(i,hell_king)

                            # print(pcs)
                            

                            if hell_king.form_0["current_hp"] < 1:
                                
                                print(f"{i.user_name} killed the HELL KING and became the new king of hell!")
                                input("")
                                ending()
                                return exit()

                    # print(winner)
                    if len(winner) > 0:
                        print(f"{i.user_name} killed the HELL KING and became the new king of hell!")
                        input("")
                        ending()
                        return exit()    
               
        else:
            print("No players! Game over!")
            exit()

    


def creating_players(mode):
    game_logo()

    how_many_players = 0
    if mode == 1:
        how_many_players = 1
    if mode in (2,3):
        if mode == 3:
            deathmatch.append("YES")
        warn_message = ""
        warning = "You have to set the number of players 1-8! Try again!"
        while True:
            game_logo()

            print(warn_message)
            players_count = input("HOW MANY USER PLAYERS? (1-8 or 'q' to quit) ")
            if players_count.isdigit():
                players_count = int(players_count)

                if players_count > 18 or players_count < 1:
                    warn_message = warning
                else:
                    how_many_players = players_count
                    break
            elif players_count.lower() == "q":
                return
    
    player_symbols = ["X","Y","Z","W","E","Q","O","G"]
    for _ in range(how_many_players):
        warn_message = ""
        warning = "Your name has to be max 18 characters long and cannot be empty!"
        while True:
            game_logo()
            print(warn_message)    
            name = input("CHOOSE YOUR NAME (max 18 characters or 'q' to quit): ")
            if len(name) > 18 or len(name) < 1:
                warn_message = warning
            elif name.lower() == "q":
                return
            else:
                break
        
        warn_message = ''
        warning = "You can choose only the symbol from the list!"
        # player_symbols = ["X","Y","Z","W","E","Q","O","G"]
        while True:
            (f"WELCOME {name}!\n")

            for i in player_symbols:
                print(i,end=", ")
            print("")

            print(warn_message)
            symbol = input("NOW CHOOSE YOUR SYMBOL ABOVE: ")

            if symbol.upper() not in player_symbols:
                warn_message = warning
            else:
                create_player(name,symbol.upper())
                player_symbols.remove(symbol.upper())
                            
                break
    
    
    return main_game_mode()
            





def main():
    start_warn_message = ''
    start_warning = "You have to choose only 1,2,3 or Q/q!"
    while True:
               
        game_logo()

        print(f"1) SINGLE PLAYER\n2) MULTIPLAYER\n3) DEATHMATCH\n\nQ) QUIT")
        print(f"""                                                        number of current forms: {round(len(lost_souls)/10):3d}""")
        print(start_warn_message)
        mode_choice = input("CHOOSE THE GAME MODE: ")

        if mode_choice.isdigit():
            mode_choice = int(mode_choice)
            if mode_choice < 4 and mode_choice > 0:
                if mode_choice in (1,2,3):
                    return creating_players(mode_choice)
            else:
                start_warn_message = start_warning
                
        elif mode_choice.lower() == "q":
            exit()
    
        else:
            start_warn_message = start_warning

def game_logo():
    os.system('cls')
    print(logo)
    print(line)


# def update_map(players):

#     for i in players:

#         if i.run == "YES":
#             re_back = i.where[0]
#             i.where[0] = i.backout
#             i.run = "NO"
#             if mapa[i.where[0]] == "|_|\n":
#                 mapa[i.where[0]] = f"{i.mark}|\n"
#                 i.backout = re_back
#             else:
#                 mapa[i.where[0]] = i.mark
#                 i.backout = re_back
        
#         else:
#             if mapa[i.where[0]] == "|_|\n":
#                 mapa[i.where[0]] = f"{i.mark}|\n"
#             else:              # HERE IS THE PROBLEM! DOESNT TAKE OTHER PLAYER MARKS! FIX IT!!!
#                 mapa[i.where[0]] = i.mark

        


def show_map(map):

    show_map = []
    for ky,vl in mapa.items():
        show_map.append(vl)

    return print(f"{' _'*30}\n{(''.join(show_map))}")


def clean():
    os.system('cls')

def ending():
    clean()
    print(end_logo)
    input("")
    clean()
    print("""
                          



                          dedicated to Vaclav the Retriever!

""")
input("")

end_logo = """
                          THANKS FOR PLAYING
 _______  _______           _          _______  _______ _________ _______  _______ 
(  ____ \(  ___  )|\     /|( \        (  ____ \(  ___  )\__   __/(  ____ \(  ____ )
| (    \/| (   ) || )   ( || (        | (    \/| (   ) |   ) (   | (    \/| (    )|
| (_____ | |   | || |   | || |        | (__    | (___) |   | |   | (__    | (____)|
(_____  )| |   | || |   | || |        |  __)   |  ___  |   | |   |  __)   |     __)
      ) || |   | || |   | || |        | (      | (   ) |   | |   | (      | (\ (   
/\____) || (___) || (___) || (____/\  | (____/\| )   ( |   | |   | (____/\| ) \ \__
\_______)(_______)(_______)(_______/  (_______/|/     \|   )_(   (_______/|/   \__/

                                                           created by the Ivos

"""



logo = """ 
               ___                                          
_|_ |_   _      |      _   _    ._  ._ _   _  _  ._ _|_  _ o
 |_ | | (/_    _|_ \/ (_) _>    |_) | (/_ _> (/_ | | |_ _> o
                                |                           
 _______  _______           _          _______  _______ _________ _______  _______ 
(  ____ \(  ___  )|\     /|( \        (  ____ \(  ___  )\__   __/(  ____ \(  ____ )
| (    \/| (   ) || )   ( || (        | (    \/| (   ) |   ) (   | (    \/| (    )|
| (_____ | |   | || |   | || |        | (__    | (___) |   | |   | (__    | (____)|
(_____  )| |   | || |   | || |        |  __)   |  ___  |   | |   |  __)   |     __)
      ) || |   | || |   | || |        | (      | (   ) |   | |   | (      | (\ (   
/\____) || (___) || (___) || (____/\  | (____/\| )   ( |   | |   | (____/\| ) \ \__
\_______)(_______)(_______)(_______/  (_______/|/     \|   )_(   (_______/|/   \__/

        """

line = "-"*49
borders = []

for i in range(1,31):
    borders.append(i*30)

# print(borders)

# player1 = ""
# player2 = ""
# player3 = ""
# player4 = ""
# player5 = ""
# player6 = ""
# player7 = ""
# player8 = ""

deathmatch = []
winner = []
created_players = []
# players = [player1, player2, player3, player4,
#                 player5, player6, player7, player8]
boss_fight = []
pcs = []
players = []
mapa = create_map()
create_item()

main()

# start_warn_message = ''
# start_warning = "You have to choose only 1,2,3 or Q/q!"
# while True:
    
#     print("SOUL DEVOURER")
#     print(line)

#     print(f"1) SINGLE PLAYER\n2) MULTIPLAYER\n3) DEATHMATCH\n\nQ) QUIT\n")
#     print(start_warn_message)
#     mode_choice = input("CHOOSE THE GAME MODE: ")

#     if mode_choice.isdigit():
#         mode_choice = int(mode_choice)
#         if mode_choice < 4:
#             break
#     elif mode_choice.lower() == "q":
#         exit()
#     else:
#         start_warn_message = start_warning






# player1 = Player("X","Ivos")

# player3 = Player("Z","Vaclav")


# for i in players:
#     i.remove_form()
#     i.acquire_form(no_form)
#     i.attack_list = i.forms[0]["attack_list"]
    
#     i.forms[0]["hp"] = no_form["hp"] * round(no_form["hp_coef"] * no_form["level"]) + no_form["extra_hp"]
#     i.forms[0]["current_hp"] = no_form["hp"] * round(no_form["hp_coef"] * no_form["level"]) + no_form["extra_hp"] 
  
    


# player1.acquire_form(polar_bear)


# player3.pc = "YES"
# player1.acquire_form(fox)



# for i in players:
#     if i.pc == "YES":        
#         pcs.append(i)        
#         players.remove(i)

# player3.acquire_form(polar_bear)
# player3.acquire_form(fox)

# for i in pcs:
#     i.forms[0],i.forms[-1] = i.forms[-1],i.forms[0]


# print("players",players)
# print("pcs",pcs)

# while True:
#     if len(players) > 0:
#         for i in players:        
#             print(f"{i.user_name}'s TURN!")
#             # print(f"{i.acquired}")
#             # input("")
#             i.player_turn()
#             # i.move()
#             # show_map(mapa)
#     else:
#         print("No players! Game over!")
#         exit()


















