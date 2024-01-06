import json
from copy import deepcopy
f=open('level0.json')
data=json.load(f)

neighbour_dist=[]
for k in range(20):
    row=[]
    for i in data['neighbourhoods'][f'n{k}']['distances']:
        row.append(i)
    neighbour_dist.append(row)

res=[]
for i in data['restaurants']['r0']['neighbourhood_distance']:
    res.append(i)

for i in range(len(res)):
    neighbour_dist[i].append(res[i])

neighbour_dist.extend([res])
neighbour_dist[20].append(0)
new=deepcopy(neighbour_dist)

'''
for i in range(len(new)):
    for j in range(len(new)):
        for k in range(len(new)):
            new[j][k]=min(new[j][k],new[j][i]+new[i][k])
print(new==neighbour_dist)
'''

#bruteforce
import itertools

def calculate_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def tsp_solver(distances, start):
    neighborhoods = list(range(len(distances)))
    neighborhoods.remove(start)

    min_distance = float('inf')
    min_path = []

    for perm in itertools.permutations(neighborhoods):
        path = [start] + list(perm) + [start]
        distance = calculate_distance(path, distances)
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance


distances = neighbour_dist

start_neighborhood = 20

path, distance = tsp_solver(distances, start_neighborhood)

print("Optimal Path:", path)
print("Total Distance:", distance)
