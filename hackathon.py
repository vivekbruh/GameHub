import tkinter
import PIL
import time
import random
from tkinter import *
from PIL import Image, ImageTk

#Main list that contains all the words that can be pulled for the game
word_list =["zenith", "zealot", "yearn", "yawner", "xenophobia", "wonky", "wanton", "vermillion", "vague",
"unique", "uncanny", "tenacious", "tangible", "serene", "saquinavir", "rhetorical", "rambunctious",
"quixotic", "quell", "pique", "paradigm", "oxymoron", "optimistically", "nostalgic", "narrative",
"misanthrope", "melancholy", "lucid", "lethargic", "ken", "karma", "jurisdiction", "jejune", "irony",
"integrity", "hypnosis", "hyperbole", "guise", "gallivant", "fortitude", "fervent"]
def get_user_inp():
    user_inp = []
    while len(user_inp) < 3:
        inp = input("What were the words?: ")
        user_inp.append(inp)
    return user_inp
    
#Makes a timer for the user to see how long they have
def timer(delay):
    for i in range(delay):
        print(delay-i)
        time.sleep(1)

#Function to hide the words after the time runs out
def hide_world():
    for i in range(100):
        print("*")
#Checks the list and the user inputted list to see if they are the same. If they are,
#the user moves on to the next level and if they aren't, they fail
def check(list_one, list_two):
    points = 0
    for i in range(3):
        if list_one[i] == list_two[i]:
            points += 1
        else:
            points = points
    if points == 1:
        print("Sorry, you only got " + str(points) + " words correct.")
        return False
    if points == 2:
        print("Sorry, you only got " + str(points) + " words correct.")
        return False
    if points == 3:
        print("Congrats, you got all three words correct!")
        return True
    if points == 0:
        print("Sorry, you didn't get any words correct.")
        return False 
 
