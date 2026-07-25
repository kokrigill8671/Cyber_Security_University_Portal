from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    student_id = db.Column(db.String(50))
    course = db.Column(db.String(100))
    semester = db.Column(db.String(50))
    dob = db.Column(db.String(50))
    address = db.Column(db.Text)

    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password