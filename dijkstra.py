from heapdict import heapdict
from collections import defaultdict
import time

def shortest(n, graph):

    if graph == []:
        return None
    neigh = defaultdict(list)
    path_back = {}
    edge = {}
    weight = heapdict()

    for i, j, k in graph:
        edge[i,j] = k
        neigh[i].append(j)
        neigh[j].append(i)
        weight[i] = float('inf')
        weight[j] = float("inf")
    weight[0] = 0

    def _shortest():
        num_to_visit = len(neigh[n-1])-1

        while len(weight) != 1:

            curr_node, curr_weight = weight.popitem()
            if curr_node == n-1:
                if num_to_visit <= 0:
                    return curr_weight

            for neigh_node in neigh[curr_node]:
                if neigh_node == n-1:
                    num_to_visit = num_to_visit - 1
                if weight.get(neigh_node, "") != "":
                    try:
                        if weight[neigh_node] > edge[curr_node, neigh_node] + curr_weight:
                            weight[neigh_node] = edge[curr_node, neigh_node] + curr_weight
                            path_back[neigh_node] = curr_node
                    except KeyError:
                        if weight[neigh_node] > edge[neigh_node, curr_node] + curr_weight:
                            weight[neigh_node] = edge[neigh_node, curr_node] + curr_weight
                            path_back[neigh_node] = curr_node

        return weight[n-1]

    shortest_weight = _shortest()
    path = []
    x = n-1
    path.append(x)
    try:
        while x != 0:
            path.append(path_back[x])
            x = path_back[x]
        path.reverse()
        return shortest_weight, path
    except KeyError:
        return None
