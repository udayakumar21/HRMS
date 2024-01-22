from flask import Flask, render_template, request, jsonify
from firebase_admin import credentials, initialize_app, db

app = Flask(__name__)

# Firebase configuration
cred = credentials.Certificate('credentials.json')
firebase_app = initialize_app(cred, {'databaseURL': 'https://hrms-42a58-default-rtdb.firebaseio.com/'})

class Employee:
    def __init__(self, name, designation, department, date_of_joining, address, email):
        self.name = name
        self.designation = designation
        self.department = department
        self.date_of_joining = date_of_joining
        self.address = address
        self.email = email
        self.in_time = None
        self.out_time = None

    def serialize(self):
        return {
            'name': self.name,
            'designation': self.designation,
            'department': self.department,
            'date_of_joining': self.date_of_joining,
            'address': self.address,
            'email': self.email,
            'in_time': self.in_time,
            'out_time': self.out_time
        }

@app.route('/')
def home():
    employees = db.reference('/employees').get()

    # Calculate department count
    department_count = {}
    for employee_id, employee in employees.items():
        if isinstance(employee, dict):  # Check if employee is a dictionary
            department = employee.get('department')
            if department in department_count:
                department_count[department] += 1
            else:
                department_count[department] = 1

    return render_template('home.html', employees=employees, department_count=department_count)

@app.route('/employees')
def employee_list():
    employees = db.reference('/employees').get()
    return render_template('employee_list.html', employees=employees)

@app.route('/employee/<int:employee_id>')
def employee_details(employee_id):
    employee = db.reference('/employees/{}'.format(employee_id)).get()
    return render_template('employee_details.html', employee=employee)

@app.route('/api/employees', methods=['GET', 'POST'])
def api_employees():
    if request.method == 'GET':
        employees = db.reference('/employees').get()
        return jsonify(employees)

    elif request.method == 'POST':
        data = request.get_json()
        new_employee_ref = db.reference('/employees').push()
        new_employee_ref.set(data)
        return jsonify({'message': 'Employee added successfully'})

@app.route('/api/employee/<int:employee_id>', methods=['GET'])
def api_employee_details(employee_id):
    employee = db.reference('/employees/{}'.format(employee_id)).get()
    return jsonify(employee)

@app.route('/api/attendance', methods=['POST'])
def mark_attendance():
    data = request.json
    employee_id = data.get('employee_id')
    in_time = data.get('in_time')
    out_time = data.get('out_time')

    employee = db.reference('/employees/{}'.format(employee_id)).get()
    if employee:
        employee['in_time'] = in_time
        employee['out_time'] = out_time

        db.reference('/employees/{}'.format(employee_id)).set(employee)
        return jsonify({'message': 'Attendance marked successfully'})
    else:
        return jsonify({'error': 'Employee not found'})

if __name__ == '__main__':
    app.run(debug=True)
