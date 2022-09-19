import math as mp
import MinHeap as Mh
#source vertex and destination vertex
sv=11
dv=17

#initialization and node id and coordinates mapping
count=1
xmax=-1
xmin=-1
ymax=-1
ymin=-1
max_hgrid=-1
max_vgrid=-1
k=-1
n_grids=-1
index=[] #index containing coordinates to 
fh=open("snodes.txt","r")
while(count==1):
    line=fh.readline()
    if(line==''):
        count=0
        break
    else:
        temp_x=float(line.split()[1])
        temp_y=float(line.split()[2])
        temp_node=[]
        temp_node.append(temp_x)
        temp_node.append(temp_y)
        index.append(temp_node)

def load_partition(iid):    
    gnode=[]
    gedge=[]
    gbedge=[]
    overflow=0
    nodecp=0#used for overhead extractions
    nodecc=0#used for main extraction
    fh=open(str(iid)+" .txt","r")
    count=1
    ##code for main bucket processing
    if(overflow==0):
        while(count==1):
            x=fh.readline()
            if(x==''):
                break
            y=x.split()
            if(len(y)==1):#found a special character
                if(y[0]=='##'):
                    nodecc=1
                    edgec=1
                    edgeb=0
                if(y[0]=='%%'):
                    nodecc=2
                   
                if(y[0]=='??'):
                    nodecp=4
                if(y[0]=='**'):
                    nodecp=5
                    
            else:
                if(nodecc==0 and nodecp==0):
                    gnode.append(int(y[0]))
                elif(nodecc==1 and nodecp==0):
                    temp_node=[]
                    temp_node.append(int(y[0]))
                    temp_node.append(int(y[1]))
                    temp_node.append(float(y[2]))
                    
                    gedge.append(temp_node)
                elif(nodecc==2 and nodecp==0):
                    temp_node=[]
                    temp_node.append(int(y[0]))
                    temp_node.append(int(y[1]))
                    temp_node.append(float(y[2]))
                    
                    gbedge.append(temp_node)
                elif(nodecp==5 ):
                   x=fh.readline()
                   
                elif(nodecp==4):
                    overflow=overflow+1
                    
                else:
                    continue
    ##end of code for main bucket file
    fh.close()

    ##processing the overflow buckets
    i=1

    while(i<=overflow):
        fh=open(str(iid)+" "+str(i)+".txt")
        count=1
        nodecp=0
        x=fh.readline()#first line is useless 
        x=fh.readline() #second line is useless
        while(count==1):
            x=fh.readline()
            if(x==''):
                break
            y=x.split()
            if(len(y)==1):#found a special character
                if(y[0]=='##'):
                    nodecc=1
                    edgec=1
                    edgeb=0
                if(y[0]=='%%'):
                    nodecc=2
                    edgeb=1
                    edgec=0
                if(y[0]=='**'):
                   nodecp=4
            else:
                if(nodecc==0 and nodecp==0):
                    gnode.append(int(y[0]))
                elif(nodecc==1 and nodecp==0):
                    temp_node=[]
                    temp_node.append(int(y[0]))
                    temp_node.append(int(y[1]))
                    temp_node.append(float(y[2]))
                    gedge.append(temp_node)
                elif(nodecc==2 and nodecp==0):
                    temp_node=[]
                    temp_node.append(int(y[0]))
                    temp_node.append(int(y[1]))
                    temp_node.append(float(y[2]))
                    gbedge.append(temp_node)
                elif(nodecp==4):
                   x=fh.readline()    
                else:
                    continue
        fh.close()
        i=i+1
    return(gnode,gedge,gbedge,overflow)


def get_grid_no(x,y):
        x_no=(x-xmin)//k
        y_no=(y-ymin)//k
        grid_no=max_hgrid*y_no+x_no
        return int(grid_no)


def meta_data():
    fh=open("metadata.txt","r")
    xmin=float(fh.readline().split()[0])
    xmax=float(fh.readline().split()[0])
    ymin=float(fh.readline().split()[0])
    ymax=float(fh.readline().split()[0])
    k=int(fh.readline().split()[0])
    max_hgrid=mp.ceil((xmax-xmin)/k)
    max_vgrid=mp.ceil((ymax-ymin)/k)
    n_grids=max_hgrid*max_vgrid
    return(xmin,xmax,ymin,ymax,k,max_hgrid,max_vgrid,n_grids)
    

#load basic information for the grid
t=meta_data()
xmin=t[0]
xmax=t[1]
ymin=t[2]
ymax=t[3]
k=t[4]
max_hgrid=t[5]
max_vgrid=t[6]
n_grids=t[7]


##########djisktra starting
gridBoard=[]
distance=[]
visited=[]
close_list=[]
partitionlist=[]
pageflts=0
parent=[]

for i in range(0,len(index)):
    infi=mp.inf
    distance.append(infi)
    parent.append(-1*infi)
    visited.append(0)

for i in range(0,n_grids):
    t=[]
    gridBoard.append(t)


#heap for storing min distance and destination vertex
open_list=Mh.MinHeap()
distance[sv]=0
temp_node=[sv,0]
open_list.insert(temp_node)#insert updated distance  source vertex into heap
while(open_list.size>0):
    t=open_list.delete()
    close_list.append(t)
    vertex=t[0]
    visited[vertex]=1
    gid=get_grid_no(index[vertex][0],index[vertex][1])
    if(vertex==dv):#destination vertex is visited
        break
    if(len(gridBoard[gid])==0):#partition is not loaded
        (ta1,ta2,ta3,ta4)=load_partition(gid)
        pageflts=pageflts+1+ta4
        gridBoard[gid].append(ta1)
        gridBoard[gid].append(ta2)
        gridBoard[gid].append(ta3)
        partitionlist.append(gid)#append to partition list
    temp1=gridBoard[gid][1] #inside partition edges
    temp2=gridBoard[gid][2] #outside partition edges
    temp_nodess=temp1+temp2#all graph edges
    i=0
    while(i<len(temp_nodess)):
       
        if(temp_nodess[i][0]==vertex):
            nvertex=temp_nodess[i][1]
            upd=temp_nodess[i][2]+distance[vertex]
            #scan if node is not already present with small distance in heap
            if(visited[nvertex]==0  and distance[nvertex]>upd):
                distance[nvertex]=upd#update the distance
                parent[nvertex]=vertex#update the parent
                fnd=open_list.search(nvertex)
                if(fnd>=0):
                    open_list.decrease_key(fnd,upd)
                else:
                    open_list.insert([nvertex,upd])#insert in open_list   
        i=i+1
        
def trace_path(sv,dv):
    path=[]
    if(visited[dv]==0):
        print("Vertex not reachable")
    else:
        while(dv!=sv):
            path.append(dv)
            dv=parent[dv]
        path.append(sv)
        while(len(path)!=0):
            print(path.pop(),end=" ")
        
	
print("distance between source and destination")           
print(distance[dv])
print("path from sv to dv")
trace_path(sv,dv)
print("")
print("no of page_faults = ",pageflts)
    
    
    
    
        
        
        
            
        
        
            
        
        

