# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random


def generate_graph(num):
    graph = {}
    for i in range(0, num):
        neighbours = []
        for j in range(random.randint(0, num//2), random.randint(num//2, num)):
            if i != j:
                neighbours.append(j)
        graph.update({i: neighbours})
    return graph


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited)
    return visited


g = generate_graph(6)
visited = dfs(g, 1, [])
print(g)
print(visited)

