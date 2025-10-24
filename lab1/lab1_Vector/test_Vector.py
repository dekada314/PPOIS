import unittest
from Vector import Vector

class Test_Vector(unittest.TestCase):
    
    def setUp(self):
        self.vector1 = Vector([8,6,0],[4,3,0])
        self.vector2 = Vector([12,5,0])
    
    def test_calcLen(self):
        self.assertEqual(self.vector1.calcLen(),5)
        
    def test_add(self):
        result = self.vector1 + self.vector2
        self.assertEqual(result.x, 16)
        self.assertEqual(result.y, 8)
        self.assertEqual(result.z, 0)
        
    def test_iadd(self):
        vector = self.vector1
        vector += self.vector2
        self.assertEqual(vector.x, 16)
        self.assertEqual(vector.y, 8)
        self.assertEqual(vector.z, 0)
        
    def test_sub(self):
        result = self.vector1 - self.vector2
        self.assertEqual(result.x, -8)
        self.assertEqual(result.y, -2)
        self.assertEqual(result.z, 0)
        
    def test_isub(self):
        vector = self.vector1
        vector -= self.vector2
        self.assertEqual(vector.x, -8)
        self.assertEqual(vector.y, -2)
        self.assertEqual(vector.z, 0)
        
    def test_mul_vector(self):
        result = self.vector1 * self.vector2
        self.assertEqual(result, 63)  
    
    def test_mul_number(self):
        result = self.vector1 * 2
        self.assertEqual(result.x, 8)
        self.assertEqual(result.y, 6)
        self.assertEqual(result.z, 0)
    
    def test_imul(self):
        vector = self.vector1
        vector *= 2
        self.assertEqual(vector.x, 8)
        self.assertEqual(vector.y, 6)
        self.assertEqual(vector.z, 0)
    
    def test_truediv(self):
        result = self.vector1 / 2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 1.5)
        self.assertEqual(result.z, 0)
    
    def test_itruediv(self):
        vector = self.vector1
        vector /= 2
        self.assertEqual(vector.x, 2)
        self.assertEqual(vector.y, 1.5)
        self.assertEqual(vector.z, 0)
    
    def test_comparison(self):
        self.assertTrue(self.vector1 < self.vector2)
        self.assertTrue(self.vector1 <= self.vector2)
        self.assertFalse(self.vector1 > self.vector2)
        self.assertFalse(self.vector1 >= self.vector2)


        
if __name__ == '__main__':
    unittest.main()



