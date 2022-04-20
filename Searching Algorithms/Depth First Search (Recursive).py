# Using a Python dictionary to act as an adjacency list
'''The illustrated graph is represented using
an adjacency list - an easy way to do it in Python
is to use a dictionary data structure.
Each vertex has a list of its adjacent nodes stored.'''
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

# visited is a set that is used to keep track of visited nodes.
visited = set()

'''dfs follows the algorithm described:
1. It first checks if the current node is unvisited - if yes, it is appended in the visited set.
2. Then for each neighbor of the current node, the dfs function is invoked again.
3. The base case is invoked when all the nodes are visited. The function then returns.'''

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# Driver Code
'''The dfs function is called and is passed the visited set,
the graph in the form of a dictionary, and A, 
which is the starting node (root node).'''
dfs(visited, graph, 'A')