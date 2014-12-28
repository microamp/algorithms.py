# -*- coding: utf-8 -*-

"""
Dijkstra's shortest path between two nodes

Links:
* Dijkastra's algorithm: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""


def min_dist_node(nodes, dist, visited):
    try:
        return min(filter(lambda n: n not in visited, nodes),
                   key=lambda n: dist[n])
    except ValueError:
        return None


def shortest_paths(graph, nodes=None, dist=None, prev=None, visited=None):
    node = min_dist_node(nodes, dist, visited)
    if node is None:
        return dist, prev
    else:
        for n in graph[node]:
            new_dist = dist[node] + graph[node][n]
            if n not in dist or new_dist < dist[n]:
                # print("detected new shortest distance to '{0}': {1} "
                #       "(previous node: '{2}')".format(n, new_dist, node))
                dist[n], prev[n] = new_dist, node
        return shortest_paths(graph, nodes={n for n in graph[node]},
                              dist=dist, prev=prev,
                              visited=visited.union({node}))


def dijkstra(graph, source, target):
    def get_path(source, prev, path):
        return (path if path[0] == source else
                get_path(source, prev, [prev[path[0]]] + path))

    dist, prev = shortest_paths(graph, nodes={source},
                                dist={source: 0}, prev={},
                                visited=set())
    return dist[target], get_path(source, prev, [target])
