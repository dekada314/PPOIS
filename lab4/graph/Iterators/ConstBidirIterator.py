class ConstBidirIterator:
    def __init__(self, elements, reverse=False):
        self._elements = tuple(elements)
        self._position = len(self._elements) if reverse else -1
        self._reverse = reverse

    def __iter__(self):
        return self

    def __next__(self):
        if not self._reverse:
            if self._position + 1 >= len(self._elements):
                raise StopIteration
            self._position += 1
            return self._elements[self._position]
        else:  # noqa RET505
            if self._position <= 0:
                raise StopIteration
            self._position -= 1
            return self._elements[self._position]

    def prev(self):
        if not self._reverse:
            if self._position <= 0:
                raise StopIteration
            self._position -= 1
            return self._elements[self._position]

        else:  # noqa RET505
            if self._position + 1 >= len(self._elements):
                raise StopIteration
            self._position += 1
            return self._elements[self._position]

    def peek_next(self):
        if not self._reverse:
            if self._position + 1 >= len(self._elements):
                raise StopIteration
            return self._elements[self._position + 1]
        else:  # noqa RET505
            if self._position <= 0:
                raise StopIteration
            return self._elements[self._position - 1]

    def peek_prev(self):
        if not self._reverse:
            if self._position <= 0:
                raise StopIteration
            return self._elements[self._position - 1]

        else:  # noqa RET505
            if self._position + 1 >= len(self._elements):
                raise StopIteration
            return self._elements[self._position + 1]
        
    def current(self):
        return self._elements[self._position]
