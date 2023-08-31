import unittest
from unittest.mock import patch

# Import the function to be tested
from myFunc import hello, bye

class MyFuncTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = Flask(__name__)
    
    def tearDown(self):
        pass
    
    def test_hello_route(self):
        with self.app.test_client() as client:
            response = client.get('/hello')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Hello world!')
    
    def test_hello_template_rendered(self):
        with self.app.test_client() as client:
            response = client.get('/hello')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<p>Hello world!</p>', response.data)
    
    def test_bye_route(self):
        with self.app.test_client() as client:
            response = client.get('/bye')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Goodbye world!')
    
    def test_bye_template_rendered(self):
        with self.app.test_client() as client:
            response = client.get('/bye')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<p>Goodbye world!</p>', response.data)


if __name__ == '__main__':
    unittest.main()