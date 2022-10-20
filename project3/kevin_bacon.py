from shortest_path import *

def bacon_degree(g, actor):
    """Takes an actor name and returns the shortest path to Kevin Bacon"""

def bacon_actors_with_degree(g, n):
    """Returns all actors with degree n to Kevin Bacon"""

def highest_bacon(g):
    """Returns the actor(s) with the highest Bacon degroo"""

def any_actors_degree(g, actor1, actor2):
    """A more general function to return the path length between any two actors"""


'''Code to build the example graph:
Note that the add_edge function adds two edges to account for undirected edges. 
add this function to your graph class:'''

def add_edge(self, f, t, weight=1):
    self.addEdge(f, t, weight)
    self.addEdge(t, f, weight)

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

