import math as m

#-----------------------------------section1--------------------------------
#global constant can be changed to view the results
k=5
b=4

#----------------------------------section2------------------------------------
class Grid():
    def __init__(self,iid,k1,b1,a,b,c,d):
        self.id=iid
        self.overflow=0
        self.nodes=[]
        self.edges=[]
        self.bedges=[]
        self.maxx=b
        self.minx=a
        self.maxy=d
        self.miny=c
        self.disk_cap=b1
        self.grid_size=k1
        
    def inf(self):
        print("id of the grid ",self.id)
        print("x boundary coordinate ")
        print("x min ",self.minx)
        print("x max ",self.maxx)
        print("y boundary coordinate ")
        print("y min ",self.miny)
        print("y max ",self.maxy)
        print(" ")
    def add_edge(self,a,b,c):
        temp_edge=[]
        temp_edge.append(a)
        temp_edge.append(b)
        temp_edge.append(c)
        self.edges.append(temp_edge)
    def add_node(self,x):
        temp_node=[]
        temp_node.append(x)
        self.nodes.append(temp_node)
    def add_bedge(self,a,b,c):
        temp_edge=[]
        temp_edge.append(a)
        temp_edge.append(b)
        temp_edge.append(c)
        self.bedges.append(temp_edge)
    def check_edge(self,a,b,c):
        count=0
        for i in self.edges:
            if(i[0]==a):
                if(i[1]==b):
                    if(i[2]==c):
                        count=1
                        break
        return count
    def check_bedge(self,a,b,c):
        count=0
        for i in self.bedges:
            if(i[0]==a):
                if(i[1]==b):
                    if(i[2]==c):
                        count=1
                        break
        return count
    def write_file(self,i,j,k,disk_cap,ind_node):
        n_records=disk_cap-2
        u=0
        fname=str(self.id)+" "
        if(self.overflow!=0):
            main_f=str(self.id)+" "+".txt"+"\n"
            fname=fname+str(self.overflow)
        fname=fname+".txt"
        fh=open(fname,"a")
        t=self.overflow
        if(t>0):
            meta_data="??\n"
            fh.write(meta_data)
            fh.write(main_f)
        while(u<n_records):
            if(i<len(self.nodes)):
                temp_str=str(self.nodes[i][0])+" "
                t_index=int(self.nodes[i][0])
                temp_str=temp_str+str(ind_node[t_index][0])+" "+str(ind_node[t_index][1])+"\n"
                fh.write(temp_str)
                i=i+1
                u=u+1
            if(i>=len(self.nodes)):
                if(j<len(self.edges)):
                    
                    if(j==0):
                        meta_data="##\n"
                        fh.write(meta_data)
                    temp_str=str(self.edges[j][0])+" "+str(self.edges[j][1])+" "+str(self.edges[j][2])+"\n"
                    fh.write(temp_str)
                    j=j+1
                    u=u+1
                if(j>=len(self.edges)):
                    if(k<len(self.bedges)):
                        if(k==0):
                            meta_data="%%\n"
                            fh.write(meta_data)
                        temp_str=str(self.bedges[k][0])+" "+str(self.bedges[k][1])+" "+str(self.bedges[k][2])+"\n"
                        fh.write(temp_str)
                        k=k+1
                        u=u+1
                    if(k>=len(self.bedges)):
                        break
        meta_data="**\n"
        fh.write(meta_data)
        temp_str=str(self.minx)+" "+str(self.maxx)+"\n"
        fh.write(temp_str)
        temp_str=str(self.miny)+" "+str(self.maxy)+"\n"
        fh.write(temp_str)
        if(self.overflow==0 and (m.floor((len(self.edges)+len(self.bedges)+len(self.nodes))/n_records)>=1)):
            meta_data="??\n"
            fh.write(meta_data)
            n_overflows=m.ceil((len(self.edges)+len(self.bedges)+len(self.nodes))/n_records)-1
            t=1
            for t in range(1,n_overflows+1):
                temp_str=str(self.id)+" "+str(t)+".txt"+"\n"
                fh.write(temp_str)
        fh.close()
        return (i,j,k)
    
    def write_grid(self,ind_node):
        i=0
        j=0
        k=0
        n_rounds=m.ceil((len(self.edges)+len(self.bedges)+len(self.nodes))/(self.disk_cap-2))
        for p in range(0,n_rounds):
            t=self.write_file(i,j,k,self.disk_cap,ind_node)
            i=t[0]
            j=t[1]
            k=t[2]
            self.overflow=self.overflow+1

