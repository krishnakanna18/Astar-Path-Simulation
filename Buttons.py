import tkinter as tk
class Button:
    __slots__=["x","y","button"]
    press=0
    def __init__(self,master):
        self.button=tk.Button(master)
        self.button["bg"]="black"
        self.button.rowconfigure(0,weight=2)
        self.button.columnconfigure(0,weight=2)
        self.button["padx"]=master.winfo_screenwidth()//200
        self.button["pady"]=master.winfo_screenheight()//200
        self.button["command"]=self.onPress
        self.button.bind("<Enter>",self.onMotion)

    def onPress(self):
        print("Pressed button",Button.press)
        if(Button.press==1):
            Button.press=0
            return
        if(Button.press==0):
            self.change()
            Button.press=1
            return

    def onMotion(self,e):
        if(Button.press==0):
            return
        # print("on Motion")
        if(Button.press==1):
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
                Control.obstacleNumber["text"]=str(len(obstacle))
            else:
                self.button["bg"]="white"
                obstacle.append([self.x,self.y])
                Control.obstacleNumber["text"]=str(len(obstacle))
        
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

class Buttons:
    arr=[]
    n=0
    obstacle=[]
    def __init__(self,n=None,game=None):
        Buttons.n=n
        Buttons.Grid=tk.Frame(game)
        
    def buttonsCreate(self,master):
        Buttons.arr=[[0 for j in range(Buttons.n)] for i in range(Buttons.n)]
        # astar([1,1],goal)
        for i in range(Buttons.n):
            for j in range(Buttons.n):
                Buttons.arr[i][j]=Button(master)
                Buttons.arr[i][j].posSet(i,j)
        return Buttons.arr

    def undoObstacles(self):
        while(len(Buttons.obstacle)>0):
            for block in Buttons.obstacle:
                Buttons.arr[block[0]][block[1]].change()

class Control:

    def __init__(self,n,game,root):
        Control.n=n
        Control.controls=tk.Frame(game)
        Control.controls.grid(row=0,column=n+4)
        Control.closeButton=tk.Button(Control.controls,text="Close the game",command=root.destroy)
        Control.closeButton.grid(row=n//2+3,column=n+10,sticky="nwes")
        Control.obstacleInfo=tk.Frame(Control.controls)
        Control.obstacleInfo.grid(row=n//4,column=n+10)
        Control.obstacleText="Number of obstacle is: "
        Control.displayObstacle=tk.Label(Control.obstacleInfo,text=Control.obstacleText).grid(row=n//4,column=n+8,sticky="nwse")
        Control.obstacleNumber=tk.Label(Control.obstacleInfo,text=str(len(obstacle)))
        Control.obstacleNumber.grid(row=n//4,column=n+10,sticky="nwse")
        Control.totalMoves=tk.Label(Control.controls)
        Control.clearObstacles=tk.Button(Control.controls,text="Clear all obstacles",command=Buttons().undoObstacles)
        Control.clearObstacles.grid(row=n//8,column=n+10,sticky="nwse")
        Control.Pause=tk.Button(Control.controls)



obstacle=Buttons.obstacle