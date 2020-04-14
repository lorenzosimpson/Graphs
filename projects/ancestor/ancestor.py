
from util import Stack, Queue


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError('vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for tup in ancestors:
        g.add_vertex(tup[0])
        g.add_vertex(tup[1])
        g.add_edge(tup[1], tup[0])
    
    q = Queue()
    q.enqueue([starting_node])
    last_v = -1

    while q.size() > 0:
        path = q.dequeue()
        node = path[-1]

        if node < last_v or len(path) > 1:
            last_v = node
        
        for n in g.get_neighbors(node):
            path_copy = path.copy()
            path_copy.append(n)
            q.enqueue(path_copy)
    
    return last_v

        