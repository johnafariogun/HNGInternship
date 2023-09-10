from . import app, db
from .models import Person
from flask import jsonify, request

# Create a new person
@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data or 'age' not in data:
        return jsonify({"error": "Your complete details are required"}), 400
    print(data)
    person = Person(name=data['name'], age=data['age'], track=data['track'], slack_username=data['slack_username'])
    db.session.add(person)
    db.session.commit()
    
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "slack_username": person.slack_username, "track": person.track}), 201

# Retrieve a person by name
@app.route('/person/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({"error": "Person not found"}), 404
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "slack_username": person.slack_username, "track": person.track}), 200

# Update details of an existing person by name
@app.route('/person/<string:name>', methods=['PUT'])
def update_person(name):
    data = request.get_json()
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({"error": "Person not found"}), 404

    person.age = data.get('age', person.age)
    person.slack_username = data.get('slack_username', person.slack_username)
    person.track = data.get('track', person.track)
    db.session.commit()
    
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "slack_username": person.slack_username, "track": person.track}), 200

# Remove a person by name
@app.route('/person/<string:name>', methods=['DELETE'])
def delete_person(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({"error": "Person not found"}), 404

    db.session.delete(person)
    db.session.commit()
    
    return jsonify({"message": "Person deleted"}), 200
