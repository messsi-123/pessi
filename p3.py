from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Asha', 'marks': 88},
    {'id': 2, 'name': 'Rahul', 'marks': 76},
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for s in students:
        if s['id'] == student_id:
            return jsonify(s), 200

    return jsonify({'error': 'student not found'}), 404

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    new_id = max(s['id'] for s in students) + 1 if students else 1

    new_student = {
        'id': new_id,
        'name': data['name'],
        'marks': data['marks']
    }

    students.append(new_student)

    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()

    for s in students:
        if s['id'] == student_id:
            s['name'] = data['name']
            s['marks'] = data['marks']

            return jsonify(s), 200

    return jsonify({'error': 'student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students

    before = len(students)

    students = [s for s in students if s['id'] != student_id]

    if len(students) == before:
        return jsonify({'error': 'student not found'}), 404

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
