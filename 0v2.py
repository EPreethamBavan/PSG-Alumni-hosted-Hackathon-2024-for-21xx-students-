import json
from copy import deepcopy
f=open('level0.json')
data=json.load(f)

neighbour_dist=[]
for k in range(20):
    row=[];j=0
    for i in data['neighbourhoods'][f'n{k}']['distances']:
        row.append([i,j]);j+=1
    neighbour_dist.append(row)

res=[]
j=0
for i in data['restaurants']['r0']['neighbourhood_distance']:
    res.append([i,j])
    j+=1
j=0
for i in range(len(res)):
    neighbour_dist[i].append([res[i][0],j])
    j+=1

neighbour_dist.extend([res])
neighbour_dist[20].append([0,20])
new=deepcopy(neighbour_dist)

'''
for i in range(len(new)):
    for j in range(len(new)):
        for k in range(len(new)):
            new[j][k]=min(new[j][k],new[j][i]+new[i][k])
print(new==neighbour_dist)
'''
visited=[0 for i in range(21)]
visited[20]=1
path=""
c=0
from heapq import *
a=[]
for i in neighbour_dist[20]:
    heappush(a,i)
cost=0    
while a and c!=20:
    g=heappop(a)
    if not visited[g[1]]:
        c+=1
        path=path+" "+str(g[1])
        a=[]
        visited[g[1]]=1
        cost+=g[0]
        for i in neighbour_dist[g[1]]:
            if not visited[i[1]]:
                heappush(a,i)

