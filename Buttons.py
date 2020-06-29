import tkinter as tk
class Button:
    __slots__=["x","y","button"]
    def __init__(self,master):
        self.button=tk.Button(master)
        self.button["bg"]="black"
        self.button.rowconfigure(0,weight=2)
        self.button.columnconfigure(0,weight=2)
        self.button["padx"]=master.winfo_screenwidth()//200
        self.button["pady"]=master.winfo_screenheight()//200
        self.button["command"]=self.onPress
        self.button.bind("<Enter>",self.onMotion)
        # self.button.bind("<ButtonPress-1>",self.onPress)
        # self.button.bind("<B1-Motion>",self.onMotion)
        # self.button.bind("<ButtonRelease-1>",self.onRelase)
        # self.button.bind("<Leave>",self.onLeave)

    def onPress(self):
        global press
        print("Pressed button",press)
        if(press==1):
            press=0
            return
        if(press==0):
            self.change()
            press=1
            return

    def onMotion(self,e):
        global press
        if(press==0):
            return
        # print("on Motion")
        if(press==1):
            self.change()

    def change(self):
        global obstacle
        if(self.button["bg"]=="yellow"):
            return
        # print(obstacle)
        if(self.button["bg"]!="blue"):
            if(self.button["bg"]=="white"):
                self.button["bg"]="black"
                obstacle.remove([self.x,self.y])
                obstacleNumber["text"]=str(len(obstacle))
            else:
                self.button["bg"]="white"
                obstacle.append([self.x,self.y])
                obstacleNumber["text"]=str(len(obstacle))
        


    # def onLeave(self,e):
    #     self.button["bg"]="red"

    def onclick(self):
        if(self.button["bg"]=="red"):
            self.button["bg"]="black"
        else:
            self.button["bg"]="red"
    def posSet(self,x,y):
        self.x=x
        self.y=y
        # self.button["text"]="{0}{1}".format(x,y)
        self.button.grid(row=x,column=y)
    def posGet(self):
        return [self.x,self.y]


def buttonsCreate(master):
    arr=[[0 for j in range(n)] for i in range(n)]
    # astar([1,1],goal)
    for i in range(n):
        for j in range(n):
            arr[i][j]=Button(master)
            arr[i][j].posSet(i,j)
    return arr


def undoObstacles():
    while(len(obstacle)>0):
        for block in obstacle:
            arr[block[0]][block[1]].change()

def buttonVariables(game):
    Grid=tk.Frame(game)
    return Grid

obstacle=[]
press=0

