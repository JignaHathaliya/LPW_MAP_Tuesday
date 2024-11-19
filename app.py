#Implement a python application for the hospital management system (HMS), build an HMS image of the docker, and 
# deploy it using a docker desktop. Upload HMS with a docker image into the GitHub repository.

from flask import Flask, request, jsonify
from models import db, Patient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully!"}), 201

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{'id': patient.id, 'name': patient.name, 'age': patient.age, 'gender': patient.gender} for patient in patients])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


