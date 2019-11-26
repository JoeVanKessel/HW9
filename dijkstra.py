from heapdict import heapdict
from collections import defaultdict
import time

def shortest(n, graph):
    #start_time = time.time()
    if graph == []:
        return None
    neigh = defaultdict(list)
    #path_to = defaultdict(list)
    path_back = {}
    edge = {}
    weight = heapdict()

    for i, j, k in graph:
        edge[i,j] = k
        neigh[i].append(j)
        neigh[j].append(i)
        #if i == 0:
        #    if weight.get(i, "") == "":
        #        weight[i] = 0
        #        path_to[i].append(i)
        #else:
        #path_to[i] = []
            #if path_to.get(j, "") == "":
        #path_to[j] = []
        weight[i] = float('inf')
        weight[j] = float("inf")

    #path_to[0].append(0)
    weight[0] = 0

    #print("--- %s seconds to setup---" % (time.time() - start_time))
    #print("edge dict below")
    #print(edge)
    #print("path_to dict below")
    #for a in path_to:
    #    print(a, path_to[a])
    #print("weight dict below")
    #for a in weight:
    #    print(a, weight[a])


    def _shortest():
        new_weight = float('inf')
        i = 0;
        #print(neigh[n-1])
        num_to_visit = len(neigh[n-1])-1

        #print(len(weight))
        #print("neigh dict below")
        #for a in neigh:
            #print(a, neigh[a])
        while len(weight) != 1:

            curr_node, curr_weight = weight.popitem()
            if curr_node == n-1:
                if num_to_visit <= 0:
                    return curr_weight

            for neigh_node in neigh[curr_node]:

                if neigh_node == n-1:
                    #print("Before -- Current Node: ", curr_node, "Current Weight: ", curr_weight, "Weight Neighbor: ", weight[neigh_node])
                    num_to_visit = num_to_visit - 1
                if weight.get(neigh_node, "") != "":
                    #print("neighbor node: ", neigh_node)
                    #print("edge: ", curr_node, neigh_node)
                    try:
                        if weight[neigh_node] > edge[curr_node, neigh_node] + curr_weight:
                            weight[neigh_node] = edge[curr_node, neigh_node] + curr_weight
                            #path_to[neigh_node] = path_to[curr_node] + [neigh_node]
                            path_back[neigh_node] = curr_node
                            #print("Current Node: ", curr_node, "Path to Neighbor: ", path_to[neigh_node], "Weigth Current :", curr_weight, "Weight Next :", weight[neigh_node])#"Current Node: ", curr_node, "Path to current: ", path_to[curr_node])
                            #print("Path Back (Node : Weight to)", path_back)
                            #if neigh_node == n-1:
                                #print("After -- Current Node: ", curr_node, "Weight Neighbor: ", weight[neigh_node])


                    except KeyError:
                        if weight[neigh_node] > edge[neigh_node, curr_node] + curr_weight:
                            weight[neigh_node] = edge[neigh_node, curr_node] + curr_weight
                            #path_to[neigh_node] = path_to[curr_node] + [neigh_node]
                            path_back[neigh_node] = curr_node
                            #print("Current Node: ", curr_node, "Path to Neighbor: ", path_to[neigh_node], "Weigth Current :", curr_weight, "Weight Next :", weight[neigh_node])#"Current Node: ", curr_node, "Path to current: ", path_to[curr_node])
                            #print("Path Back (Node : Weight to)", path_back)
                            #if neigh_node == n-1:
                                #print("After -- Current Node: ", curr_node, "Weight Neighbor: ", weight[neigh_node])

            #print(len(weight), curr_node, curr_weight)


        #short_path = []
        return weight[n-1]
        #while x != n-1:
            #short_path.append(path_back[x])
            #x =

        #print("--- %s seconds for alg---" % (time.time() - start_time))
        #return new_weight

    #for a in _shortest():
        #least_weigth = a


    shortest_weight = _shortest()
    #return shortest_weight, path_to[n-1]
    #print("path_to dict below")
    #for a in path_to:


    #print(path)
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
