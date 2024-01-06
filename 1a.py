import json
from copy import deepcopy
f=open('level1a.json')
data=json.load(f)

neighbour_dist=[]
order=[]
for k in range(20):
    row=[];j=0
    for i in data['neighbourhoods'][f'n{k}']['distances']:
        row.append([i,j]);j+=1
    neighbour_dist.append(row)
    #print(data['neighbourhoods'][f'n{k}']["order_quantity"])
    order.append(int(data['neighbourhoods'][f'n{k}']["order_quantity"]))
res=[]
j=0
for i in data['restaurants']['r0']['neighbourhood_distance']:
    res.append([i,j])
    j+=1
#print(res)    
j=0
for i in range(len(res)):
    neighbour_dist[i].append([res[i][0],j])
    j+=1
neighbour_dist.extend([res])
neighbour_dist[20].append([0,20])
new=deepcopy(neighbour_dist)

cap=data["vehicles"]["v0"]["capacity"]

completed=[0 for i in range(21)]
completed[20]=1
a=new[20]
a.sort(key=lambda x:x[0])
last=20
paths=[]
path=["r0"]
capacity=int(cap)
k=0
while not all(completed):
    if k:
        b=k
        k=0
    else:    
        b=a.pop(0)
        
    #print(a,b)    
    if not completed[b[1]]:
        if order[b[1]]<=capacity:

            capacity-=order[b[1]]
            completed[b[1]]=1
            path.append("n"+str(b[1]))
        else:
            order[b[1]]-=capacity
            capacity=0    
            k=b
        if capacity==0:
            path.append("r0")
            paths.append(path)
            path=["r0"]
            capacity=int(cap)
            a=new[20]
            a.sort(key=lambda x:x[0])

        else:
            a=new[b[1]]
            #print(a)
            a.sort(key=lambda x:x[0])
    
if path!=[]:
    path.append("r0")
paths.append(path)    
print(paths)
d={}
for i in range(len(paths)):
    d[f"path{i+1}"]=paths[i]
a={"v0":d}
f =open('level1a_output.json',"w")

json.dump(a,f)