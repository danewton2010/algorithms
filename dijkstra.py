#! /usr/bin/env python
#  coding: utf-8 

def find_min_cost(cost_dict):
    min_cost = float("inf")
    min_cost_node = None

    for node in cost_dict:
        cost = cost_dict[node]
        if cost < min_cost and node not in used:
            min_cost = cost
            min_cost_node = node

    return min_cost_node


def dijkstra(graph):
    node = find_min_cost(costs)
    while node is not None:
        cost = costs[node]
        neigh = graph[node]

        for n in neigh.keys():
            if costs[n] > cost + neigh[n]:
                costs[n] = cost + neigh[n]
                parent[n] = node
        used.append(node)
        node = find_min_cost(costs)


# init costs and parent dict
def init(grap):
    costs = {}
    parent = {}

    # find grap's keys and init
    for i in grap.keys():
        costs[i] = float("inf")
        parent[i] = None

    for k, v in grap["begin"].items():
        costs[k] = v
        parent[k] = "begin"

    del costs["begin"]

    return costs, parent


if __name__ == '__main__':
    used = []

    grap = {}
    grap["begin"] = {}
    grap["begin"]['a'] = 6
    grap["begin"]['b'] = 2
    grap["a"] = {}
    grap["a"]["end"] = 1
    grap["b"] = {}
    grap["b"]["a"] = 3
    grap["b"]["end"] = 5
    grap["end"] = {}

    costs, parent = init(grap)

    dijkstra(grap)
    print(costs)
    print(parent)

    seq=["end"]
    node = parent["end"]
    while node:
       seq.append(node)
       node = parent[node]
    seq.reverse()
    print(' -> '.join(seq))





'''
             a    
           / | \
         6/  |  1
         /   |   \
    begin    3    end
         \   |   /   
          2  |  5
           \ | /
             b

'''
