from typing import List

import graphviz


class Graph:
    """
    Represents simple, undirected graph as incidency matrix\\
    Initializes with one vertex without neighbours
    """

    def __init__(self, matrix: List[List[bool]] = [[False]]):
        self.N = len(matrix)
        self.matrix = matrix

    @classmethod
    def G7(cls):
        """
        Smallest traingle distinct graph\\
        O(1)
        """
        matrix = [
            [False, True, True, True, True, True, True],
            [True, False, True, True, True, True, False],
            [True, True, False, True, False, True, True],
            [True, True, True, False, True, False, False],
            [True, True, False, True, False, False, True],
            [True, True, True, False, False, False, False],
            [True, False, True, False, True, False, False]
        ]
        return cls(matrix)

    def __len__(self):
        """
        Returns number of vertices\\
        O(1)
        """
        return self.N

    def __str__(self) -> str:
        """
        Converts to DOT format string\\
        O(N^2)
        """
        dot = graphviz.Graph()
        for i in range(self.N):
            dot.node(f'{i}', f'v{i}')  

        for i in range(self.N):
            neighbours = self.get_neighbours(i)
            dot.edges(map(lambda x: str(i)+str(x), neighbours))

        return 'strict '+dot.source

    def to_image(self, path: str, filename: str) -> None:
        """
        Renders to PNG at given path\\
        O(N^2)
        """
        src = graphviz.Source(str(self), format='png')
        src.render(path+filename+'png')

    def prepend_vertex(self) -> None:
        """
        Moves all verticies indexes by one, adds new one with id=0\\
        O(N)
        """
        for l in self.matrix:
            l.insert(0, [])
        
        self.N += 1
        self.matrix.insert(0, [False]*self.N)

    def append_vertex(self) -> int:
        """
        Adds vertex with biggest index, returns it\\
        O(N)
        """
        for l in self.matrix:
            l.append([])
        
        self.N += 1
        self.matrix.append([False]*self.N)
        return self.N-1

    def add_edge(self, i: int, j: int) -> None:
        """
        Adds edge between vertices at index i and j\\
        O(1)
        """
        self.matrix[i][j] = True
        self.matrix[j][i] = True

    def get_neighbours(self, i: int) -> List[int]:
        """
        Returns list of neighbour indicies\\
        O(N)
        """
        return  [ j for j, x in enumerate(self.matrix[i]) if x == True ]

    def get_degree(self, i: int) -> int:
        """
        Returns degree of given vertex\\
        O(N)
        """
        return len(self.get_neighbours(i))
    
    def get_traingle_degree(self, i: int) -> int:
        """
        Returns triangle degree of given vertex\\
        O(N^2)
        """
        neighbours = self.get_neighbours(i)
        sub_matrix = [ self.matrix[x] for x in neighbours ]
        for i, l in enumerate(sub_matrix):
            sub_matrix[i] = [ l[x] for x in neighbours ]
        sub_graph = Graph(sub_matrix)
        return sum(map(sub_graph.get_degree, list(range(len(sub_graph)))))//2
