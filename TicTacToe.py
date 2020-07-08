import os

def board(cnos):
    '''
    This is the layout of the TicTacToe board thats going to be visible to the user
    '''
    print("TIC TAC TOE ")
    
    print("      |      |      ")
    print("  {}   |  {}   |  {}  ".format(cnos[0],cnos[1],cnos[2]))
    print("      |      |      ")
    print("--------------------")
    print("      |      |      ")
    print("  {}   |  {}   |  {}  ".format(cnos[3],cnos[4],cnos[5]))
    print("      |      |      ")
    print("--------------------")
    print("      |      |      ")
    print("  {}   |  {}   |  {}  ".format(cnos[6],cnos[7],cnos[8]))
    print("      |      |      ")

def screen_clr():
    if os.name == 'posix':
        _ = os.system ('clear')
    else:
        _ = os.system('cls')

def again():
    play_again = input("Play again? - Enter YES/NO:  ")
    if play_again.upper() == "YES":
        mainfunc()
    else:
        print("Thank you for playing")

def wincheck():
    if (lst[0]=="X"and lst[1]=="X") and lst[2]=="X":
            print("User 1 Wins")
            again()
    elif (lst[3]=="X"and lst[4]=="X") and lst[5]=="X":
        print("User 1 Wins")
        again()
    elif (lst[6]=="X"and lst[7]=="X") and lst[8]=="X":
        print("User 1 Wins")
        again()
    elif (lst[0]=="X"and lst[3]=="X") and lst[6]=="X":
        print("User 1 Wins")
        again()
    elif (lst[1]=="X"and lst[4]=="X") and lst[7]=="X":
        print("User 1 Wins")
        again()
    elif (lst[2]=="X"and lst[5]=="X") and lst[8]=="X":
        print("User 1 Wins")
        again()
    elif (lst[0]=="X"and lst[4]=="X") and lst[8]=="X":
        print("User 1 Wins")
        again()
    elif (lst[2]=="X"and lst[4]=="X") and lst[6]=="X":
        print("User 1 Wins")
        again()
    elif (lst[0]=="O"and lst[1]=="O") and lst[2]=="O":
        print("User 2 Wins")
        again()
    elif (lst[3]=="O"and lst[4]=="O") and lst[5]=="O":
        print("User 2 Wins")
        again()
    elif (lst[6]=="O"and lst[7]=="O") and lst[8]=="O":
        print("User 2 Wins")
        again()
    elif (lst[0]=="O"and lst[3]=="O") and lst[6]=="O":
        print("User 2 Wins")
        again() 
    elif (lst[1]=="O"and lst[4]=="O") and lst[7]=="O":
        print("User 2 Wins")
        again()
    elif (lst[2]=="O"and lst[5]=="O") and lst[8]=="O":
        print("User 2 Wins")
        again()
    elif (lst[0]=="O"and lst[4]=="O") and lst[8]=="O":
        print("User 2 Wins")
        again()
    elif (lst[2]=="O"and lst[4]=="O") and lst[6]=="O":
        print("User 2 Wins")
        again()

def choicefunc():
    global lst
    lst=[" "," "," "," "," "," "," "," "," "]
    for i in range(1,10):
        if i % 2 == 1:
            cho=int(input("Enter your Choice User 1: "))
            screen_clr()
            lst[cho-1] = "X"
            board(lst)
            wincheck()
        else:
            cho=int(input("Enter your Choice User 2: "))
            screen_clr()
            lst[cho-1] = "O"
            board(lst)
            wincheck()
        
def mainfunc():
    board([" "," "," "," "," "," "," "," "," "])
    choicefunc()
    again()
mainfunc()
        



