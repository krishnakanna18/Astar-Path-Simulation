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
        return math.sqrt((goal[0]-self.x)**2+(goal[1]-self.y)**2)

def construct(goal,moves):
    if(goal.parent==None):
        print(goal,"The starting point")
        print(moves,": Taken")
        return
    construct(goal.parent,moves+1)
    # print("[",goal.x,",",goal.y,"]",end="  ")
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

# obstacle=[[i,2]for i in range(99)]+[[i,60]for i in range(99)]
# obstacle=[[i,2] for i in range(0,5)]
obstacle=[[18, 16], [19, 16], [19, 17], [19, 18], [18, 18], [17, 18], [16, 18], [15, 18], [14, 18], [13, 18], [12, 18], [11, 18], [10, 18], [9, 18], [8, 18], [7, 18], [6, 18], [5, 18], [4, 18], [3, 18], [2, 18], [2, 17], [2, 16], [2, 15], [2, 14], [2, 13], [2, 12], [2, 11], [2, 10], [2, 9], [2, 8], [2, 7], [2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [9, 3], [10, 3], [11, 3], [12, 3], [13, 3], [14, 3], [14, 2], [15, 2], [16, 2], [17, 2], [18, 2], [19, 2]]
print(obstacle)
goal=[19,0]
n=20
astar([19,19],goal)