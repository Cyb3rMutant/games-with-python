import random,time,os
grid={0:["","","","","","","","",""]
     ,1:["","","","","","","","",""]
     ,2:["","","","","","","","",""]
     ,3:["","","","","","","","",""]
     ,4:["","","","","","","","",""]
     ,5:["","","","","","","","",""]
     ,6:["","","","","","","","",""]
     ,7:["","","","","","","","",""]
     ,8:["","","","","","","","",""]}
grid2={0: ['0 0', '0 1', '0 2', '0 3', '0 4', '0 5', '0 6', '0 7', '0 8']
      ,1: ['1 0', '1 1', '1 2', '1 3', '1 4', '1 5', '1 6', '1 7', '1 8']
      ,2: ['2 0', '2 1', '2 2', '2 3', '2 4', '2 5', '2 6', '2 7', '2 8']
      ,3: ['3 0', '3 1', '3 2', '3 3', '3 4', '3 5', '3 6', '3 7', '3 8']
      ,4: ['4 0', '4 1', '4 2', '4 3', '4 4', '4 5', '4 6', '4 7', '4 8']
      ,5: ['5 0', '5 1', '5 2', '5 3', '5 4', '5 5', '5 6', '5 7', '5 8']
      ,6: ['6 0', '6 1', '6 2', '6 3', '6 4', '6 5', '6 6', '6 7', '6 8']
      ,7: ['7 0', '7 1', '7 2', '7 3', '7 4', '7 5', '7 6', '7 7', '7 8']       
      ,8: ['8 0', '8 1', '8 2', '8 3', '8 4', '8 5', '8 6', '8 7', '8 8']}
def board2():
    return print("""
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    |%s|%s|%s|%s|%s|%s|%s|%s|%s|
    -------------------------------------------------------
    """%(grid2[0][0].center(5," "),grid2[0][1].center(5," "),grid2[0][2].center(5," "),grid2[0][3].center(5," "),grid2[0][4].center(5," "),grid2[0][5].center(5," "),grid2[0][6].center(5," "),grid2[0][7].center(5," "),grid2[0][8].center(5," ")
        ,grid2[1][0].center(5," "),grid2[1][1].center(5," "),grid2[1][2].center(5," "),grid2[1][3].center(5," "),grid2[1][4].center(5," "),grid2[1][5].center(5," "),grid2[1][6].center(5," "),grid2[1][7].center(5," "),grid2[1][8].center(5," ")
        ,grid2[2][0].center(5," "),grid2[2][1].center(5," "),grid2[2][2].center(5," "),grid2[2][3].center(5," "),grid2[2][4].center(5," "),grid2[2][5].center(5," "),grid2[2][6].center(5," "),grid2[2][7].center(5," "),grid2[2][8].center(5," ")
        ,grid2[3][0].center(5," "),grid2[3][1].center(5," "),grid2[3][2].center(5," "),grid2[3][3].center(5," "),grid2[3][4].center(5," "),grid2[3][5].center(5," "),grid2[3][6].center(5," "),grid2[3][7].center(5," "),grid2[3][8].center(5," ")
        ,grid2[4][0].center(5," "),grid2[4][1].center(5," "),grid2[4][2].center(5," "),grid2[4][3].center(5," "),grid2[4][4].center(5," "),grid2[4][5].center(5," "),grid2[4][6].center(5," "),grid2[4][7].center(5," "),grid2[4][8].center(5," ")
        ,grid2[5][0].center(5," "),grid2[5][1].center(5," "),grid2[5][2].center(5," "),grid2[5][3].center(5," "),grid2[5][4].center(5," "),grid2[5][5].center(5," "),grid2[5][6].center(5," "),grid2[5][7].center(5," "),grid2[5][8].center(5," ")
        ,grid2[6][0].center(5," "),grid2[6][1].center(5," "),grid2[6][2].center(5," "),grid2[6][3].center(5," "),grid2[6][4].center(5," "),grid2[6][5].center(5," "),grid2[6][6].center(5," "),grid2[6][7].center(5," "),grid2[6][8].center(5," ")
        ,grid2[7][0].center(5," "),grid2[7][1].center(5," "),grid2[7][2].center(5," "),grid2[7][3].center(5," "),grid2[7][4].center(5," "),grid2[7][5].center(5," "),grid2[7][6].center(5," "),grid2[7][7].center(5," "),grid2[7][8].center(5," ")
        ,grid2[8][0].center(5," "),grid2[8][1].center(5," "),grid2[8][2].center(5," "),grid2[8][3].center(5," "),grid2[8][4].center(5," "),grid2[8][5].center(5," "),grid2[8][6].center(5," "),grid2[8][7].center(5," "),grid2[8][8].center(5," ")))

for b in range(9):
    a=random.randint(0,8)
    c=random.randint(0,8)
    while grid[a][c]=="X":
        a=random.randint(0,8)
        c=random.randint(0,8)
    grid[a][c]="X" 

