import math
import heap as hp
import tkinter as tk
from threading import Thread, Event
import time
class Button:
    __slots__=["x","y","button"]
    def __init__(self,master):
        self.button=tk.Button(master)
        self.button["bg"]="black"
        self.button["padx"]=master.winfo_screenwidth()//200
        self.button["pady"]=master.winfo_screenheight()//200
        self.button["command"]=self.onclick
        self.button.bind("<Enter>",self.onEnter)
        # self.button.bind("<Leave>",self.onLeave)

    def onEnter(self,e):
        global obstacle
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

class node:
    __slots__=["x","y","g","h","f","parent","hid","v"]
    def __init__(self,x,y,parent):
        global goal
        self.x=x
        self.y=y
        self.g=0
        self.parent=None
        if(parent!=None):
            self.parent=parent
            # self.g=self.heuristic((parent.x,parent.y))
            self.g=parent.g+1
        self.h=self.heuristic(goal)
        self.f=self.g+self.h

    def succesors(self):
        global obstacle
        global n
        possible=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        for move in possible:
            a,b=self.x+move[0],self.y+move[1]
            if(-1<a<n and -1<b<n and [a,b] not in obstacle):
                yield node(a,b,self)

    def points(self):
        return [self.x,self.y]

    def __str__(self):
        return ("Coordinates:{0},{1} ; Dist from parent: {2} ; Dist from goal:{3} ; Heurestic: {4}".format(self.x,self.y,self.g,self.h,self.f))

    def heuristic(self,goal):
        print(goal,"Heurisitcs")
        return math.sqrt((goal[0]-self.x)**2+(goal[1]-self.y)**2)

def construct(goal,moves):
    global arr
    if(goal.parent==None):
        # print(goal,"The starting point")
        arr[goal.x][goal.y].button["bg"]="blue"
        totalMoves.grid(row=n//3,column=n+9,sticky="nswe")
        totalMoves["text"]="The number of moves taken to solve is: \n"+str(moves)
        print()
        return
    construct(goal.parent,moves+1)
    arr[goal.x][goal.y].button["bg"]="blue"
    # print("[",goal.x,",",goal.y,"]",end="  ")
    print(goal)

def erase(sol):
    global arr
    if(sol==None):
        return
    if(sol.parent==None):
        arr[sol.x][sol.y].button["bg"]="black"
        return
    arr[sol.x][sol.y].button["bg"]="black"
    erase(sol.parent)
    
    
def astar(s,goal):
    open=hp.Heap([])
    closed=[]
    print(goal,"The goal")
    print(obstacle,"The obstacle")
    src=node(s[0],s[1],None)
    open.push([src.f,src])
    sol=None
    while True:
        # print(open.size)
        if(open.size==0):
            print("The goal is blocked")
            # root.destroy()
            return  None
        cur=open.pop()[1]
        if([cur.x,cur.y]==goal):
            moves=0
            construct(cur,moves)
            sol=cur
            # erase(sol)
            # astar(sol,goal)
            return cur
            break
        closed.append([cur.x,cur.y])
        for possible in cur.succesors():
            if(possible.points()==goal):
                moves=0
                construct(possible,moves)
                sol=possible
                # erase(sol)
                # astar(s,goal)
                return possible
                sol=possible
                break
            if(possible.points() in closed):
                continue
            if(open.isPresent(possible)):
                child=open.getState(possible.points())
                if(possible.g<child.g):
                    child.parent=cur
                    open.decrease_key([0,child],possible.f)
            else:
                open.push([possible.f,possible])
    erase(sol)
    # astar(s,goal)


def renderGame(source,goal):
    global arr
    global n
    global obstacle
    print(source,"In render game")
    # for i in range(n):
    #     for j in range(n):
    #         arr[i][j].button.unbind("<Enter>")
    def resume(sol):
        erase(sol)
        totalMoves["text"]=""
        root.after(8000,renderGame,source,goal)


    sol=astar([source[0],source[1]],goal) #Called initally and at an interval of 16seconds
    # print(sol,"The sol returned")
    root.after(8000,resume,sol)
    # print(obstacle,"this timeeee...")
    

def startrender():

    def sourceInit(source,sourceValue,goalValue):
        global goal
        source=list(map(int,sourceValue.get().split(',')))
        goal=list(map(int,goalValue.get().split(',')))
        initialise.destroy()
        root.after(10000,renderGame,source,goal)

    initialise=tk.Toplevel()
    sourceLabel=tk.Label(initialise,text="Enter source coordinates").grid(row=0,column=0,sticky="w")
    sourceValue=tk.Entry(initialise)
    sourceValue.grid(row=0,column=1,sticky="e")
    goalLabel=tk.Label(initialise,text="Enter destination coordinates").grid(row=1,column=0,sticky="w")
    goalValue=tk.Entry(initialise)
    goalValue.grid(row=1,column=1,sticky="e")
    source=[]
    enter=tk.Button(initialise,text="Enter source",command=lambda :sourceInit(source,sourceValue,goalValue)).grid(row=2,column=1,sticky="we")
    initialise.mainloop()

# obstacle=[[i,2]for i in range(99)]+[[i,60]for i in range(99)]
obstacle=[]
goal=[]
n=20
root=tk.Tk()
root.title("A* Pathfind Tracing")
# root.attributes('-zoomed',True)
game=tk.Frame(root)
game.pack(fill=tk.BOTH,expand=True)
arr=[[0 for j in range(n)] for i in range(n)]
# astar([1,1],goal)
for i in range(n):
    for j in range(n):
        arr[i][j]=Button(game)
        arr[i][j].posSet(i,j)
print("Before")
closeButton=tk.Button(game,text="Close the game",command=root.destroy)
closeButton.grid(row=n//2,column=j+10,sticky="nwes")
obstacleInfo=tk.Frame(game)
obstacleInfo.grid(row=n//4,column=j+10)
obstacleText="Number of obstacle is: "
displayObstacle=tk.Label(obstacleInfo,text=obstacleText).grid(row=n//4,column=j+8,sticky="nwse")
obstacleNumber=tk.Label(obstacleInfo,text=str(len(obstacle)))
obstacleNumber.grid(row=n//4,column=j+10,sticky="nwse")
totalMoves=tk.Label(game)
root.after(2000,startrender)
root.mainloop()