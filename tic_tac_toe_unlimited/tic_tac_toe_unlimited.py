# IMPORT LIBRARIES

import os

# FUN FOR START GAME

def main():
     
     # SETTING UP THE DIMENSIONS OF THE BOARD
     
     diagonal = input(f"Choose the horizontal length of the board, please (min {rule} / max 26): ")
     
     while not diagonal.isdigit() or int(diagonal) < rule or int(diagonal) > 26:
               diagonal = input(f"Length has to be a number between {rule}-26.\nTry again, please: ")
     diagonal = int(diagonal)
   
     vertical = input(f"Now choose the vertical length of the board, please (min {rule} / max 26): ")

     while not vertical.isdigit() or int(vertical) < rule or int(vertical) > 26:
               vertical = input(f"Length has to be a number between {rule}-26.\nTry again, please: ")
     vertical = int(vertical)
          
     return create_board(int(diagonal),int(vertical))


# FUN FOR CREATING BOARD

def create_board(diagonal,vertical):
     
     # CREATING THE BOARD ACCORDING TO THE INPUT VALUES
          
     for i in range(1,((diagonal*vertical)+vertical)+1):

          board[i]= "|_"

     # SETTING UP THE LAST LINES OF EACH ROW 

     for i in range(1,len(board)+1):
          if i % (diagonal+1) == 0:
               board[i] = f"|\n"

     # CREATING THE TABLE OF STARTING LINES OF EACH ROW

     ylines = []

     for i in range(0,len(board)):
          if board[i] == "|\n":
               ylines.append(i)

     # 'ENUMARATING' EACH ROW

     l = 0

     for i in range(0,len(board)-diagonal):
          if board[i] == "|\n" or board[i] == "\n":
               l +=1
               board[i+1] = (f"{l:2d}|_")

     # CREATING THE HEADER COORDINATES 

     alphabet = "abcdefghijklmnopqrstuvwxyz "

     header = []

     for i in range(0,diagonal):
          header.append(alphabet[i].upper())

     # UNDERLINING THE HEADER VALUES FOR BETTER 'DESIGN ILLUSION'

     header = "\u0332 ".join(header + list(" "))
     board[0] = f"   {header}\n"

     # STARTING THE FIRST BLOW FOR PLAYER X 

     os.system("cls")

     return mark_x(diagonal,vertical)


# MARKING FUN FOR PLAYER X

def mark_x(diagonal,vertical):
 
     os.system("cls")

     # PRINT BOARD

     print("".join(map(str,list(board.values()))))

     # PLAYER INPUT

     coordinates = input(f"Player {player_x} (X), choose your coordinates (or 'quit' for quit): ")
     if coordinates.lower() == "quit":
           return
     
     # HEADER MARKERS LIST

     alphabet = "abcdefghijklmnopqrstuvwxyz "

     # CONVERTING COORDINATES

     num = ""
     alpha = ""
     digits = ""
     alphasis = ""


     for i in coordinates:
          
          if i.isdigit():
               digits += i
               num = int(digits)
               
          if len(i) == 1 and i.isalpha():
               alphasis +=i
               alpha = i

          if digits == "":
                num = 0

     # CYCLE FOR WRONG INPUT

     while len(alphasis) != 1 or (alphabet.index(alpha.lower())+1) > diagonal or num > vertical or num < 1 or (alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))) in occupied:
           print("NOT POSSIBLE! (Place is already occupied or out of board)\nTry again, please.")
           input("\nPress any key to continue...")
           return mark_x(diagonal,vertical)

     # ASSIGNING EXCEPTION FOR 1ST COLUMNS
     # ALSO INSERTING THE POSITION INTO THE OCCUPIED COLUMNS LIST    

     if alpha.lower() == "a":
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"{num:2d}|X"))
          occupied_x.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
     
     # ASSIGNING SYMBOLS FOR OTHER COLUMNS
     # ALSO INSERTING THE POSITION INTO THE OCCUPIED COLUMNS LIST
     
     else:
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"|X"))
          occupied_x.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
    
     # PRINT UPDATED BOARD
     
     print("".join(map(str,list(board.values()))))

     # SETTING UP THE CORRDINATE VALUE

     coor_x = alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))

     # LAUNCHING THE POSSIBLE WIN CHECK     

     return check_mark_x(coor_x,diagonal,vertical)


# MARKING FUN FOR PLAYER O