for y in range(0,9):
    for x in range(0,9):
        if grid[y][x]!="X":
            grid[y][x]="0"
            for j in range(y-1,y+2):
                for k in range(x-1,x+2):
                    try:
                        if (grid[j][k]=="X") and (j!=-1) and (k!=-1):
                            grid[y][x]=str(int(grid[y][x])+1)
                    except KeyError:
                        continue
                    except IndexError:
                        continue
            if grid[y][x]=="0":
                grid[y][x]=""
grid2fortest=grid2[0]+grid2[1]+grid2[2]+grid2[3]+grid2[4]+grid2[5]+grid2[6]+grid2[7]+grid2[8]
gridfortest=grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+grid[5]+grid[6]+grid[7]+grid[8]
def grow(y,x):
    global grid,grid2
    if grid[y][x].isdigit()==False:
        grid2[y][x]=grid[y][x]
        try:
            if ((grid[y][x+1]=="") or (grid[y][x+1].isdigit()==True)) and ((grid2[y][x+1]!="") or ((grid2[y][x+1].isdigit()==False) and (len(grid2[y][x+1])==1))):
                grow(y,x+1)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if ((grid[y+1][x]=="") or (grid[y+1][x].isdigit()==True)) and ((grid2[y+1][x]!="") or ((grid2[y+1][x].isdigit()==False) and (len(grid2[y+1][x])==1))):
                grow(y+1,x)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (((grid[y][x-1]=="") and (x-1)!=-1) or (grid[y][x-1].isdigit()==True)) and ((grid2[y][x-1]!="") or ((grid2[y][x-1].isdigit()==False) and (len(grid2[y][x-1])==1))):
                grow(y,x-1)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if ((grid[y-1][x]=="") or (grid[y-1][x].isdigit()==True)) and ((grid2[y-1][x]!="") or ((grid2[y-1][x].isdigit()==False) and (len(grid2[y-1][x])==1))):
                grow(y-1,x)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if grid[y+1][x+1].isdigit()==True:
                grid2[y+1][x+1]=grid[y+1][x+1]
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (grid[y+1][x-1].isdigit()==True) and (x-1)!=-1:
                grid2[y+1][x-1]=grid[y+1][x-1]
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if grid[y-1][x+1].isdigit()==True:
                grid2[y-1][x+1]=grid[y-1][x+1]
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (grid[y-1][x-1].isdigit()==True) and (x-1)!=-1:
                grid2[y-1][x-1]=grid[y-1][x-1]
        except KeyError:
            pass
        except IndexError:
            pass
    elif x!=-1:grid2[y][x]=grid[y][x]
board2()
while "X" not in grid2fortest:
    player=input()
    q=int(player.split()[0])
    w=int(player.split()[1])
    if len(player.split())==3:
        grid2[q][w]=player.split()[2]
    else:
        grid2[q][w]=grid[q][w]
    if grid2[q][w]=="":
        try:
            if (grid[q][w+1]=="") or (grid[q][w+1].isdigit()==True):
                grow(q,w+1)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (grid[q+1][w]=="") or (grid[q+1][w].isdigit()==True):
                grow(q+1,w)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if ((grid[q][w-1]=="") and ((w-1)!=-1)) or (grid[q][w-1].isdigit()==True):
                grow(q,w-1)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (grid[q-1][w]=="") or (grid[q-1][w].isdigit()==True):
                grow(q-1,w)
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if grid[q+1][w+1].isdigit()==True:
                grid2[q+1][w+1]=grid[q+1][w+1]
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (grid[q+1][w-1].isdigit()==True) and (w-1)!=-1:
                grid2[q+1][w-1]=grid[q+1][w-1]
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if grid[q-1][w+1].isdigit()==True:
                grid2[q-1][w+1]=grid[q-1][w+1]
        except KeyError:
            pass
        except IndexError:
            pass
        try:
            if (grid[q-1][w-1].isdigit()==True) and (w-1)!=-1:
                grid2[q-1][w-1]=grid[q-1][w-1]
        except KeyError:
            pass
        except IndexError:
            pass
    elif (grid2[q][w].isdigit==True) and len(grid2[q][w])==1:
        continue
    os.system("cls")
    board2()
    grid2fortest=grid2[0]+grid2[1]+grid2[2]+grid2[3]+grid2[4]+grid2[5]+grid2[6]+grid2[7]+grid2[8]
    if gridfortest.count("")==grid2fortest.count("") and gridfortest.count("1")==grid2fortest.count("1") and gridfortest.count("2")==grid2fortest.count("2") and gridfortest.count("3")==grid2fortest.count("3") and gridfortest.count("4")==grid2fortest.count("4") and gridfortest.count("5")==grid2fortest.count("5") and gridfortest.count("6")==grid2fortest.count("6") and gridfortest.count("7")==grid2fortest.count("7") and gridfortest.count("8")==grid2fortest.count("8") and gridfortest.count("9")==grid2fortest.count("9"):
        print("congrats")
        break
    if gridfortest.count("X")==grid2fortest.count("P"):
        for i in range(len(grid2fortest)):
            if gridfortest[i]=="X":
                if grid2fortest[i]!="P":
                    break
        else:
            print("congrats")
            break
time.sleep(20)
