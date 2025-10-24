from math import sqrt

## @brief A class representing a 3D vector.
# @details This class implements basic vector operations such as addition, subtraction, 
# scalar multiplication, dot product, angle cosine computation, and length comparisons.
# The vector's length is calculated using the Euclidean formula.
class Vector:
    ## @brief Constructs a 3D vector.
    # @details Creates a vector as the difference between end and begin points.
    # @param end Coordinates of the end point (list of 3 floats).
    # @param begin Coordinates of the start point (list of 3 floats, default [0, 0, 0]).
    def __init__(self, end: list[float], begin=[0, 0, 0]) -> None:
        self.x, self.y, self.z = [float(end[i] - begin[i]) for i in range(3)]
        ## @var x
        # X-component of the vector (float).
        ## @var y
        # Y-component of the vector (float).
        ## @var z
        # Z-component of the vector (float).

    ## @brief String representation of the vector.
    # @return A string in the format 'Vector(x, y, z)'.
    def __str__(self) -> str:
        return f'Vector({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'
    
    ## @brief Adds two vectors.
    # @param other Another Vector object.
    # @return A new Vector representing the sum.
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector([self.x + other.x, self.y + other.y, self.z + other.z])
    
    ## @brief In-place addition of two vectors.
    # @param other Another Vector object.
    # @return Self after addition.
    def __iadd__(self, other: 'Vector') -> 'Vector':
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    ## @brief Subtracts another vector.
    # @param other Another Vector object.
    # @return A new Vector representing the difference.
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector([self.x - other.x, self.y - other.y, self.z - other.z])
    
    ## @brief In-place subtraction of another vector.
    # @param other Another Vector object.
    # @return Self after subtraction.
    def __isub__(self, other: 'Vector') -> 'Vector':
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
    ## @brief Computes dot product or scalar multiplication.
    # @details If other is a Vector, computes dot product. If other is a number, performs scalar multiplication.
    # @param other Either a Vector or a float/int.
    # @return Float for dot product, or new Vector for scalar multiplication.
    def __mul__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return Vector([self.x * other, self.y * other, self.z * other])
    
    ## @brief Right-hand scalar multiplication (e.g., 5 * vector).
    # @param num A scalar (float or int).
    # @return A new Vector scaled by num.
    def __rmul__(self, num: float) -> 'Vector':
        return self.__mul__(num)
    
    ## @brief In-place scalar multiplication.
    # @param num A scalar (float or int).
    # @return Self after scaling.
    def __imul__(self, num: float) -> 'Vector':
        self.x *= num
        self.y *= num
        self.z *= num
        return self
    
    ## @brief Divides vector by a scalar.
    # @param num A scalar (float or int).
    # @return A new Vector with components divided by num.
    def __truediv__(self, num: float) -> 'Vector':
        return Vector([self.x / num, self.y / num, self.z / num])
    
    ## @brief In-place division by a scalar.
    # @param num A scalar (float or int).
    # @return Self after division.
    def __itruediv__(self, num: float) -> 'Vector':
        self.x /= num
        self.y /= num
        self.z /= num
        return self

    ## @brief Computes cosine of the angle between two vectors.
    # @param other Another Vector object.
    # @return Float representing the cosine of the angle.
    def __xor__(self, other: 'Vector') -> float:
        return (self * other) / (self.calcLen() * other.calcLen())
    
    ## @brief Compares vector lengths (greater than).
    # @param other Another Vector object.
    # @return True if self's length is greater than other's.
    def __gt__(self, other: 'Vector') -> bool:
        return self.calcLen() > other.calcLen()
    
    ## @brief Compares vector lengths (greater than or equal).
    # @param other Another Vector object.
    # @return True if self's length is greater than or equal to other's.
    def __ge__(self, other: 'Vector') -> bool:
        return self.calcLen() >= other.calcLen()
    
    ## @brief Compares vector lengths (less than).
    # @param other Another Vector object.
    # @return True if self's length is less than other's.
    def __lt__(self, other: 'Vector') -> bool:
        return self.calcLen() < other.calcLen()
    
    ## @brief Compares vector lengths (less than or equal).
    # @param other Another Vector object.
    # @return True if self's length is less than or equal to other's.
    def __le__(self, other: 'Vector') -> bool:
        return self.calcLen() <= other.calcLen()

    ## @brief Computes the Euclidean length of the vector.
    # @return Float representing the vector's length.
    def calcLen(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)