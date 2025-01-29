### Test unitario

import unittest
from e13_pruebas_unitarias import sum_two
from e13_pruebas_unitarias import my_dict


# test de función
class TestFunSumTwo(unittest.TestCase):
    
    def test_fun_sum_two(self):
        self.assertEqual(sum_two(3, 5), 8)
        self.assertFalse(sum_two(3.2, 5))
        self.assertFalse(sum_two('mesa', 5))



# Test del diccionario
    def setUp(self):
        self.data ={
            'name': 'Oscar',
            'age': 46,
            'birth_date': '17 de agosto de 1978',
            'programing_languages': ['Python', 'C++']
        }


    def test_all_fieds_exist(self):
        self.assertIn('name', self.data)
        self.assertIn('age', self.data)
        self.assertIn('birth_date', self.data)
        self.assertIn('programing_languages', self.data)


    
    def test_all_values_are_correct(self):
        self.assertIsInstance(self.data['name'], str)
        self.assertIsInstance(self.data['age'], int)
        self.assertIsInstance(self.data['birth_date'], str)
        self.assertIsInstance(self.data['programing_languages'], list)



if __name__ == '__main__':
    unittest.main()