class GridBoard():
    def __init__(self,k1,b1):
        self.node_index=[]
        self.grid_list=[]
        self.xmax=0
        self.xmin=0
        self.ymax=0
        self.ymin=0
        self.disk_cap=b1
        self.grid_size=k1
        self.max_hgrid=0
        self.max_vgrid=0
    def get_max_min(self):
        fh=open("snodes.txt","r")
        line1=fh.readline().split()
        min_x=float(line1[1])
        max_x=float(line1[1])
        min_y=float(line1[2])
        max_y=float(line1[2])
        temp_node=[]
        temp_node.append(min_x)
        temp_node.append(min_y)
        self.node_index.append(temp_node)
        count=1
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
                self.node_index.append(temp_node)
                if(temp_x<min_x):
                    min_x=temp_x
                if(temp_x>max_x):
                    max_x=temp_x
                if(temp_y<min_y):
                    min_y=temp_y
                if(temp_y>max_y):
                    max_y=temp_y
            
        fh.close()
        self.xmax=max_x
        self.xmin=min_x
        self.ymax=max_y
        self.ymin=min_y
        #creating empty grids in gridboard
        self.max_hgrid=m.ceil((self.xmax-self.xmin)/self.grid_size)
        self.max_vgrid=m.ceil((self.ymax-self.ymin)/self.grid_size)
        #print(self.max_hgrid)
        #print(self.max_vgrid)
        counter=0
        i=0
        temp_1=self.ymin
        while(i<self.max_vgrid):
            j=0
            temp_2=self.xmin
            while(j<self.max_hgrid):
                tgrid=Grid(counter,k,b,temp_2,temp_2+k,temp_1,temp_1+k)
                self.grid_list.append(tgrid)
                #tgrid.inf()
                counter=counter+1
                temp_2=temp_2+k
                j=j+1
            temp_1=temp_1+k
            i=i+1
        #print("No of grids")
        #print(len(self.grid_list))
    def metadata(self):
        fh=open("metadata.txt","w")
        fh.write(str(self.xmin)+"\n")
        fh.write(str(self.xmax)+"\n")
        fh.write(str(self.ymin)+"\n")
        fh.write(str(self.ymax)+"\n")
        fh.write(str(self.grid_size)+"\n")
        fh.write(str(len(self.node_index))+"\n")
        
        fh.close()
    def get_grid_no(self,x,y):
        x_no=(x-self.xmin)//self.grid_size
        y_no=(y-self.ymin)//self.grid_size
        grid_no=self.max_hgrid*y_no+x_no
        return int(grid_no)
    def add_nodes_to_grid(self):
        fh=open("snodes.txt","r")
        count=1
        while(count==1):
            line=fh.readline()
            if(line==''):
                count=0
                break
            else:
                n_id=int(line.split()[0])
                temp_x=float(line.split()[1])
                temp_y=float(line.split()[2])
                gno=self.get_grid_no(temp_x,temp_y)
                self.grid_list[gno].add_node(n_id)
        fh.close()
    def add_edges_to_grid(self):
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
                gno1=self.get_grid_no(self.node_index[n1_id][0],self.node_index[n1_id][1])
                gno2=self.get_grid_no(self.node_index[n2_id][0],self.node_index[n2_id][1])
                #self.grid_list[gno].add_node(n_id)
                if(gno1==gno2):
                    #check whether edge exists in the edge list of grid
                    status=self.grid_list[gno1].check_edge(n1_id,n2_id,wt)
                    if(status==0):
                        self.grid_list[gno1].add_edge(n1_id,n2_id,wt)
                        
                        
                else:
                    status1=self.grid_list[gno1].check_bedge(n1_id,n2_id,wt)
                    status2=self.grid_list[gno2].check_edge(n1_id,n2_id,wt)
                    #check whether edge exits in boundary list of two grids
                    if(status1==0):
                        self.grid_list[gno1].add_bedge(n1_id,n2_id,wt)
                    if(status2==0):
                        self.grid_list[gno2].add_bedge(n1_id,n2_id,wt)

                
        fh.close()
    def print_grids(self):
        index_node=self.node_index
        for i in range (0,len(self.grid_list)):
            if(len(self.grid_list[i].nodes)!=0):
                self.grid_list[i].write_grid(index_node)
            
        
        
        
        
    def print_max_min(self):
        print("xmin = ",self.xmin)
        print("ymin = ",self.ymin)
        print("xmax = ",self.xmax)
        print("ymax = ",self.ymax)
    
        
    
        
b1=GridBoard(k,b)
b1.get_max_min()
b1.add_nodes_to_grid()
b1.add_edges_to_grid()
b1.print_grids()
b1.metadata()     

                
                
