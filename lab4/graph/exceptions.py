class NotEdgeError(Exception):
    """Ребра не существует"""


class AlrExistEdgeError(Exception):
    """Такое ребро уже есть"""


class NotVertexError(Exception):
    """Вершины не существует"""


class AlrExistVertexError(Exception):
    """Такая вершина уже есть"""


class EmptyAdjListError(Exception):
    """Списка смежности не существует"""
