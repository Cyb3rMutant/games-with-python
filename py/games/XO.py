import os
playagain="yes"
blocks={"b1":1, "b2":2, "b3":3, "b4":4, "b5":5, "b6":6, "b7":7, "b8":8,"b9":9}
player=["X","O"]
ub=[]
n=0
def board():
    return print("""
 %s | %s | %s 
---+---+---
 %s | %s | %s 
---+---+---
 %s | %s | %s 
    """ %(blocks["b1"],blocks["b2"],blocks["b3"],blocks["b4"],blocks["b5"],blocks["b6"],blocks["b7"],blocks["b8"],blocks["b9"],))

def x(bnx):
    while bnx in ub:
            print("this block has been already used")
            bnx=int(input("please enter another block number: "))
    if bnx==1:
        blocks["b1"]="X"
    elif bnx==2:
        blocks["b2"]="X"
    elif bnx==3:
        blocks["b3"]="X"
    elif bnx==4:
        blocks["b4"]="X"
    elif bnx==5:
        blocks["b5"]="X"
    elif bnx==6:
        blocks["b6"]="X"
    elif bnx==7:
        blocks["b7"]="X"
    elif bnx==8:
        blocks["b8"]="X"
    elif bnx==9:
        blocks["b9"]="X"
    


def o(bno):
    while bno in ub:
        print("this block has been already used")
        bno=int(input("please enter another block number: "))
    
    if bno==1:
        blocks["b1"]="O"
    elif bno==2:
        blocks["b2"]="O"
    elif bno==3:
        blocks["b3"]="O"
    elif bno==4:
        blocks["b4"]="O"
    elif bno==5:
        blocks["b5"]="O"
    elif bno==6:
        blocks["b6"]="O"
    elif bno==7:
        blocks["b7"]="O"
    elif bno==8:
        blocks["b8"]="O"
    elif bno==9:
        blocks["b9"]="O"
while playagain=="yes":
    os.system("cls")
    blocks={"b1":1, "b2":2, "b3":3, "b4":4, "b5":5, "b6":6, "b7":7, "b8":8,"b9":9}
    player=["malek","yazeed"]
    ub=[]
    n=0
    board()
    for r in range(1,6):
        print("ROUND "+str(r)+":")
        for p in player:
            if p=="malek":
                print("player "+p)
                n=input("please enter a block number: ")
                while (n!="1" and n!="2" and n!="3" and n!="4" and n!="5" and n!="6" and n!="7" and n!="8" and n!="9") or int(n) in ub:
                    if n!="1" and n!="2" and n!="3" and n!="4" and n!="5" and n!="6" and n!="7" and n!="8" and n!="9":
                        print("this block is invalid")
                        n=input("please enter another block number: ")
                    else:
                        print("this block has been already used")
                        n=input("please enter another block number: ")
                n=int(n)
                x(n)
            else:
                print("player "+p)
                n=input("please enter a block number: ")
                while (n!="1" and n!="2" and n!="3" and n!="4" and n!="5" and n!="6" and n!="7" and n!="8" and n!="9") or int(n) in ub:
                    if n!="1" and n!="2" and n!="3" and n!="4" and n!="5" and n!="6" and n!="7" and n!="8" and n!="9":
                        print("this block is invalid")
                        n=input("please enter another block number: ")
                    else:
                        print("this block has been already used")
                        n=input("please enter another block number: ")
                n=int(n)
                o(n)
            ub.append(n)
            os.system("cls")
            board()
            if (blocks["b1"]==blocks["b2"]==blocks["b3"]) or (blocks["b4"]==blocks["b5"]==blocks["b6"]) or (blocks["b7"]==blocks["b8"]==blocks["b9"]) or (blocks["b1"]==blocks["b4"]==blocks["b7"]) or (blocks["b2"]==blocks["b5"]==blocks["b8"]) or (blocks["b3"]==blocks["b6"]==blocks["b9"]) or (blocks["b1"]==blocks["b5"]==blocks["b9"]) or (blocks["b3"]==blocks["b5"]==blocks["b7"]):
                print(p+" WINS")
                break
            if r==5:
                print("TIE")
                break
        if (blocks["b1"]==blocks["b2"]==blocks["b3"]) or (blocks["b4"]==blocks["b5"]==blocks["b6"]) or (blocks["b7"]==blocks["b8"]==blocks["b9"]) or (blocks["b1"]==blocks["b4"]==blocks["b7"]) or (blocks["b2"]==blocks["b5"]==blocks["b8"]) or (blocks["b3"]==blocks["b6"]==blocks["b9"]) or (blocks["b1"]==blocks["b5"]==blocks["b9"]) or (blocks["b3"]==blocks["b5"]==blocks["b7"]):
            break
        if r==5:
            break
    playagain=input("playagain: ")
