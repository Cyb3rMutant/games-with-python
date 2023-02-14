import time
import os

cells=["1","2","3","4","5","6","7"]

player=["mahmmoud","yazeed"]
column=0


grid2={1:[0,1,2,3,4,5],
      2:[0,1,2,3,4,5],
      3:[0,1,2,3,4,5],
      4:[0,1,2,3,4,5],
      5:[0,1,2,3,4,5],
      6:[0,1,2,3,4,5],
      7:[0,1,2,3,4,5]}



grid={1:[" "," "," "," "," "," "],
      2:[" "," "," "," "," "," "],
      3:[" "," "," "," "," "," "],
      4:[" "," "," "," "," "," "],
      5:[" "," "," "," "," "," "],
      6:[" "," "," "," "," "," "],
      7:[" "," "," "," "," "," "],}



def play():
    column=input("player %s, please choose a column: "%(player[p]))
    while (column not in cells) or (len(grid2[int(column)])==0):
        os.system("cls")
        board()
        column=input("player %s, please choose a column: "%(player[p]))
        
    column=int(column)
    for cell in grid2[column]:
        os.system("cls")
        grid[column][cell],prev=player[p][0].upper(),grid[column][cell]
        board()
        time.sleep(.1)
        if cell==grid2[column][-1]:
            break
        grid[column][cell]=prev
    del grid2[column][-1]

    
    
    
    
    
    
    
#time.sleep(10)
def board():    
    return print("""
-----------------------------
| %s | %s | %s | %s | %s | %s | %s |
-----------------------------
| %s | %s | %s | %s | %s | %s | %s |
-----------------------------
| %s | %s | %s | %s | %s | %s | %s |
-----------------------------
| %s | %s | %s | %s | %s | %s | %s |
-----------------------------
| %s | %s | %s | %s | %s | %s | %s |
-----------------------------
| %s | %s | %s | %s | %s | %s | %s |
-----------------------------
  1   2   3   4   5   6   7  
"""%(grid[1][0],grid[2][0],grid[3][0],grid[4][0],grid[5][0],grid[6][0],grid[7][0],
     grid[1][1],grid[2][1],grid[3][1],grid[4][1],grid[5][1],grid[6][1],grid[7][1],
     grid[1][2],grid[2][2],grid[3][2],grid[4][2],grid[5][2],grid[6][2],grid[7][2],
     grid[1][3],grid[2][3],grid[3][3],grid[4][3],grid[5][3],grid[6][3],grid[7][3],
     grid[1][4],grid[2][4],grid[3][4],grid[4][4],grid[5][4],grid[6][4],grid[7][4],
     grid[1][5],grid[2][5],grid[3][5],grid[4][5],grid[5][5],grid[6][5],grid[7][5],    
    ))

board()


win=False
def winwin():
    for c in range(1,8):
        for r in range(3):
            if grid[c][r]==grid[c][r+1]==grid[c][r+2]==grid[c][r+3]==player[p][0].upper():
                return True
    for r in range(6):
        for c in range(1,5):
            if grid[c][r]==grid[c+1][r]==grid[c+2][r]==grid[c+3][r]==player[p][0].upper():
                return True
    for c in range(1,5):
        for r in range(3):
            if grid[c][r]==grid[c+1][r+1]==grid[c+2][r+2]==grid[c+3][r+3]==player[p][0].upper():
                return True
    for c in range(1,5):
        for r in range(3,6,):
            if grid[c][r]==grid[c+1][r-1]==grid[c+2][r-2]==grid[c+3][r-3]==player[p][0].upper():
                return True
            


prev="hola"
#for round in range(1,22):
while win==False:
        #print("ROUND "+str(round)+":")
        for p in range(2):
            win=False
            if p==0:
                play()
                win=winwin()
                if win==True:
                    print("congrats "+player[p])
                    break
                else:
                    win=False
            else:
                play()
                win=winwin()
                if win==True:
                    print("congrats "+player[p])
                    break
                else:
                    win=False
time.sleep(10)
