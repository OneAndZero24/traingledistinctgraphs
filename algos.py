from typing import Optional

from graph import Graph


def check_traingle_distinct(graph: Graph) -> bool:
    """
    Checks if given graph is traingle-distinct\\
    O(N^3)
    """
    R = True
    tdegs = set()

    for i in range(len(graph)):
        tdeg = graph.get_traingle_degree(i)
        if tdeg in tdegs:
            R = False
            break
        tdegs.add(tdeg)
    return R

def construct(N: int) -> Optional[Graph]:
    """
    Constructs triangle-distinct graph of given size\\
    Returns None for N < 7\\
    O(N^2)
    """
    if N < 7:
        return None
    elif N == 7:
        return Graph.G7()
    else:
        graph = Graph.G7()
        k = 5
        for i in range(8, N+1):
            if i % 2 == 0:  # G_n+1
                j = graph.append_vertex()
                graph.add_edge(k, j)
                k = j
            else:   # G_n+2
                graph.prepend_vertex()
                for j in range(1, len(graph)):
                    graph.add_edge(0, j)
        return graph

    