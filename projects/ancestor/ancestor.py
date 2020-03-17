from util import Stack, Queue  # These may come in handy

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
            raise ValueError('vertex does not exist')


        # loop

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        q = Queue()
        # enqueue A PATH to the starting vertex
        q.enqueue([starting_vertex])
        # create set to store visited vertices
        v = set()
        # while queue is not empty,
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            # grab vertex from the end of the path
            last_vertex = path[-1]
            # check if it's been visited, if not
            if not last_vertex in v:
                # mark it as visited
                v.add(last_vertex)
                # check if it's the target
                if last_vertex == destination_vertex:
                    return path
                    # if so, return the path
                    # enequeue a path to all its neighbors
                    # make a copy of the path
                    # enqeue the copy
                for n in self.get_neighbors(last_vertex): 
                    copy = path.copy()            
                    if not n in copy:
                        copy.append(n)
                    q.enqueue(copy)
                    

def earliest_ancestor(ancestors, starting_node):
    # create graph from child/parent pairs
    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0])
    
    q = Queue()
    q.enqueue([starting_node])
    last_vertex = -1

    while q.size() > 0:
        path = q.dequeue()

        # if something
        v = path[-1]

        if (v < last_vertex) or len(path) > 1:
            last_vertex = v

        for n in g.get_neighbors(v):
            copy = path.copy()
            copy.append(n)
            q.enqueue(copy)

    return last_vertex



        

ancestor_list = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestor_list, 4))




    # return -1 if no parent
    # if tied ancestor, return the one w the lower value