def mark_o(diagonal,vertical):

     os.system("cls")

     # PRINT BOARD

     print("".join(map(str,list(board.values()))))

     # PLAYER INPUT

     coordinates = input(f"Player {player_o} (O), choose your coordinates (or 'quit' for quit): ")
     if coordinates.lower() == "quit":
           return
     
     # HEADER MARKERS LIST

     alphabet = "abcdefghijklmnopqrstuvwxyz "

     # CONVERTING COORDINATES

     num = ""
     alpha = ""
     digits = ""
     alphasis = ""


     for i in coordinates:
          
          if i.isdigit():
               digits += i
               num = int(digits)
               
          if len(i) == 1 and i.isalpha():
               alphasis +=i
               alpha = i

          if digits == "":
                num = 0

     # CYCLE FOR WRONG INPUT

     while len(alphasis) != 1 or (alphabet.index(alpha.lower())+1) > diagonal or num > vertical or num < 1 or (alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))) in occupied:
           print("NOT POSSIBLE! (Place is already occupied or out of board)\nTry again, please.")
           input("\nPress any key to continue...")
           return mark_o(diagonal,vertical)

     # ASSIGNING EXCEPTION FOR 1ST COLUMNS
     # ALSO INSERTING THE POSITION INTO THE OCCUPIED COLUMNS LIST

     if alpha.lower() == "a":
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"{num:2d}|O"))
          occupied_o.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
     
     # ASSIGNING SYMBOLS FOR OTHER COLUMNS
     # ALSO INSERTING THE POSITION INTO THE OCCUPIED COLUMNS LIST

     else:
          board[alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))] = "\u0332".join(list(f"|O"))
          occupied_o.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
          occupied.append(alphabet.index(alpha.lower()) + (num+(diagonal*(num-1))))
    
     # PRINT UPDATED BOARD

     print("".join(map(str,list(board.values()))))

     # SETTING UP THE CORRDINATE VALUE

     coor_o = alphabet.index(alpha.lower()) + (num+(diagonal*(num-1)))

     # LAUNCHING THE POSSIBLE WIN CHECK
     
     return check_mark_o(coor_o,diagonal,vertical)


# CHECK FUN FOR POSSIBLE WIN OF PLAYER O

def check_mark_x(coor_x,diagonal,vertical):
      os.system("cls")

      # CREATING LINES TO BE CHECKED

      diag_1 = []
      diag_2 = []

      diag_r1 = []
      diag_r2 = []

      diag_u1 = []
      diag_u2 = []

      diag_s1 = []
      diag_s2 = []

      # LEFT AND RIGHT DIRECTION LINES

      diag_s1 = list(board.items())[coor_x:0:-1] 
      diag_s2 = list(board.items())[coor_x:(list(board.keys())[-1]):1]

      # UP AND DOWN DIRECTION LINES

      diag_u1 = list(board.items())[coor_x::((diagonal+1)*(-1))] 
      diag_u2 = list(board.items())[coor_x:(list(board.keys())[-1]):(diagonal+1)]

      # R DIAGONAL DIRECTION LINES

      diag_r1 = list(board.items())[coor_x::((diagonal)*(-1))] 
      diag_r2 = list(board.items())[coor_x:(list(board.keys())[-1]):(diagonal)]

      # L DIAGONAL DIRECTION LINES

      diag_1 = list(board.items())[coor_x::((diagonal+2)*(-1))] 
      diag_2 = list(board.items())[coor_x:(list(board.keys())[-1]):(diagonal+2)]

      # LINES TO BE JOINED AND SORTED IN ORDER

      diag = list(set(diag_1).union(set(diag_2)))
      diag.sort()

      diagr = list(set(diag_r1).union(set(diag_r2)))
      diagr.sort()

      diagu = list(set(diag_u1).union(set(diag_u2)))
      diagu.sort()

      diags = list(set(diag_s1).union(set(diag_s2)))
      diags.sort()

      # ADDING THE SYMBOLS ACCORDING TO THE REAL SEQUENCES

      xline = []
      xliner = []
      xlineu = []
      xlines = []

      for i in diag:
            if "X" in i[1]:
                  xline.append("X")
            else:
                  xline.append("nope")

      for i in diagr:
            if "X" in i[1]:
                  xliner.append("X")
            else:
                  xliner.append("nope")

      for i in diagu:
            if "X" in i[1]:
                  xlineu.append("X")
            else:
                  xlineu.append("nope")

      for i in diags:
            if "X" in i[1]:
                  xlines.append("X")
            else:
                  xlines.append("nope")

      # AFTER ADDING THE SYMBOLS INTO THE CHECK LISTS JOIN THEM INTO THE STRING FOR BETTER OVERVIEW

      xline_check = "".join(xline)
      xliner_check = "".join(xliner)
      xlineu_check = "".join(xlineu)
      xlines_check = "".join(xlines)

      # CHECK POSSIBLE WINS

      if "X"*rule in xline_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif "X"*rule in xliner_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif "X"*rule in xlineu_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      elif "X"*rule in xlines_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_x} (X) have won!")
      
      # CHECK POSSIBLE DRAW

      elif len(occupied) == (diagonal*vertical):
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print("It's a draw!")
      
      # IF NO DRAW OR WIN - CONTINUE

      else:
            
            return mark_o(diagonal,vertical)


