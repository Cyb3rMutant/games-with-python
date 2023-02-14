import os
import time
word=input("word: ")
while len(word)>10:
    word=input("this word is too long please use another one: ")
letters=[]
for l in word:
    letters.append(l)


stars=len(letters)*"*".split()


if " " in letters:
    for l in range(len(stars)):
        if letters[l]==" ":
            stars[l]=" "
#os.system("cls")
print(*stars,sep="")            



hangman=["O","/","|","\\","/","\\"]
guy={0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" "}
hangedman="""
  +---+
  |   |
  %s   |
 %s%s%s  |
 %s %s  |
      |
------+
""" %(guy[0],guy[1],guy[2],guy[3],guy[4],guy[5])


alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ul=[" "]
mistake=0
letter=0
for p,b in zip(hangman,range(6)):
    mistake=False
    while mistake==False:
        os.system("cls")
        print(hangedman)
        print("used letters:",end=" ")
        for l in ul:
            if l!=" ":
                print(l,end=", ")
        print("")
        print(*stars,sep="")
        letter=input("please enter a letter: ")
        while (letter in ul) or (letter.lower() not in alphabet) or (type(letter)!=str):
            letter=input("please enter another letter: ")
        letter=letter.lower()
        if letter in letters:
            for l in range(len(letters)):
                if letter==letters[l]:
                    stars[l]=letter
        else:
            mistake=True
        ul.append(letter)
        if stars==letters:
            break
        #os.system("cls")
    if stars==letters:
        break
    guy[b]=p
    hangedman="""
  +---+
  |   |
  %s   |
 %s%s%s  |
 %s %s  |
      |
------+
""" %(guy[0],guy[1],guy[2],guy[3],guy[4],guy[5])

if stars==letters:
    print("haha congrats")
else:
    print("boo loser \nWord was: ", word)
time.sleep(5)
