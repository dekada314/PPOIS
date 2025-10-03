class Matrix:
    def __init__(self, rows = 0, cols = 0, data = None):
        if not data:
            self.rows = rows
            self.cols = cols
            self.data = [[0.0 for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0])
            
    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.rows = len(lines)
            self.cols = len(lines[0].split())
            self.data = [[float(x) for x in line.split()] for line in lines]
            
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def submatrix(self, start_row, start_col, end_row, end_col):
        sub_data = [[self.data[i][j] for i in range(start_col, end_col + 1)] for j in range(start_row, end_row + 1)]
        return Matrix(len(sub_data), len(sub_data[0]), sub_data)
    
    def transpon(self):
        new_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.rows, self.cols = len(new_data), len(new_data[0])
        self.data = new_data
        return self
    
    def resize(self, new_row: int, new_col: int):
        new_data = [row[:new_col] for row in self.data][:new_row]
        self.data = new_data
        return self
    
    def is_square(self):
        return True if self.rows == self.cols else False
    
    def is_diagonal(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != 0 and i != j:
                    return False
        return True
    
    def is_identity(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j and self.data[i][j] != 1.0:
                    return False
                if i != j and self.data[i][j] != 0.0:
                    return False
        return True
    
    def is_zero(self):
        return all(self.data[i][j] == 0 for i in range(self.rows) for j in range(self.cols))
    
    def is_symmetric(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True
    
    def is_upper_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(i):
                if self.data[i][j] != 0.0:
                    return False
        return True

    def is_lower_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != 0.0:
                    return False
        return True 
    
    def pre_inc(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += 1
        return self
    
    def pre_dec(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] -= 1
        return self
    
    def post_inc(self):
        result = Matrix(self.rows, self.cols, [row[:] for row in self.data])
        self.pre_inc()
        return result
    
    def post_dec(self):
        result = Matrix(self.rows, self.cols, [row[:] for row in self.data])
        self.pre_dec()
        return result