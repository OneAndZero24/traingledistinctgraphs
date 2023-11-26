from graph import Graph
from algos import *

print('---TESTS---')

# print('---Graph class---')
# print('1. G7, __str__, to_image')
# g7 = Graph.G7()
# print(str(g7))
# g7.to_image('', 'g7test')

print('2. __init__, append_vertex, prepend_vertex, add_edge, __len__, get_neighbours, get_degree, get_traingle_degree')
g = Graph()
_ = g.append_vertex()
g.add_edge(0, 1)
g.prepend_vertex()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.prepend_vertex()
g.add_edge(0, 3)
print(f'Length: {len(g)}')
print(f'Neighbours of 3: {g.get_neighbours(3)}')
print(f'Degree of 3: {g.get_degree(3)}')
print(f'Triangle degree 0: {g.get_traingle_degree(0)}')
print(f'Triangle degree 3: {g.get_traingle_degree(3)}')
g.to_image('', 'gtest')

print('---Algos---')
print('1. construct 3, 7, 13')
g3 = construct(3)
print(f'Test: {str(g3)}')
g7 = construct(7)
g13 = construct(13)
g13.to_image('', 'g13test')

print('2. check_traingle_distinct g, g7, g13')
print(f'Is traingle-distinct g: {check_traingle_distinct(g)}')
print(f'Is traingle-distinct g7: {check_traingle_distinct(7)}')
print(f'Is traingle-distinct g13: {check_traingle_distinct(13)}')