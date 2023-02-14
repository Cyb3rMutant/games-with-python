import random
import os
import time
grid2="nothing"
grid={1:["","","",""],
      2:["","","",""],
      3:["","","",""],
      4:["","","",""],}
moves=["w","a","s","d"]
def board():    
    return print("""
---------------------
|%s|%s|%s|%s|
---------------------
|%s|%s|%s|%s|
---------------------
|%s|%s|%s|%s|
---------------------
|%s|%s|%s|%s|
---------------------
"""%(grid[1][0].center(4," "),grid[1][1].center(4," "),grid[1][2].center(4," "),grid[1][3].center(4," "),
     grid[2][0].center(4," "),grid[2][1].center(4," "),grid[2][2].center(4," "),grid[2][3].center(4," "),
     grid[3][0].center(4," "),grid[3][1].center(4," "),grid[3][2].center(4," "),grid[3][3].center(4," "),
     grid[4][0].center(4," "),grid[4][1].center(4," "),grid[4][2].center(4," "),grid[4][3].center(4," ")
    ))

def right():
    temp1=0
    temp2=0
    temp3=0
    for r in range(1,5): #r is raw
        temp1=0
        temp2=0
        temp3=0
        for c in range(3,-1,-1): #c is column
            if (c==3) and (grid[r][c]!=""):
                continue
            elif grid[r][c]!="":
                for b in range(c+1,4):
                    if grid[r][b]==grid[r][c]:
                        if c==2:
                            temp3=1
                            grid[r][c],grid[r][b]="",str(int(grid[r][c])*2)
                            temp2,grid[r][b]=grid[r][b],"1"
                            temp1=b
                        else:
                            grid[r][c],grid[r][b]="",str(int(grid[r][c])*2)
                        break
                    elif grid[r][b]!="":
                        break
                    elif grid[r][b]=="":
                        grid[r][c],grid[r][b]=grid[r][b],grid[r][c]
                        c+=1
        if temp3==1:
            grid[r][temp1]=temp2
                        
                        

def left():
    temp1=0
    temp2=0
    temp3=0
    for r in range(1,5): #r is raw
        temp1=0
        temp2=0
        temp3=0
        for c in range(0,4): #c is column
            if (c==0) and (grid[r][c]!=""):
                continue
            elif grid[r][c]!="":
                for b in range(c-1,-1,-1):
                    if grid[r][b]==grid[r][c]:
                        if c==1:
                            temp3=1
                            grid[r][c],grid[r][b]="",str(int(grid[r][c])*2)
                            temp2,grid[r][b]=grid[r][b],"1"
                            temp1=b
                        else:
                            grid[r][c],grid[r][b]="",str(int(grid[r][c])*2)
                        break
                    elif grid[r][b]!="":
                        break
                    elif grid[r][b]=="":
                        grid[r][c],grid[r][b]=grid[r][b],grid[r][c]
                        c-=1
        if temp3==1:
            grid[r][temp1]=temp2
                
def up():
    temp1=0
    temp2=0
    temp3=0
    for c in range(0,4):
        temp1=0
        temp2=0
        temp3=0
        for r in range(1,5):
            if (r==1) and (grid[r][c]!=""):
                continue
            elif grid[r][c]!="":
                for b in range(r-1,0,-1):
                    if grid[b][c]==grid[r][c]:
                        if r==2:
                            temp3=1
                            grid[r][c],grid[b][c]="",str(int(grid[r][c])*2)
                            temp2,grid[b][c]=grid[b][c],"1"
                            temp1=b
                        else:
                            grid[r][c],grid[b][c]="",str(int(grid[r][c])*2)
                        break
                    elif grid[b][c]!="":
                        break
                    elif grid[b][c]=="":
                        grid[r][c],grid[b][c]=grid[b][c],grid[r][c]
                        r-=1
        if temp3==1:
            grid[temp1][c]=temp2

def down():
    temp1=0
    temp2=0
    temp3=0
    for c in range(0,4):
        temp1=0
        temp2=0
        temp3=0
        for r in range(4,0,-1):
            if (r==4) and (grid[r][c]!=""):
                continue
            elif grid[r][c]!="":
                for b in range(r+1,5):
                    if grid[b][c]==grid[r][c]:
                        if r==3:
                            temp3=1
                            grid[r][c],grid[b][c]="",str(int(grid[r][c])*2)
                            temp2,grid[b][c]=grid[b][c],"1"
                            temp1=b
                        else:
                            grid[r][c],grid[b][c]="",str(int(grid[r][c])*2)
                        break
                    elif grid[b][c]!="":
                        break
                    elif grid[b][c]=="":
                        grid[r][c],grid[b][c]=grid[b][c],grid[r][c]
                        r+=1
        if temp3==1:
            grid[temp1][c]=temp2

def losecheck():
    for r in range(1,5):
        for c in range(0,3):
            if grid[r][c]==grid[r][c+1]:
                return False
    for c in range(0,4):
        for r in range(1,4):
            if grid[r][c]==grid[r+1][c]:
                return False
    return True
            
            
            
def play():
    global grid, grid2
    grid2={1:grid[1][:],2:grid[2][:],3:grid[3][:],4:grid[4][:]}
    while grid==grid2:
        os.system("cls")
        board()
        #grid={1:grid2[1][:],2:grid2[2][:],3:grid2[3][:],4:grid2[4][:]}
        x=input()
        #os.system("cls")
        while x not in moves:
            x=input()
        if x=="w":
            up()
        elif x=="a":
            left()
        elif x=="s":
            down()
        elif x=="d":
            right()
        
        
        
lost=False
while "2048" not in grid[1] and "2048" not in grid[2] and "2048" not in grid[3] and "2048" not in grid[4] and lost==False:
    if ("" in grid[1] or "" in grid[2] or "" in grid[3] or "" in grid[4]):
        r,c=random.randint(1,4),random.randint(0,3)
        while grid[r][c]!="":
            r,c=random.randint(1,4),random.randint(0,3)
        grid[r][c]="2"
    if ("" not in grid[1] and "" not in grid[2] and "" not in grid[3] and "" not in grid[4]):
        lost=True
        lost=losecheck()
        if lost==True:
            break
    #board()
    play()
if lost==False:
    os.system("cls")
    board()
    print("congrats boi")
elif lost==True:
    os.system("cls")
    board()
    print("haha loser")
time.sleep(5)
