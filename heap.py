import math
class trial:
    __slots__=["hid","v"]
    def __init__(self,v):
        self.v=v
        self.hid=-1
class Heap:
    __slots__=["size","heap_arr","index_map"]
    def __init__(self,arr):
        self.heap_arr=arr
        self.size=len(arr)
        self.index_map=dict()
    # def heapify(self):
    #     start=self.size//2-1
    #     parent=start//2
    #     while(parent>=0):
    def increase_key(self,state_tup,new_key):
        id=self.index_map[state_tup[1].hid]
        self.heap_arr[id][0]=new_key
        self.heap_arr[id][1].v=new_key
        # print(self.heap_arr,id,self.index_map)
        l=r=id
        while(id<self.size//2):
            min=self.heap_arr[id]
            mid=id
            l=2*id+1
            r=2*id+2
            if(self.heap_arr[l][0]<=self.heap_arr[id][0] and l<self.size):
                min=self.heap_arr[l]
                mid=l
            if(self.heap_arr[r][0]<min[0] and r<self.size):
                min=self.heap_arr[r]
                mid=r
            # print(mid)
            if(mid==id):
                break
            if(mid!=id):
                self.heap_arr[id],self.heap_arr[mid]=self.heap_arr[mid],self.heap_arr[id]
                self.index_map[self.heap_arr[id][1].hid],self.index_map[self.heap_arr[mid][1].hid]=self.index_map[self.heap_arr[mid][1].hid],self.index_map[self.heap_arr[id][1].hid],
                # self.index_map[self.heap_arr[id][1]],self.index_map[self.heap_arr[mid][1]]=self.index_map[self.heap_arr[mid][1]],self.index_map[self.heap_arr[id][1]]
                self.heap_arr[id][1].hid,self.heap_arr[mid][1].hid=self.heap_arr[mid][1].hid,self.heap_arr[id][1].hid,
                id=mid
    def decrease_key(self,state_tup,new_key):
        id=self.index_map[state_tup[1].hid]
        self.heap_arr[id][0]=new_key
        self.heap_arr[id][1].v=new_key
        # print(new_key)
        p=id//2
        while(p>=0):
            p=id//2
            if(self.heap_arr[p][0]>self.heap_arr[id][0]):
                op=p; oid=id
                # print(op,oid)
                self.heap_arr[id],self.heap_arr[p]=self.heap_arr[p],self.heap_arr[id]
                self.index_map[self.heap_arr[id][1].hid],self.index_map[self.heap_arr[p][1].hid]=self.index_map[self.heap_arr[p][1].hid],self.index_map[self.heap_arr[id][1].hid]
                # self.heap_arr[id][1].hid,self.heap_arr[p][1].hid=self.heap_arr[p][1].hid,self.heap_arr[id][1].hid
                id=p
            else:
                break
    def push(self,state_tup):
        key=state_tup[0]
        # self.heap_arr[state_tup[1].hid][1].v=state_tup[0]
        state_tup[0]=math.inf
        self.heap_arr+=[state_tup]
        state_tup[1].hid=self.size
        self.index_map[state_tup[1].hid]=self.size
        # print(self.index_map)
        # self.heap_arr[state_tup[1].hid][1].v=state_tup[0]
        self.size+=1
        self.decrease_key(state_tup,key)

    def pop(self):
        ret=self.heap_arr[0]
        self.heap_arr[0]=self.heap_arr[self.size-1]
        self.index_map[self.heap_arr[0][1].hid]=0
        self.size-=1
        # print(list(map(lambda x:x[1].v,self.heap_arr)))
        self.increase_key(self.heap_arr[0],self.heap_arr[0][0])
        self.heap_arr=self.heap_arr[:-1]
        return ret

    def getState(self,points):
        for cur in self.heap_arr:
            if(cur[1].points()==points):
                return cur[1]

    def isPresent(self,state):
        for cur in self.heap_arr:
            if([cur[1].x,cur[1].y]==[state.x,state.y]):
                return 1
        return 0

    


# t1=trial(1)
# t2=trial(2)
# t3=trial(3)
# t4=trial(4)
# t5=trial(5)
# t6=trial(6)
# arr=[]
# heap=Heap(arr)
# heap.push([100,t1])
# print(heap.index_map)
# print(heap.heap_arr[0][1].v)
# heap.push([200,t2])
# print(heap.index_map)
# heap.push([500,t3])
# heap.push([400,t4])
# heap.push([300,t5])
# heap.push([600,t6])
# print(heap.index_map)
# print(list(map(lambda x:x[1].v,heap.heap_arr)))
# heap.decrease_key([5,t4],150)
# print("The value {} is present in {}".format(t5.v,heap.index_map[t5.hid]))
# heap.increase_key([1,t4],400)
# print(list(map(lambda x:x[1].v,heap.heap_arr)))
# # heap.decrease_key([9,t4],-10101)
# # print(list(map(lambda x:x[1].v,heap.heap_arr)))
# print(heap.index_map)
# # r=heap.pop()
# # print(list(map(lambda x:x[1].v,heap.heap_arr)))
# # r=heap.pop()
# # print(list(map(lambda x:x[1].v,heap.heap_arr)))
# # r=heap.pop()
# # print(list(map(lambda x:x[1].v,heap.heap_arr)))
# # heap.increase_key([1,t6],10)
# # print(list(map(lambda x:x[1].v,heap.heap_arr)))