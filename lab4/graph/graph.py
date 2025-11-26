from copy import deepcopy

from lab4.graph.exceptions import (
    AlrExistEdgeError,
    AlrExistVertexError,
    EmptyAdjListError,
    NotEdgeError,
    NotVertexError,
)
from lab4.graph.Iterators.BidirIterator import BidirIterator
from lab4.graph.Iterators.ConstBidirIterator import ConstBidirIterator

type type_adjancy_list = dict[int : list[int]]
type type_edge = list[tuple[int, int]]


class Graph[T]:
    def __init__(self, adjancy_list) -> None:
        self._adjacency_list: type_adjancy_list = adjancy_list
        self._vertices: list[T] = []
        self._edges: type_edge = []

    def _get_vertices(self) -> list[T]:
        if not self._adjacency_list:
            raise EmptyAdjListError
        self._vertices = list(self._adjacency_list.keys())

    def _get_edges(self) -> type_edge:
        if not self._adjacency_list:
            raise EmptyAdjListError
        for start_vertex, values in self._adjacency_list.items():
            for end_vertex in values:
                self._edges.append((start_vertex, end_vertex))

    def check_for_vertex(self, vertex: T) -> bool:
        return vertex in self._vertices

    def check_for_edge(self, edge: tuple[int, int]) -> bool:
        return edge in self._edges

    def vertices_quantity(self) -> int:
        return len(self._vertices) if self._vertices else None

    def edges_quantity(self) -> int:
        return len(self._edges) if self._edges else None

    def get_vertex_degree_in(self, vertex: T) -> int:
        if self.check_for_vertex(vertex):
            degree = 0
            for values in self._adjacency_list.values():
                if vertex in values:
                    degree += 1
            return degree
        raise NotVertexError

    def get_vertex_degree_out(self, vertex: T) -> int:
        if self.check_for_vertex(vertex):
            return len(self._adjacency_list[vertex])
        raise NotVertexError

    def get_adjacency_vertices(self, vertex: T) -> list:
        adj_vertices = []
        for key, value in self._adjacency_list.items():
            if key == vertex:
                adj_vertices.extend(value)
            elif vertex in value:
                adj_vertices.append(key)
        return sorted(adj_vertices)

    def get_incident_edges(self, vertex: T) -> list:
        return list(filter(lambda edge: vertex in edge, self._edges))

    def get_edge_degree(self, edge: tuple[int, int]) -> int:
        if self.check_for_edge(edge):
            degree = 0
            for value in self._adjacency_list[edge[0]]:
                if value == edge[1]:
                    degree += 1
        else:
            raise NotEdgeError

        return degree

    def add_vertex(self, vertex: T):
        if vertex in self._adjacency_list:
            raise AlrExistVertexError
        self._adjacency_list[vertex] = []
        self._vertices.append(vertex)

    def remove_vertex(self, vertex: T) -> None:
        for key, value in self._adjacency_list.items():
            if vertex == key:
                del self._adjacency_list[key]
            elif vertex in value:
                value.remove(vertex)

    def add_edge(self, edge):
        u, v = edge
        if v in self._adjacency_list[u]:
            raise AlrExistEdgeError

        if not (self.check_for_vertex(u) and self.check_for_vertex(v)):
            raise NotVertexError

        self._adjacency_list[u].append(v)
        self._edges.append(edge)

    def remove_edge(self, edge):
        if self.check_for_edge(edge):
            self._adjacency_list[edge[0]].remove(edge[1])

    def empty(self) -> bool:
        return not (self._adjacency_list and self._vertices and self._edges)

    def clear(self) -> None:
        self._adjacency_list: type_adjancy_list = []
        self._vertices: list[T] = []
        self._edges: type_edge = []

    def __deepcopy__(self, memo=None) -> "Graph":
        new_adjacency_list: type_adjancy_list = deepcopy(self._adjacency_list, memo)
        new_graph = Graph[T](new_adjacency_list)
        new_graph._vertices = deepcopy(self._vertices, memo)
        new_graph._edges = deepcopy(self._edges, memo)

        return new_graph

    def __lt__(self, other: "Graph") -> bool:
        main_sum = len(self._edges)
        other_sum = len(other._edges)
        return main_sum < other_sum

    def __eq__(self, other: "Graph") -> bool:
        return self._adjacency_list == other._adjacency_list

    def __gt__(self, other: "Graph") -> bool:
        main_sum = len(self._edges)
        other_sum = len(other._edges)
        return main_sum > other_sum

    def __del__(self) -> None:
        print(f"Deleted {self.__class__.__name__} object")

    def iterator_for_vertices(self) -> "BidirIterator":
        return BidirIterator(self._vertices)

    def reverse_iterator_for_vertices(self) -> "BidirIterator":
        return BidirIterator(self._vertices, reverse=True)

    def const_iterator_for_vertices(self) -> "BidirIterator":
        return ConstBidirIterator(self._vertices)

    def conts_reverse_iterator_for_vertices(self) -> "ConstBidirIterator":
        return ConstBidirIterator(self._vertices, reverse=True)

    def iterator_for_adjacency_vertices(self, vertex: T) -> "BidirIterator":
        vertices = self.get_adjacency_vertices(vertex)
        return BidirIterator(vertices)

    def reverse_iterator_for_adjacency_verties(self, vertex: T) -> "BidirIterator":
        vertices = self.get_adjacency_vertices(vertex)
        return BidirIterator(vertices, reverse=True)

    def const_iterator_for_adjacency_verties(self, vertex: T) -> "BidirIterator":
        vertices = self.get_adjacency_vertices(vertex)
        return ConstBidirIterator(vertices)

    def const_reverse_iterator_for_adjacency_verties(
        self, vertex: T
    ) -> "ConstBidirIterator":
        vertices = self.get_adjacency_vertices(vertex)
        return ConstBidirIterator(vertices, reverse=True)

    def iterator_for_edges(self) -> "BidirIterator":
        return BidirIterator(self._edges)

    def reverse_iterator_for_edges(self) -> "BidirIterator":
        return BidirIterator(self._edges, reverse=True)

    def const_iterator_for_edges(self) -> "ConstBidirIterator":
        return ConstBidirIterator(self._edges)

    def conts_reverse_iterator_for_edges(self) -> "ConstBidirIterator":
        return ConstBidirIterator(self._edges, reverse=True)

    def iterator_for_incident_edges(self, vertex: T) -> "BidirIterator":
        incid_edges = self.get_incident_edges(vertex)
        return BidirIterator(incid_edges)

    def reverse_iterator_for_incident_edges(self, vertex: T) -> "BidirIterator":
        incid_edges = self.get_incident_edges(vertex)
        return BidirIterator(incid_edges, reverse=True)

    def const_iterator_for_incident_edges(self, vertex: T) -> "ConstBidirIterator":
        incid_edges = self.get_incident_edges(vertex)
        return ConstBidirIterator(incid_edges)

    def const_reverse_iterator_for_incident_edges(
        self, vertex: T
    ) -> "ConstBidirIterator":
        incid_edges = self.get_incident_edges(vertex)
        return ConstBidirIterator(incid_edges, reverse=True)
