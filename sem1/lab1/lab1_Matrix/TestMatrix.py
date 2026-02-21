import unittest
from Matrix import Matrix

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(2, 2, [[1.0, 2.0], [3.0, 4.0]])
        self.identity = Matrix(2, 2, [[1.0, 0.0], [0.0, 1.0]])
        self.zero = Matrix(2, 2, [[0.0, 0.0], [0.0, 0.0]])
        self.diagonal = Matrix(2, 2, [[1.0, 0.0], [0.0, 2.0]])
        self.symmetric = Matrix(2, 2, [[1.0, 2.0], [2.0, 1.0]])
        self.upper_tri = Matrix(2, 2, [[1.0, 2.0], [0.0, 3.0]])
        self.lower_tri = Matrix(2, 2, [[1.0, 0.0], [2.0, 3.0]])

    def test_init(self):
        self.assertEqual(self.matrix.rows, 2)
        self.assertEqual(self.matrix.cols, 2)
        self.assertEqual(self.matrix.data, [[1.0, 2.0], [3.0, 4.0]])

    def test_load_from_file(self):
        with open("test_matrix.txt", "w") as f:
            f.write("1.0 2.0\n3.0 4.0")
        matrix = Matrix()
        matrix.load_from_file("test_matrix.txt")
        self.assertEqual(matrix.data, [[1.0, 2.0], [3.0, 4.0]])

    def test_submatrix(self):
        sub = self.matrix.submatrix(0, 0, 0, 0)
        self.assertEqual(sub.data, [[1.0]])

    def test_transpon(self):
        self.matrix.transpon()
        self.assertEqual(self.matrix.data, [[1.0, 3.0], [2.0, 4.0]])
        
    def test_resize(self):
        self.matrix.resize(1,1)
        self.assertEqual(self.matrix.data, [[1.0]])
        
    def test_is_square(self):
        self.assertTrue(self.matrix.is_square())
        matrix = Matrix(2, 3, [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        self.assertFalse(matrix.is_square())

    def test_is_diagonal(self):
        self.assertTrue(self.diagonal.is_diagonal())
        self.assertFalse(self.matrix.is_diagonal())

    def test_is_zero(self):
        self.assertTrue(self.zero.is_zero())
        self.assertFalse(self.matrix.is_zero())

    def test_is_identity(self):
        self.assertTrue(self.identity.is_identity())
        self.assertFalse(self.matrix.is_identity())

    def test_is_symmetric(self):
        self.assertTrue(self.symmetric.is_symmetric())
        self.assertFalse(self.matrix.is_symmetric())

    def test_is_upper_triangular(self):
        self.assertTrue(self.upper_tri.is_upper_triangular())
        self.assertFalse(self.matrix.is_upper_triangular())

    def test_is_lower_triangular(self):
        self.assertTrue(self.lower_tri.is_lower_triangular())
        self.assertFalse(self.matrix.is_lower_triangular())
        
    def test_pre_inc(self):
        result = self.matrix.pre_inc()
        self.assertEqual(result.data, [[2.0, 3.0], [4.0, 5.0]])
    def test_pre_dec(self):
        result = self.matrix.pre_dec()
        self.assertEqual(result.data, [[0.0, 1.0], [2.0, 3.0]])
        
    def test_post_inc(self):
        result = self.matrix.post_inc()
        self.assertEqual(result.data, [[1.0, 2.0], [3.0, 4.0]])
        
    def test_post_dec(self):
        result = self.matrix.post_dec()
        self.assertEqual(result.data, [[1.0, 2.0], [3.0, 4.0]])
        

if __name__ == '__main__':
    unittest.main()