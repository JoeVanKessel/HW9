from heapdict import heapdict
from collections import defaultdict

def shortest(n, graph):
    neigh = defaultdict(list)
    path_to = defaultdict(list)
    edge = {}
    weight = heapdict()

    for i, j, k in graph:
        edge[i,j] = k
        neigh[i].append(j)

        if i == 0:
            if weight.get(i, "") == "":
                weight[i] = 0
                path_to[i].append(i)
        else:
            path_to[i] = []
            if path_to.get(j, "") == "":
                path_to[j] = []
            weight[i] = float('inf')
            weight[j] = float("inf")

    def _shortest():

        while len(weight) != 1:
            curr_node, curr_weight = weight.popitem()
            for neigh_node in neigh[curr_node]:
                try:
                    if weight[neigh_node] > edge[curr_node, neigh_node] + curr_weight:
                        weight[neigh_node] = edge[curr_node, neigh_node] + curr_weight
                        path_to[neigh_node] = path_to[curr_node] + [neigh_node]
                except KeyError:
                    return None


    _shortest()
    try:
        if weight[n-1] != float("inf") or path_to[n-1] != []:
            return weight[n-1], path_to[n-1]
        else:
            return None
    except KeyError:
        return None
