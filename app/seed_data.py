from datetime import datetime
from .models import db, FitnessClass
from .utils import convert_ist_to_utc

def seed_data():
    classes = [
        FitnessClass(name='Yoga', datetime=convert_ist_to_utc(datetime(2025, 6, 10, 10, 0)), instructor='Alice', total_slots=10, available_slots=10),
        FitnessClass(name='Zumba', datetime=convert_ist_to_utc(datetime(2025, 6, 11, 18, 0)), instructor='Bob', total_slots=8, available_slots=8),
        FitnessClass(name='HIIT', datetime=convert_ist_to_utc(datetime(2025, 6, 12, 7, 30)), instructor='Charlie', total_slots=12, available_slots=12),
    ]
    db.session.bulk_save_objects(classes)
    db.session.commit()
