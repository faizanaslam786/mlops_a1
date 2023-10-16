import unittest
from app import app

class TestIrisClassification(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_classification(self):
        # Test a valid prediction
        valid_input = {
            'sepal_length': '5.1',
            'sepal_width': '3.5',
            'petal_length': '1.4',
            'petal_width': '0.2'
        }
        response = self.app.post('/', data=valid_input)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The predicted Iris species is Setosa', response.data)

        # Test an invalid prediction (non-numeric input)
        invalid_input = {
            'sepal_length': 'invalid',
            'sepal_width': 'input',
            'petal_length': 'here',
            'petal_width': 'too'
        }
        response = self.app.post('/', data=invalid_input)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input. Please enter valid numeric values.', response.data)

if __name__ == '__main__':
    unittest.main()
