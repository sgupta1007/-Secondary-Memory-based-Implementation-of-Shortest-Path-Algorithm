class MinHeap:
    def __init__(self):
        self.size=0
        self.heap=[]
    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False
    def insert(self,x):
        item=x
        if(self.isEmpty()):
            self.heap.append(x)
            self.size=self.size+1
            #print(self.heap)
        else:
            self.heap.append(x)#append to last of the heap
            pos=self.size
            status=1
            while(status==1 and pos>0):
                pos1=(pos-1)//2
                #print(pos,pos1,self.heap[pos][1],self.heap[pos1][1],sep=" ")
                if(self.heap[pos][1]<self.heap[(pos-1)//2][1]):
                #print(" b swapping ",self.heap[pos],self.heap[(pos-1)//2],sep="  ")
                    (self.heap[pos],self.heap[(pos-1)//2])=(self.heap[(pos-1)//2],self.heap[pos])
                #print(" a swapping ",self.heap[pos],self.heap[(pos-1)//2],sep="  ")
                #print(self.heap)
                    pos=pos1
                else:
                    break
            self.size=self.size+1#increase heap size
            
    def delete(self):
        x=len(self.heap)
        onode=None
        if(x>0):
            i=0
            (self.heap[0],self.heap[x-1])=(self.heap[x-1],self.heap[0])
            onode=self.heap.pop()
            while(i<len(self.heap)):
                    i1=2*i+1
                    i2=2*i+2
                    if(i2<len(self.heap)):
                            if(self.heap[i1][1]>self.heap[i2][1]):
                                    if(self.heap[i2][1]<self.heap[i][1]):
                                            (self.heap[i],self.heap[i2])=(self.heap[i2],self.heap[i])
                                            i=i2
                                    else:
                                            break
                            else:
                                    if(self.heap[i1][1]<self.heap[i][1]):
                                            (self.heap[i],self.heap[i1])=(self.heap[i1],self.heap[i])
                                            i=i1
                                    else:
                                            break
                    elif(i1<len(self.heap)):
                            if(self.heap[i1][1]<self.heap[i][1]):
                                    (self.heap[i1],self.heap[i])=(self.heap[i],self.heap[i1])
                                    i=i1
                            else:
                                    break
                    else:
                            break
            self.size=self.size-1
        return onode
    # to search whether key is present in node
    def search(self,key):
        loc=-1
        for i in range(0,len(self.heap)):
            if(key==self.heap[i][0]):
                return i
        return loc
    # decrease the key value since value is updated
    def decrease_key(self,pos,value):
        pos1=(pos-1)//2
        self.heap[pos][1]=value
        while(self.heap[pos][1]<self.heap[pos1][1] and pos>0):
            (self.heap[pos],self.heap[pos1])=(self.heap[pos1],self.heap[pos])
            pos=pos1
            pos1=(pos-1)//2
                        
            
                    
        
            
            
#b=MinHeap()

#b.insert([2,50])
#b.insert([5,70])
#b.insert([3,12])
#b.insert([1,21])
#b.insert([4,16])
#b.insert([6,4])
#x=b.search(5)
#b.decrease_key(x,2)
#print(b.heap)
#b.delete()
#b.delete()
#b.delete()
#print(b.heap)
#b.delete()
#b.delete()
#b.delete()
#b.delete()
#print(b.heap)

