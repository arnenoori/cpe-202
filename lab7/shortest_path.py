import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    # if vertex is less than vertex, vertex.distance

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def addVertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.addVertex(frm)
        if to not in self.vert_dict:
            self.addVertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    # make shortest path from previous
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

# Kevin Bacon List portion

def bacon_degree(self, actor):
    """Takes an actor name and returns the shortest path to Kevin Bacon"""
    table = self.shortest(self.adjacent['Kevin Bacon'])
    return table[actor][0]


def bacon_actors_with_degree(self, n):
    """Returns all actors with degree n to Kevin Bacon"""
    table = self.shortest(self.adjacent['Kevin Bacon'])
    actors = []
    for i in table:
        if table[i][1] == n:
            actors.append(i)
    return actors


def highest_bacon(self):
    """Returns the actor(s) with the highest Bacon degree"""
    table = self.shortest(self.adjacent['Kevin Bacon'])
    actors = []
    max1 = 0
    for i in table:
        if table[i][1] > max1:
            max1 = table[i][1]
            actors = []
        if table[i][1] == max1:
            actors.append(i)
            return actors


def any_actors_degree(self, actor1, actor2):
    """A more general function to return the path length between any two actors"""
    table = self.shortest(self.adjacent[actor1])
    return table[actor2][1]


if __name__ == '__main__':

    g = Graph()

    g.addVertex('Kevin Bacon')
    g.addVertex('Tom Hanks')
    g.addVertex('Bill Paxton')
    g.addVertex('Paul Herbert')
    g.addVertex('Yves Aubert')
    g.addVertex('Shane Zaza')
    g.addVertex('Seretta Wilson')
    g.addVertex('Meryl Streep')
    g.addVertex('John Beluci')
    g.addVertex('Kathleen Quinlan')
    g.addVertex('Donald Sutherland')
    g.addVertex('Lloyd Bridges')
    g.addVertex('Grace Kelly')
    g.addVertex('Nicole Kidman')
    g.addVertex('Patrick Allen')
    g.addVertex('Glenn Close')
    g.addVertex('John Gielgud')
    g.addVertex('Vernon Dobtcheff')
    g.addVertex('Kate Winslet')

    g.add_edge('Kevin Bacon', 'Tom Hanks')
    g.add_edge('Kevin Bacon', 'John Beluci')
    g.add_edge('Kevin Bacon', 'Meryl Streep')
    g.add_edge('Kevin Bacon', 'Donald Sutherland')
    g.add_edge('Kevin Bacon', 'Bill Paxton')
    g.add_edge('Kevin Bacon', 'Kathleen Quinlan')
    g.add_edge('Tom Hanks', 'Kathleen Quinlan')
    g.add_edge('Tom Hanks', 'Bill Paxton')
    g.add_edge('Tom Hanks', 'Paul Herbert')
    g.add_edge('Tom Hanks', 'Yves Aubert')
    g.add_edge('Tom Hanks', 'Shane Zaza')
    g.add_edge('Tom Hanks', 'Seretta Wilson')
    g.add_edge('Tom Hanks', 'Lloyd Bridges')
    g.add_edge('Lloyd Bridges', 'Grace Kelly')
    g.add_edge('Donald Sutherland', 'Patrick Allen')
    g.add_edge('Donald Sutherland', 'Nicole Kidman')
    g.add_edge('Donald Sutherland', 'Vernon Dobtcheff')
    g.add_edge('Nicole Kidman', 'Glenn Close')
    g.add_edge('Nicole Kidman', 'John Gielgud')
    g.add_edge('Bill Paxton', 'Kate Winslet')
    g.add_edge('Patrick Allen', 'John Gielgud')
    g.add_edge('Nicole Kidman', 'John Gielgud')
    g.add_edge('Vernon Dobtcheff', 'John Gielgud')

    print('The Kevin Bacon Universe:')
    # Printing Vertex
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('(%s, %s)' % (vid, wid))

    # Printing Edges
    for v in g:
        print('Actor: %s is to %s' % (v.get_id(), g.vert_dict[v.get_id()]))

    # target = g.get_vertex('actor name here')
    # path = [target.get_id()]
    # shortest(target, path)

'''
How to do:
add variable to Vertex class to mark as visits, checking edges

two lists, visited & unvisited

breadth first is easier

Textbook Reference:

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]
'''
