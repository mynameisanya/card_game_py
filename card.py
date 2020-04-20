from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import time
import random
import math
import turtle

root = Tk()
root.geometry('284x430')
root.title("Парные картинки")

def click(event,n,m):
    global k,x,y,win,img0,color,count,num,buttons,img,imgS,imgW,img1
    if buttons[n][m]['state']!=DISABLED:
        buttons[n][m]['image']=img0[n][m]
        root.update()
        if k==0:
            x=n
            y=m
            k+=1
            return
        if k==1 and (n!=x or m!=y):
            if str(img[n][m])==str(img[x][y]):
                win+=2
                time.sleep(1)
                buttons[n][m]['image']=imgW
                buttons[x][y]['image']=imgW
                buttons[n][m]['state']=DISABLED
                buttons[x][y]['state']=DISABLED
                k=0
                x=5
                y=5
                count+=1
                if win==16:
                    time.sleep(1)
                    won()
                return
        time.sleep(1)
        buttons[n][m]['image']=imgS
        buttons[x][y]['image']=imgS
        k=0
        x=5
        y=5
        count+=1
        steps()
        return

def won():
    global img0,color,buttons,img,imgS,imgW,img1,k,win,count
    diapason = 0
    size = 600
    root2 = Tk()
    root2.title('Победа!')
    root2.geometry('600x600')
    canv1 = Canvas(root2,width=size, height=size)
    canv1.pack()
    while diapason < 2000:
        colors = random.choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime',])
        x0 = random.randint(-size/10, size)
        y0 = random.randint(-size/10, size)
        d = random.randint(0, size/5)
        canv1.create_oval(x0, y0, x0+d, y0+d, fill=colors)
        root.update()
        diapason += 1
    l = Label(canv1,text='Вы выйграли!', bg = 'green', fg='white', font = 'Arial 32')
    l.place(x=180,y=300)
def steps():
    global img0,color,buttons,img,imgS,imgW,img1,k,win,count
    canv1 = Label(root,text='Ход: '+str(count))
    canv1.place(x=10, y=390)

def data():
    global img0,color,buttons,img,imgS,imgW,img1,k,win,count,f
    f=1
    img = [ ["1_2.gif","1_3.gif","1_4.gif","1_5.gif"],
            ["1_6.gif","1_7.gif","1_8.gif","1_9.gif"],
            ["1_2.gif","1_3.gif","1_4.gif","1_5.gif"],
            ["1_6.gif","1_7.gif","1_8.gif","1_9.gif"]  ]
    p=[]
    for i in img:
        for j in i:
            p.append(j)
    random.shuffle(p)
    q=-1
    for i in range(4):
        for j in range(4):
            q+=1
            img[i][j]=p[q]
    img0 = []
    buttons = []
    k=0
    x=5
    y=5
    win=0
    count=0

    color=['black','white','brown','blue','red','yellow','green']
    imgS=PhotoImage(file="back.gif")
    imgW=PhotoImage(file="1_0.gif")
    for i in range(4):
        buttons.append([])
        img0.append([])
        for j in range(4):
            img1=PhotoImage(file=str(img[i][j]))
            img0[i].append(img1)
            button = Button(root, width = 65, height = 90, image = imgS)        
            buttons[i].append(button)
            buttons[i][j].grid(row = i, column = j)
            buttons[i][j].bind('<Button-1>',lambda event, i = i, j = j : click(event, i, j))

def info():
    global img0,color,buttons,img,imgS,imgW,img1,k,win,count
    canv1 = Canvas(root,bg='white',width=284, height=430)
    canv1.place(x=0,y=0)
    text = Text(canv1, state='normal', width=36, height=10, wrap=WORD)
    text.place(x=0, y=0)
    text.insert(END, 'Игра "Парные карты," разработала проект Анна Янпольская')
    text.configure(state='disabled')

def exit():
    sys.exit()
	
def menu():
    main_menu = Menu()
    main_menu.add_cascade(label="Start", command=data)
    main_menu.add_cascade(label="Info", command=info)
    main_menu.add_cascade(label="Exit", command=exit)
    root.config(menu=main_menu)
menu()
root.mainloop()
