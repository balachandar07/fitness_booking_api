from flask import Blueprint, request, jsonify
from datetime import datetime
from .models import db, FitnessClass, Booking
from .utils import convert_utc_to_ist
from datetime import datetime, timezone

fba = Blueprint('fba', __name__)

@fba.route('/classes', methods=['GET'])
def get_classes():
    classes = FitnessClass.query.all()
    return jsonify([
        {
            'id': c.id,
            'name': c.name,
            'datetime': convert_utc_to_ist(c.datetime).isoformat(),
            'instructor': c.instructor,
            'available_slots': c.available_slots
        } for c in classes
    ])

@fba.route('/book', methods=['POST'])
def book_class():
    data = request.get_json()
    class_id = data.get('class_id')
    client_name = data.get('client_name')
    client_email = data.get('client_email')
    if not all([class_id, client_name, client_email]):
        return jsonify({'error': 'Missing fields'}), 400
    fitness_class = db.session.get(FitnessClass, class_id)
    if not fitness_class:
        return jsonify({'error': 'Class not found'}), 404
    if fitness_class.available_slots <= 0:
        return jsonify({'error': 'No available slots'}), 400

    booking = Booking(
        class_id=class_id,
        client_name=client_name,
        client_email=client_email,
        booked_at=datetime.now(timezone.utc)
    )
    fitness_class.available_slots -= 1
    db.session.add(booking)
    db.session.commit()

    return jsonify({'message': 'Booking confirmed!'})

@fba.route('/bookings', methods=['GET'])
def get_bookings():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    bookings = Booking.query.filter_by(client_email=email).all()
    result = []
    for b in bookings:
        fitness_class = FitnessClass.query.get(b.class_id)
        result.append({
            'class_name': fitness_class.name,
            'datetime': convert_utc_to_ist(fitness_class.datetime).isoformat(),
            'instructor': fitness_class.instructor,
            'booked_at': b.booked_at.isoformat()
        })
    return jsonify(result)
