import unittest
import json
from app import app, business_details

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_details(self):
        response = self.app.post('/upload_details', json={
            "classrooms": {
                "Math 101": {
                    "availability": "MWF 10:00 AM - 11:00 AM",
                    "price": "$100",
                    "syllabus": "Algebra, Geometry, Calculus"
                }
            },
            "teachers": {
                "Mr. Smith": {
                    "availability": "MWF 9:00 AM - 12:00 PM",
                    "subjects": "Math"
                }
            }
        })
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Business details uploaded successfully.")
        self.assertIn("Math 101", business_details['classrooms'])
        self.assertIn("Mr. Smith", business_details['teachers'])

    def test_query(self):
        # First, upload details
        self.app.post('/upload_details', json={
            "classrooms": {
                "Math 101": {
                    "availability": "MWF 10:00 AM - 11:00 AM",
                    "price": "$100",
                    "syllabus": "Algebra, Geometry, Calculus"
                }
            },
            "teachers": {
                "Mr. Smith": {
                    "availability": "MWF 9:00 AM - 12:00 PM",
                    "subjects": "Math"
                }
            }
        })
        # Then, make a query
        response = self.app.post('/query', json={"query": "What is the availability for the Math 101 class?"})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn("MWF 10:00 AM - 11:00 AM", data['response'])

if __name__ == '__main__':
    unittest.main()
