import math as mp
import MinHeap as mh
#source vertex and destination vertex

sv=11
dv=17
#graph processing and meta data processing
fh=open("metadata.txt","r")
xmin=float(fh.readline().split()[0])
xmax=float(fh.readline().split()[0])
ymin=float(fh.readline().split()[0])
ymax=float(fh.readline().split()[0])
k=int(fh.readline().split()[0])
N=k=int(fh.readline().split()[0])
fh.close()# read meta data successfully
visited=[]
parent=[]
distance=[]
g=[]
infi=mp.inf
ninfi=mp.inf*-1
#Creating structures
for i in range(0,N):
    visited.append(0)
    parent.append(ninfi)
    distance.append(infi)
    g.append([])

#populating the graph
fh=open("sedges.txt","r")
count=1
while(count==1):
    line=fh.readline()
    if(line==''):
        count=0
        break
    else:
        n1_id=int(line.split()[0])
        n2_id=int(line.split()[1])
        wt=float(line.split()[2])
        if(len(g[n1_id])==0):
            temp_edge=[n2_id,wt]
            g[n1_id].append(temp_edge)
        else:
            x=len(g[n1_id])
            epres=0
            while(i<x):
                if(g[n1_id][0]==n2_id):
                    epres=1
                    break
                i=i+1
            if(epres==0):
                g[n1_id].append([n2_id,wt])

#djisktra beggining
on=mh.MinHeap()# min heap for storing the min distances
close_node=[]#close node
distance[sv]=0
temp_node=[sv,0]
on.insert(temp_node)
minid=0#initally 0 is the min index
status=1 #indicating destination vertex is not found
while(on.size>0):
    if(on.size==1):
        t=on.delete()#remove the minimum element from
    else:
        t=on.delete()#(on[minid],on[-1])=(on[-1],on[minid])# min distance vertex is last node
    close_node.append(t)#append the list into close node
    vertex=t[0]
    visited[vertex]=1# mark the vertex as visited
    if(vertex==dv):# destination vertex is found
        break
    lal=len(g[vertex])
    i=0
    while(i<lal):
            nvertex=g[vertex][i][0]
            upd=g[vertex][i][1]+distance[vertex]
            if(visited[nvertex]==0  and distance[nvertex]>upd):
                distance[nvertex]=upd#update the distance
                parent[nvertex]=vertex
                fnd=on.search(nvertex)
                if(fnd>=0):
                    on.decrease_key(fnd,upd)
                else:
                    on.insert([nvertex,upd])#insert in open_list   
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

    

