import math
import heap as hp
import tkinter as tk
import time
from Buttons import *
#Changed in version2
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
        # obstacle=Buttons.obstacle
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
        return math.sqrt((goal[0]-self.x)**2+(goal[1]-self.y)**2)


def construct(goal,moves):
    global arr
    if(goal==None):
        totalMoves["text"]="The goal cannot be reached"
        totalMoves.grid(row=n//3,column=n+10,sticky="nswe")
    if(goal.parent==None):
        # print(goal,"The starting point")
        # arr[goal.x][goal.y].button["bg"]="blue"
        totalMoves.grid(row=n//3,column=n+10,sticky="nswe")
        totalMoves["text"]="The number of moves taken to solve is: \n"+str(moves)
        print()
        return
    construct(goal.parent,moves+1)
    if(arr[goal.x][goal.y].button["bg"]!="yellow"):
        arr[goal.x][goal.y].button["bg"]="blue"
    # print("[",goal.x,",",goal.y,"]",end="  ")

def erase(sol):
    global arr
    if(sol==None):
        return
    if(sol.parent==None):
        return
    if(arr[sol.x][sol.y].button["bg"]!="yellow"):
        arr[sol.x][sol.y].button["bg"]="black"
    erase(sol.parent)

def pathnode(x,y):
    global arr
    if(arr[x][y].button["bg"]!="blue" and arr[x][y].button["bg"]!="yellow"):
        arr[x][y].button["bg"]!="green"
    
    
def astar(s,goal):
    print(obstacle)
    open=hp.Heap([])
    closed=[]
    print(goal,"The goal")
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
        pathnode(cur.x,cur.y)
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
                    try:
                        open.decrease_key([0,child],possible.f)
                    except:
                        print(cur,child,possible,"The possible")
            else:
                open.push([possible.f,possible])
    erase(sol)
    # astar(s,goal)

# def resume(sol,source,goal):
#         erase(sol)
#         Pause.grid_forget()
#         # Pause["text"]=""
#         totalMoves["text"]=""
#         st=time.time()
#         root.after(5000,renderGame,source,goal)
#         print("Time taken: ",time.time()-st)

# def pause(sol,source,goal):
#     global paused
#     if(paused==1):
#         Pause["text"]="Stop"
#         paused=0
#         resume(sol,source,goal)
#         return
#     else:
#         paused=1
#         print("Atleast")
#         Pause["text"]="Start"

# def renderGame(source,goal):
#     global n
#     global paused
#     print(source,"In render game")
#     # for i in range(n):
#     #     for j in range(n):
#     #         arr[i][j].button.unbind("<Enter>")

#     sol=astar([source[0],source[1]],goal) #Called initally and at an interval of 16seconds
#     # print(sol,"The sol returned")
#     if(sol==None):
#         totalMoves["text"]="The goal cannot be reached"
#         totalMoves.grid(row=n//3,column=n+10,sticky="nswe")
#     # Pause.grid(row=n//2,column=n+10)
#     # Pause["command"]=lambda : pause(sol,source,goal)
#     # root.after(3000,resume,sol,source,goal)
#     # print(obstacle,"this timeeee...")

def renderGame(source,goal):
    global n
    global paused
    print(source,"In render game")

    def resume(sol,source,goal):
        erase(sol)
        Pause.grid_forget()
        # Pause["text"]=""
        totalMoves["text"]=""
        st=time.time()
        root.after(5000,renderGame,source,goal)
        print("Time taken: ",time.time()-st)

    sol=astar([source[0],source[1]],goal) #Called initally and at an interval of 16seconds
    # print(sol,"The sol returned")
    if(sol==None):
        totalMoves["text"]="The goal cannot be reached"
        totalMoves.grid(row=n//3,column=n+10,sticky="nswe")

    root.after(3000,resume,sol,source,goal)
    # print(obstacle,"this timeeee...")

def startrender():

    def sourceInit(source,sourceValue,goalValue):
        global goal
        source=list(map(int,sourceValue.get().split(',')))
        goal=list(map(int,goalValue.get().split(',')))
        arr[source[0]][source[1]].button["bg"]="yellow"
        arr[goal[0]][goal[1]].button["bg"]="yellow"
        initialise.destroy()
        root.after(6000,renderGame,source,goal)

    initialise=tk.Toplevel()
    sourceLabel=tk.Label(initialise,text="Enter source coordinates").grid(row=0,column=0,sticky="w")
    sourceValue=tk.Entry(initialise)
    sourceValue.grid(row=0,column=1,sticky="e")
    goalLabel=tk.Label(initialise,text="Enter destination coordinates").grid(row=1,column=0,sticky="w")
    goalValue=tk.Entry(initialise)
    goalValue.grid(row=1,column=1,sticky="e")
    source=[]
    enter=tk.Button(initialise,text="Start!",command=lambda :sourceInit(source,sourceValue,goalValue)).grid(row=2,column=1,sticky="we")
    initialise.mainloop()

# obstacle=[[i,2]for i in range(99)]+[[i,60]for i in range(99)]
goal=[]
n=18
press=0
root=tk.Tk()
root.title("A* Pathfind Tracing")
# root.attributes('-zoomed',True)
game=tk.Frame(root)
# game.pack(fill=tk.BOTH,expand=True)
game.pack()
buttons=Buttons(n,game)
Grid=Buttons.Grid
arr=buttons.buttonsCreate(Grid)
print("Before")
Grid.grid(row=0,column=0)
Controls=Control(n,game,root)
Pause=Control.Pause
Pause["text"]="Start"
paused=1
totalMoves=Control.totalMoves
root.after(2000,startrender)
root.mainloop()