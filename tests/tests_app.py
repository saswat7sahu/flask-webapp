import unittest
from app.app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>DevOps Engineer Portfolio</title>', response.data)
        self.assertIn(b'<h1>Saswata Sahu</h1>', response.data)

if __name__ == '__main__':
    unittest.main()

