from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Krishna@19",  # Your MySQL password
    database="hospital"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    contact = request.form['contact']
    address = request.form['address']
    cursor.execute("INSERT INTO Patients (name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s)",
                   (name, age, gender, contact, address))
    db.commit()
    return redirect('/patients')

@app.route('/doctors')
def doctors():
    cursor.execute("SELECT * FROM Doctors")
    doctors = cursor.fetchall()
    return render_template('doctors.html', doctors=doctors)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form['name']
    specialization = request.form['specialization']
    contact = request.form['contact']
    cursor.execute("INSERT INTO Doctors (name, specialization, contact) VALUES (%s, %s, %s)",
                   (name, specialization, contact))
    db.commit()
    return redirect('/doctors')

@app.route('/appointments')
def appointments():
    query = """
        SELECT a.appointment_id, p.name AS patient, d.name AS doctor, a.appointment_date
        FROM Appointments a
        JOIN Patients p ON a.patient_id = p.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
    """
    cursor.execute(query)
    appointments = cursor.fetchall()
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    cursor.execute("SELECT * FROM Doctors")
    doctors = cursor.fetchall()
    return render_template('appointments.html', appointments=appointments, patients=patients, doctors=doctors)

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    patient_id = request.form['patient_id']
    doctor_id = request.form['doctor_id']
    date = request.form['date']
    cursor.execute("INSERT INTO Appointments (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)",
                   (patient_id, doctor_id, date))
    db.commit()
    return redirect('/appointments')

@app.route('/prescriptions')
def prescriptions():
    query = """
        SELECT pr.prescription_id, p.name AS patient, d.name AS doctor, pr.medicine, pr.notes
        FROM Prescriptions pr
        JOIN Appointments a ON pr.appointment_id = a.appointment_id
        JOIN Patients p ON a.patient_id = p.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
    """
    cursor.execute(query)
    prescriptions = cursor.fetchall()
    cursor.execute("SELECT * FROM Appointments")
    appointments = cursor.fetchall()
    return render_template('prescriptions.html', prescriptions=prescriptions, appointments=appointments)

@app.route('/add_prescription', methods=['POST'])
def add_prescription():
    appointment_id = request.form['appointment_id']
    medicine = request.form['medicine']
    notes = request.form['notes']
    cursor.execute("INSERT INTO Prescriptions (appointment_id, medicine, notes) VALUES (%s, %s, %s)",
                   (appointment_id, medicine, notes))
    db.commit()
    return redirect('/prescriptions')

if __name__ == '__main__':
    app.run(debug=True)
