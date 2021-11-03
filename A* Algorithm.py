def aStarAlgo(start_node, stop_node):  # find's shortest dist between start_node and stop_node
    open_set = set(start_node)         # "Open set" is set of nodes from which we can choose current node or (best node)
    closed_set = set()                 # set of nodes already evaluated.
    g = {}                             # (gScore): store actual distance from starting node
    parents = {}                       # mapping of parent child node
    g[start_node] = 0                  # distance of starting node from itself is zero
    parents[start_node] = start_node   # initially, parent of start node is start node itself

    while len(open_set) > 0:                                            # loop till we have node in open set to explore
        n = None                                                        # n is current node with best path

        for v in open_set:                                              # select node with lowest fScore as current node
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):  # For node n, fScore[n] = gScore[n] + h(n)
                n = v                                                   # node with lowest f() is found

        if n == stop_node or Graph_nodes[n] == None:                    # if n is stop node then don't find its neighbour
            pass                                                        # don't go to else part
        else:
            for (m, weight) in get_neighbors(n):                        # find neighbour of current node

                if m not in open_set and m not in closed_set:           # if neighbour is unexplored then add to openSet
                    open_set.add(m)
                    parents[m] = n                                      # make current node as its parent
                    g[m] = g[n] + weight                                # calculate gScore of neighbour

                else:                                   # for each node m,compare its distance from start
                    if g[m] > g[n] + weight:            # i.e g(m) to the from start through n node
                        g[m] = g[n] + weight            # #update g(m)
                        parents[m] = n                  # #change parent of m to n

                        if m in closed_set:             # if m in closed set,remove and add to open
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:                                   # if still n is none then no path exist to stop_node
            print('Path does not exist!')
            return None

        if n == stop_node:                              # if the current node is the stop_node
            path = []                                   # add answer to path array

            while parents[n] != n:                      # untill parent of node is node itself add it to path array
                path.append(n)                          # append current node then
                n = parents[n]                          # make parent of current node as current node and repeat this

            path.append(start_node)                     # finally add start node to path
            path.reverse()                              # reverse path array to give answer in ascending order
            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)                              # remove n from the open_list, and add it to closed_list
        closed_set.add(n)                               # because all of his neighbors were inspected

    print('Path does not exist!')                       # If open_set is empty then no path exist
    return None


def get_neighbors(v):                          # return array of neighbour and its distance from the passed node
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):                              # it gives approx distance from current node to stop_node
    H_dist = {
        'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
    }
    return H_dist[n]


Graph_nodes = {                               # adjacency matrix of all node with gScore
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}
aStarAlgo('A', 'J')                          # call aStar algorithm to find shortest path between start and stop node.
