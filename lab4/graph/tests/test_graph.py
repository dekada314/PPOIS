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
