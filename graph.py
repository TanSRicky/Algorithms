class Graph(object):
    def  __init__(self):
         print("Graph class")
         self.vert_dict = {}
         self.num_vertices = 0

    def add_vertex(self,node):
         new_v = Vertex(node)
         self.vert_dict[node] = new_v
         self.num_vertices = self.num_vertices + 1
    def get_vertex(self,node):
         if node in self.vert_dict:
             return self.vert_dict[node]
         else:
             return None

    def add_edge(self, from_edge, to_edge, weight = 1):
         if from_edge not in self.vert_dict:
                self.add_vertex(from_edge)
         if to_edge not in self.vert_dict:
             self.add_vertex(to_edge)
         self.vert_dict[from_edge].add_neighbor(self.vert_dict[to_edge], weight)
         
    def get_vertices(self):
        return self.vert_dict.keys

    def graph_summary(self):

        for v in self.vert_dict.values():
            for w in v.get_connections():
                v_id = v.get_id()
                w_id = w.get_id()
                print(v_id + ' ' + w_id + ' ' + str(v.get_weight(w)))
class Vertex:
    def __init__(self,node):
         self.id = node
         self.adj = {}

    def add_neighbor(self,neighbor,weight):
        self.adj[neighbor] = weight

    def get_id(self):
        return self.id
    def get_weight(self,neighbor):
        return self.adj[neighbor]
    def get_connections(self):
        return self.adj.keys()
    


g = Graph()
g.add_vertex('A')
g.add_vertex('S')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('S','A',10)
g.add_edge('S','C',2)


g.add_edge('A','B',2)


g.add_edge('S','A',10)

g.graph_summary()



