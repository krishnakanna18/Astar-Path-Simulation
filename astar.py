import math
import heap as hp
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
            self.g+=1
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
        return math.sqrt((goal[0]-self.x)**2+(goal[1]-self.y)**2)

def construct(goal):
    if(goal.parent==None):
        print(goal,"The starting point")
        return
    construct(goal.parent)
    print(goal)
    
    
def astar(s,goal):
    open=hp.Heap([])
    closed=[]
    src=node(s[0],s[1],None)
    open.push([src.f,src])
    sol=None
    while True:
        # print(open.size)
        if(open.size==0):
            print("The goal is blocked")
            # root.destroy()
            return -1
        cur=open.pop()[1]
        if([cur.x,cur.y]==goal):
            construct(cur)
            sol=cur
            # erase(sol)
            # astar(sol,goal)
            return cur
            break
        closed.append([cur.x,cur.y])
        for possible in cur.succesors():
            if(possible.points()==goal):
                construct(possible)
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

# obstacle=[[i,2]for i in range(99)]+[[i,60]for i in range(99)]
obstacle=[[1,i] for i in range(2,12)]
goal=[1,12]
n=20
astar([1,1],goal)