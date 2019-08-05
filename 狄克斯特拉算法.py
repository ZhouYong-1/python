graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
costs = {}
costs["a"] = 6
costs["b"] = 2
parents["a"] = "start"
parents["b"]  ="start"
processed = []

node = dind_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbo