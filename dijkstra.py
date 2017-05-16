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


# cost dict create
def create_costs(grap):
    costs = {}
    for i in grap.keys():
        costs[i] = float("inf")
    del costs["begin"]

    for k, v in grap["begin"].items():
        costs[k] = v

    return costs


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

    # costs create
    costs = create_costs(grap)

    parent = {}
    parent["a"] = "begin"
    parent["b"] = "begin"
    parent["end"] = None

    dijkstra(grap)
    print(costs)