# CHECK FUN FOR POSSIBLE WIN OF PLAYER O

def check_mark_o(coor_o,diagonal,vertical):
      os.system("cls")

      # CREATING LINES TO BE CHECKED

      diag_1 = []
      diag_2 = []

      diag_r1 = []
      diag_r2 = []

      diag_u1 = []
      diag_u2 = []

      diag_s1 = []
      diag_s2 = []

      # LEFT AND RIGHT DIRECTION LINES

      diag_s1 = list(board.items())[coor_o:0:-1] 
      diag_s2 = list(board.items())[coor_o:(list(board.keys())[-1]):1]

      # UP AND DOWN DIRECTION LINES

      diag_u1 = list(board.items())[coor_o::((diagonal+1)*(-1))] 
      diag_u2 = list(board.items())[coor_o:(list(board.keys())[-1]):(diagonal+1)]

      # R DIAGONAL DIRECTION LINES

      diag_r1 = list(board.items())[coor_o::((diagonal)*(-1))] 
      diag_r2 = list(board.items())[coor_o:(list(board.keys())[-1]):(diagonal)]

      # L DIAGONAL DIRECTION LINES

      diag_1 = list(board.items())[coor_o::((diagonal+2)*(-1))] 
      diag_2 = list(board.items())[coor_o:(list(board.keys())[-1]):(diagonal+2)]

      # LINES TO BE JOINED AND SORTED IN ORDER

      diag = list(set(diag_1).union(set(diag_2)))
      diag.sort()

      diagr = list(set(diag_r1).union(set(diag_r2)))
      diagr.sort()

      diagu = list(set(diag_u1).union(set(diag_u2)))
      diagu.sort()

      diags = list(set(diag_s1).union(set(diag_s2)))
      diags.sort()

      # ADDING THE SYMBOLS ACCORDING TO THE REAL SEQUENCES

      oline = []
      oliner = []
      olineu = []
      olines = []

      for i in diag:
            if "O" in i[1]:
                  oline.append("O")
            else:
                  oline.append("nope")

      for i in diagr:
            if "O" in i[1]:
                  oliner.append("O")
            else:
                  oliner.append("nope")

      for i in diagu:
            if "O" in i[1]:
                  olineu.append("O")
            else:
                  olineu.append("nope")

      for i in diags:
            if "O" in i[1]:
                  olines.append("O")
            else:
                  olines.append("nope")

      # AFTER ADDING THE SYMBOLS INTO THE CHECK LISTS JOIN THEM INTO THE STRING FOR BETTER OVERVIEW

      oline_check = "".join(oline)
      oliner_check = "".join(oliner)
      olineu_check = "".join(olineu)
      olines_check = "".join(olines)

      # CHECK POSSIBLE WINS
     
      if "O"*rule in oline_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif "O"*rule in oliner_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif "O"*rule in olineu_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      elif "O"*rule in olines_check:
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print(f"Player {player_o} (O) have won!")
      
      # CHECK POSSIBLE DRAW

      elif len(occupied) == (diagonal*vertical):
            os.system("cls")
            print("".join(map(str,list(board.values()))))
            return print("It's a draw!")
      
      # IF NO DRAW OR WIN - CONTINUE

      else:
            
            return mark_x(diagonal,vertical)
      
      
# MAIN PROGRAM START
           
os.system("cls")

# SET THE GAME CONTROL VARIABLES

board = {0:f"\n"}
occupied = []
occupied_x = []
occupied_o = []

# WELCOME MESSAGE

print("Welcome to the game of PISKVORKY UNLIMITED!\n")

# SET THE PLAYER NAMES

player_x = input("Choose name for player X: ")
player_o = input("Choose name for player O: ")

# SET THE WINNING RULE

rule = ""

while not rule.isdigit():
      rule = input("Please set the number of symbols which has to be in line to win the game: (min 3, max 9): ")

rule = int(rule)

while rule < 3 or rule > 9:
      rule = input("The number has to be between 3 and 9: ")
      while not rule.isdigit():
            rule = input("The number has to be between 3 and 9: ")
      rule = int(rule)

# LAUNCH THE GAME

main()