#Main function. When it is called the game will start.
def main():
    print("""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─████████████████───████████████──────██████████████─██████████████─██████──────────██████─██████████████─
─██░░██──────────██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░████────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─
─██░░██──────────██░░██─██░░██████░░██─██░░████████░░██───██░░████░░░░██────██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████████─
─██░░██──────────██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██────██░░██─────────██░░██──██░░██─██░░██████░░██████░░██─██░░██─────────
─██░░██──██████──██░░██─██░░██──██░░██─██░░████████░░██───██░░██──██░░██────██░░██─────────██░░██████░░██─██░░██──██░░██──██░░██─██░░██████████─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██────██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██████░░████───██░░██──██░░██────██░░██──██░░██─██░░██████░░██─██░░██──██████──██░░██─██░░██████████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██────██░░██──██░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██─────────
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░██──██░░██████─██░░████░░░░██────██░░██████░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██████████─
─██░░██████░░██████░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░████────██░░░░░░░░░░██─██░░██──██░░██─██░░██──────────██░░██─██░░░░░░░░░░██─
─██████──██████──██████─██████████████─██████──██████████─████████████──────██████████████─██████──██████─██████──────────██████─██████████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    print("Memorize the three words and type them when you are prompted to! Only type one word per response and type them in the order you saw them!")
    print("Have fun!")
    print("REMEMBER: NO SCROLLING UP!")
    time.sleep(10)
    delay = 5
    while True:
    #Makes the new list of guessing words for every level
        #window1 = tkinter.Tk()
        #window1.geometry("800x500+200+150")
        #window1.title("Word Game")
        #label2 = tkinter.Label(window1, text = "Welcome to the word game!").pack()
        #label2.place(x=0,y=0)
        #window1.mainloop()
        new_list = []
        while len(new_list) < 3:
            nl_index = random.randint(0, len(word_list))
            if word_list[nl_index] not in new_list:
                new_list.append(word_list[nl_index])
        print(new_list)
        timer(delay)
        hide_world()
        user = get_user_inp()
        #Call to the function to check if the user and 
        valid_win = check(user, new_list)
        if valid_win == True:
            delay = delay - 1
            print("""
        
            ██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██╗░░░██╗██████╗░
            ██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ██║░░░██║██╔══██╗
            ██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██║░░░██║██████╔╝
            ██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██║░░░██║██╔═══╝░
            ███████╗███████╗░░╚██╔╝░░███████╗███████╗  ╚██████╔╝██║░░░░░
            ╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░░░░""")
            time.sleep(3)
            hide_world()
        else:
            print("""
            ████████╗██████╗░██╗░░░██╗  ░█████╗░░██████╗░░█████╗░██╗███╗░░██╗
            ╚══██╔══╝██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔════╝░██╔══██╗██║████╗░██║
            ░░░██║░░░██████╔╝░╚████╔╝░  ███████║██║░░██╗░███████║██║██╔██╗██║
            ░░░██║░░░██╔══██╗░░╚██╔╝░░  ██╔══██║██║░░╚██╗██╔══██║██║██║╚████║
            ░░░██║░░░██║░░██║░░░██║░░░  ██║░░██║╚██████╔╝██║░░██║██║██║░╚███║
            ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝""")
            break
        if delay == 0:
            print("Congrats, you have beat all 5 levels of the Memory Game! Play again!")
            break

def main3():
    print("""         _.-----._
      .-'         `-.
    .'     _..._     `.
   :     .' .-. `.     :
  :     :  :   :  :     :
 :      :  :   :  :      :
 :       `._`-'_.'       :
 :       .' .-. `.       :
 :      :  :   :  :      :
  :     :  :   :  :     :
   :     `._`-'_.'     :
    `.      '''      .'
      `-._       _.-'
          `-----'""")
    word_list1 = ["I can't predict that now.","No","Perhaps...","Ask again later","Don't count on it","It is certain.","Signs point to yes!","Without a doubt.","NO!!","My reply is no","I don't believe so"]
    while True:
        q = input("What is your question? (Type -1 to quit) ")
        if q == "-1":
            break
        i = random.randint(0,10)
        print(word_list1[i])

def main2():
    print("""W E L C O M E   T O
▀█▀ █ █▀▀ ▄▄ ▀█▀ ▄▀█ █▀▀ ▄▄ ▀█▀ █▀█ █▀▀
░█░ █ █▄▄ ░░ ░█░ █▀█ █▄▄ ░░ ░█░ █▄█ ██▄""")
    def checkWin(posList,numCheck):
        if posList[0] == numCheck:
            if posList[1] == numCheck:
                if posList[2] == numCheck:
                    return numCheck;
            if posList[4] == numCheck:
                if posList[8] == numCheck:
                    return numCheck
            if posList[3] == numCheck:
                if posList[6] == numCheck:
                    return numCheck
        if posList[1] == numCheck:
            if posList[4] == numCheck:
                if posList[7] == numCheck:
                    return numCheck
        if posList[2] == numCheck:
            if posList[4] == numCheck:
                if posList[6] == numCheck:
                    return numCheck
            if posList[5] == numCheck:
                if posList[8] == numCheck:
                    return numCheck
        if posList[3] == numCheck:
            if posList[4] == numCheck:
                if posList[5] == numCheck:
                    return numCheck
        if posList[6] == numCheck:
            if posList[7] == numCheck:
                if posList[8] == numCheck:
                    return numCheck
        return 0

    def drawBoard(posList):
        print("|" + str(symbolAt(posList[0])) + "|" + str(symbolAt(posList[3])) + "|" + str(symbolAt(posList[6])) + "|\n|" + str(symbolAt(posList[1])) + "|" + str(symbolAt(posList[4])) + "|" + str(symbolAt(posList[7])) + "|\n|" + str(symbolAt(posList[2])) + "|" + str(symbolAt(posList[5])) + "|" + str(symbolAt(posList[8])) + "|")

    def symbolAt(num):
        if num==1:
            return "X"
        if num == 2:
            return "O"
        return " "

    pos_List = [0,0,0,0,0,0,0,0,0]
    sentinel = 0
    print("To play tic tac toe, type the position of the spot you want to put the X or O according to this grid")
    print("|1|4|7|\n|2|5|8|\n|3|6|9|")
    while(sentinel == 0):
        sentinel = checkWin(pos_List,1)
        sentinel = checkWin(pos_List,2)
        while True:
            print("Player 1: ")
            num = int(input())
            if not((num>0 and num<10) and pos_List[num-1] == 0):
                print("invalid number go again")
                continue
            break
        pos_List[num-1] = 1
        drawBoard(pos_List)
        sentinel = checkWin(pos_List,1)
        if checkWin(pos_List,1) == 1:
            break
        while True:
            print("Player 2: ")
            num = int(input())
            if not((num>0 and num<10) and pos_List[num-1] == 0):
                print("invalid number go again")
                continue
            break
        pos_List[num-1] = 2
        drawBoard(pos_List)
        sentinel = checkWin(pos_List,2)

    print("Player " + str(sentinel) + " Wins")

def example():
    window.destroy()
    main()

def example2():
    window.destroy()
    main2()

def example3():
    window.destroy()
    main3()

window = tkinter.Tk()
window.title("Game Hub")
label = tkinter.Label(window, text = "Welcome to the word game!").pack()
window.geometry("1270x710+300+150")
# Create a photoimage object of the image in the path
image1 = Image.open(r"C:\Users\swamy\OneDrive\Desktop\Misc\haha\FINAL0000.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
quit1 = Button(window, text = 'Quit', width = '50',height= '3', command=window.destroy)
play1 = Button(window, text = 'Word Game', width = '40', height = '3', command=example)
play2 = Button(window, text = 'Tic Tac Toe', width = '40', height = '3', command=example2)
play3 = Button(window, text = 'Magic 8-Ball', width = '40', height = '3', command=example3)
# Set the position of button on the top of window.
quit1.place(x=465,y=450)
play1.place(x=150,y=295)
play2.place(x=500,y=295)
play3.place(x=850,y=295)
# Position image
label1.place(x=0, y=0) 

window.mainloop()