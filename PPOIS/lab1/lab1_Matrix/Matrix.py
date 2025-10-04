## @brief A class representing a matrix.
# @details This class implements matrix operations such as creation, loading from file, 
# submatrix extraction, transposition, resizing, and checking properties like square, 
# diagonal, identity, zero, symmetric, and triangular matrices.
class Matrix:
    ## @brief Constructs a matrix.
    # @details Creates a matrix with specified rows and columns (filled with zeros) or from provided data.
    # @param rows Number of rows (int, default 0).
    # @param cols Number of columns (int, default 0).
    # @param data 2D list of floats representing the matrix (optional).
    def __init__(self, rows=0, cols=0, data=None):
        if not data:
            self.rows = rows
            self.cols = cols
            self.data = [[0.0 for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0])
        ## @var rows
        # Number of rows in the matrix (int).
        ## @var cols
        # Number of columns in the matrix (int).
        ## @var data
        # 2D list containing matrix elements (floats).

    ## @brief Loads matrix data from a file.
    # @details Reads matrix elements from a text file, where each line represents a row.
    # @param filename Path to the file containing matrix data.
    # @return None
    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.rows = len(lines)
            self.cols = len(lines[0].split())
            self.data = [[float(x) for x in line.split()] for line in lines]

    ## @brief String representation of the matrix.
    # @return A string with matrix rows separated by newlines and elements by spaces.
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    ## @brief Extracts a submatrix.
    # @param start_row Starting row index (inclusive).
    # @param start_col Starting column index (inclusive).
    # @param end_row Ending row index (inclusive).
    # @param end_col Ending column index (inclusive).
    # @return A new Matrix object representing the submatrix.
    def submatrix(self, start_row, start_col, end_row, end_col):
        sub_data = [[self.data[i][j] for j in range(start_col, end_col + 1)] for i in range(start_row, end_row + 1)]
        return Matrix(data=sub_data)

    ## @brief Transposes the matrix in-place.
    # @return Self after transposition.
    def transpon(self):
        new_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.rows, self.cols = self.cols, self.rows
        self.data = new_data
        return self

    ## @brief Resizes the matrix.
    # @param new_row New number of rows.
    # @param new_col New number of columns.
    # @return Self after resizing.
    def resize(self, new_row: int, new_col: int):
        new_data = [row[:new_col] for row in self.data[:new_row]]
        self.data = new_data
        self.rows = new_row
        self.cols = new_col
        return self

    ## @brief Checks if the matrix is square.
    # @return True if the matrix has equal rows and columns, False otherwise.
    def is_square(self):
        return True if self.rows == self.cols else False

    ## @brief Checks if the matrix is diagonal.
    # @return True if the matrix is square and all non-diagonal elements are zero, False otherwise.
    def is_diagonal(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != 0 and i != j:
                    return False
        return True

    ## @brief Checks if the matrix is an identity matrix.
    # @return True if the matrix is square with 1s on the diagonal and 0s elsewhere, False otherwise.
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

    ## @brief Checks if the matrix is zero.
    # @return True if all elements are zero, False otherwise.
    def is_zero(self):
        return all(self.data[i][j] == 0 for i in range(self.rows) for j in range(self.cols))

    ## @brief Checks if the matrix is symmetric.
    # @return True if the matrix is square and symmetric (data[i][j] == data[j][i]), False otherwise.
    def is_symmetric(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True

    ## @brief Checks if the matrix is upper triangular.
    # @return True if the matrix is square and all elements below the diagonal are zero, False otherwise.
    def is_upper_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(i):
                if self.data[i][j] != 0.0:
                    return False
        return True

    ## @brief Checks if the matrix is lower triangular.
    # @return True if the matrix is square and all elements above the diagonal are zero, False otherwise.
    def is_lower_triangular(self):
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != 0.0:
                    return False
        return True

    ## @brief Increments all elements by 1 in-place.
    # @return Self after incrementing.
    def pre_inc(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] += 1
        return self

    ## @brief Decrements all elements by 1 in-place.
    # @return Self after decrementing.
    def pre_dec(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] -= 1
        return self

    ## @brief Returns a copy of the matrix and increments all elements by 1.
    # @return A new Matrix with original values before incrementing.
    def post_inc(self):
        result = Matrix(self.rows, self.cols, [row[:] for row in self.data])
        self.pre_inc()
        return result

    ## @brief Returns a copy of the matrix and decrements all elements by 1.
    # @return A new Matrix with original values before decrementing.
    def post_dec(self):
        result = Matrix(self.rows, self.cols, [row[:] for row in self.data])
        self.pre_dec()
        return result