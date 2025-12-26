# Implementation of an undirected graph using Adjacency Matrix

class Vertex:
    def __init__(self, name):
        self.name = name


class Graph:
    def __init__(self):
        self.vertices = {}        # vertex_name -> Vertex
        self.edges = []           # adjacency matrix
        self.edge_indices = {}    # vertex_name -> index

    def add_vertex(self, vertex):
        # Validate input
        if not isinstance(vertex, Vertex):
            return False

        if vertex.name in self.vertices:
            return False

        # 1. Add vertex
        self.vertices[vertex.name] = vertex

        # 2. Expand existing rows (add new column)
        for row in self.edges:
            row.append(0)

        # 3. Add new row initialized with zeros
        self.edges.append([0] * (len(self.edges) + 1))

        # 4. Assign index to vertex
        self.edge_indices[vertex.name] = len(self.edge_indices)

        return True

    def add_edge(self, u, v, weight=1):
        if u not in self.vertices or v not in self.vertices:
            return False

        i = self.edge_indices[u]
        j = self.edge_indices[v]

        # Undirected graph
        self.edges[i][j] = weight
        self.edges[j][i] = weight

        return True

    def print_graph(self):
        for vertex, i in sorted(self.edge_indices.items()):
            print(vertex, end=" ")
            for value in self.edges[i]:
                print(value, end=" ")
            print()
 

g = Graph()

# Add vertices
for ch in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(ch)))

# Add edges
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH',
         'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[0], edge[1])

# Print graph
g.print_graph()

