import networkx as nx
from pulp import LpProblem, LpVariable, LpMinimize

def optimize_route(locations):
    G = nx.Graph()
    for loc in locations:
        G.add_edge(loc[0], loc[1], weight=loc[2])
    source, destination = locations[0][0], locations[-1][1]
    path = nx.shortest_path(G, source=source, target=destination, weight='weight')
    distance = nx.shortest_path_length(G, source=source, target=destination, weight='weight')
    return path, distance

def vehicle_routing():
    problem = LpProblem("VehicleRouting", LpMinimize)
    x1 = LpVariable("Route1", 0, 1, cat="Binary")
    x2 = LpVariable("Route2", 0, 1, cat="Binary")
    problem += 10 * x1 + 15 * x2, "Minimize Costs"
    problem += x1 + x2 == 1, "One route must be selected"
    problem.solve()
    return {var.name: var.varValue for var in problem.variables()}
