import pytest

from lab4.graph.exceptions import *
from lab4.graph.Iterators.BidirIterator import BidirIterator
from lab4.graph.Iterators.ConstBidirIterator import ConstBidirIterator


def test_init(graph, vertices, edges):
    graph._get_edges()
    graph._get_vertices()

    assert graph._vertices == vertices
    assert graph._edges == edges


def test_check_for_edge(graph):
    edge_for_error = (1, 4)
    edge_for_pass = (4, 2)
    graph._get_edges()

    assert graph.check_for_edge(edge_for_pass)
    assert not graph.check_for_edge(edge_for_error)


def test_check_for_vertex(graph):
    pass_vertex = 2
    error_vertex = 6
    graph._get_vertices()

    assert graph.check_for_vertex(pass_vertex)
    assert not graph.check_for_vertex(error_vertex)


def test_get_vertex_degree_in(graph):
    graph._get_vertices()       
    degree = graph.get_vertex_degree_in(3)
    assert degree == 1
    
def test_get_vertex_degree_in_fail(graph):
    graph._get_vertices()
    with pytest.raises(NotVertexError):
        degree = graph.get_vertex_degree_in(7)

def test_get_edge_degree_fail(graph):
    graph._get_edges()
    with pytest.raises(NotEdgeError):
        graph.get_edge_degree((10,11))

def test_get_vertex_degree_out(graph):
    graph._get_vertices()
    assert graph.get_vertex_degree_out(1) == 2


def test_clear(graph):
    graph._get_edges()
    graph._get_vertices()

    graph.clear()

    assert graph._edges == []
    assert graph._vertices == []


def test_get_edge_degree(graph):
    graph._get_edges()

    assert graph.get_edge_degree((1, 3)) == 1
    
def test_iterator_for_vertices(graph):
    graph._get_vertices()
    
    iterator = graph.iterator_for_vertices()
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert iterator.prev() == 1
    
def test_iterator_for_edges(graph):
    graph._get_edges()
    
    iterator = graph.iterator_for_edges()
    assert next(iterator) == (1,2)
    assert next(iterator) == (1,3)
    assert iterator.prev() == (1,2)
    
def test_reverse_iterator_for_vertices(graph):
    graph._get_vertices()
    
    iterator = graph.reverse_iterator_for_vertices()
    assert next(iterator) == 5
    assert next(iterator) == 4
    assert iterator.prev() == 5
    
def test_const_iterator_for_vertices(graph):
    graph._get_vertices()
    
    iterator = graph.const_iterator_for_vertices()
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert iterator.prev() == 1
    assert next(iterator) == 2
    assert iterator.peek_next() == 3
    assert iterator.peek_prev() == 1
    assert iterator.current() == 2
    
def test_const_iterator_for_vertices_with_stop(graph):
    graph._get_vertices()
    
    iterator = graph.const_iterator_for_vertices()
    assert next(iterator) == 1
    with pytest.raises(StopIteration):
        assert iterator.prev()

    
def test_const_reverse_iterator_for_vertices(graph):
    graph._get_vertices()
    
    iterator = graph.conts_reverse_iterator_for_vertices()
    assert next(iterator) == 5
    assert next(iterator) == 4
    assert iterator.prev() == 5
    assert next(iterator) == 4
    assert iterator.peek_next() == 3
    assert iterator.current() == 4
    assert iterator.peek_prev() == 5
    assert iterator.current() == 4
    
def test_get_adjacency_vertices(graph):
    graph._get_vertices()

    assert graph.get_adjacency_vertices(1) == [2,3,5]
    
def test_iterator_for_adjacency_vertices(graph):
    graph._get_vertices()
    
    iterator = graph.iterator_for_adjacency_vertices(1)
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 5
    assert iterator.prev() == 3
    
def test_get_incident_edges(graph):
    graph._get_vertices()
    graph._get_edges()
    
    assert graph.get_incident_edges(1) == [(1,2), (1,3), (5,1)]

def test_iterator_for_incident_edges(graph):
    graph._get_vertices()
    graph._get_edges()
    
    iterator = graph.iterator_for_incident_edges(1)
    
    assert next(iterator) == (1,2)
    assert next(iterator) == (1,3)
    assert iterator.prev() == (1,2)