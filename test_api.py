from datetime import datetime
from app.utils import convert_ist_to_utc
import unittest
from app import create_app
from app.models import db, FitnessClass
from datetime import datetime
class BookingAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        test_class = FitnessClass(
            name="Test Yoga",
            datetime=convert_ist_to_utc(datetime(2025, 6, 10, 10, 0)),  
            instructor="Test Instructor",
            total_slots=10,
            available_slots=10
        )
        db.session.add(test_class)
        db.session.commit()
        self.test_class_id = test_class.id
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_classes_endpoint(self):
        response = self.client.get('/classes')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) >= 1)

    def test_missing_booking_fields(self):
        response = self.client.post('/book', json={})
        self.assertEqual(response.status_code, 400)

    def test_successful_booking(self):
        response = self.client.post('/book', json={
            "class_id": self.test_class_id,
            "client_name": "Test User",
            "client_email": "test@example.com"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Booking confirmed", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
