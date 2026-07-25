from flask import Flask, render_template, request, redirect

from flask import Flask, render_template, request, redirect, session
app.secret_key = "cyberportal_secret_key"

MY_IP = "223.188.83.89"
from config import Config
from models import db, Student

import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
app.secret_key = "cyberportal_secret_key"

# ---------------- Home ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- Login ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["admin"] = username
            return redirect("/admin")

        return render_template(
            "login.html",
            error="Invalid Admin Username or Password"
        )

    return render_template("login.html")


# ---------------- Dashboard ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- Admin ----------------
@app.route("/admin")
def admin():
    return render_template("admin.html")


# ---------------- Profile ----------------
@app.route("/profile")
def profile():
    return render_template("profile.html")


# ---------------- Courses ----------------
@app.route("/courses")
def courses():
    return render_template("courses.html")


# ---------------- Attendance ----------------
@app.route("/attendance")
def attendance():
    return render_template("attendance.html")


# ---------------- Results ----------------
@app.route("/results")
def results():
    return render_template("results.html")


# ---------------- Notices ----------------
@app.route("/notices")
def notices():
    return render_template("notices.html")


# ---------------- Contact ----------------
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        print("===== CONTACT MESSAGE =====")
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)
        print("===========================")

        return render_template(
            "contact.html",
            success="✅ Your message has been sent successfully!"
        )

    return render_template("contact.html")


# ---------------- Register ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        student = Student(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            phone=request.form["phone"],
            student_id=request.form["student_id"],
            course=request.form["course"],
            semester=request.form["semester"],
            dob=request.form["dob"],
            address=request.form["address"],
            username=request.form["username"]
        )

        student.set_password(request.form["password"])

        db.session.add(student)
        db.session.commit()

        return redirect("/userlogin")

    return render_template("register.html")
#gggg
@app.route("/userlogin", methods=["GET", "POST"])
def userlogin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        student = Student.query.filter_by(username=username).first()

        if student and student.check_password(password):
            session["user"] = student.username
            return redirect("/dashboard")

        return "Invalid Username or Password"

    return render_template("userlogin.html")

@app.route("/students")
def students():


    if request.remote_addr != MY_IP:    
        return "Access Denied", 403        


students = Student.query.all()


output = """
    <html>
    <head>
        <title>Registered Students</title>
        <style>
            body{
                font-family:Arial;
                background:#f4f4f4;
                padding:20px;
            }
            table{
                width:100%;
                border-collapse:collapse;
                background:white;
            }
            th,td{
                border:1px solid #ddd;
                padding:10px;
                text-align:center;
            }
            th{
                background:#007BFF;
                color:white;
            }
        </style>
    </head>
    <body>

    <h2>Registered Students</h2>

    <table>

    <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Student ID</th>
        <th>Course</th>
        <th>Semester</th>
        <th>DOB</th>
        <th>Address</th>
        <th>Username</th>
        <th>Password</th>
    </tr>
    """

    for s in students:
        output += f"""
        <tr>
            <td>{s.id}</td>
            <td>{s.first_name}</td>
            <td>{s.last_name}</td>
            <td>{s.email}</td>
            <td>{s.phone}</td>
            <td>{s.student_id}</td>
            <td>{s.course}</td>
            <td>{s.semester}</td>
            <td>{s.dob}</td>
            <td>{s.address}</td>
            <td>{s.username}</td>
            <td>{s.password}</td>
        </tr>
        """

    output += """
    </table>
    </body>
    </html>
    """

    return output
    

# test
@app.route("/testpassword")
def testpassword():
    student = Student()
    student.set_password("123456")
    return student.password
"""
@app.route("/delete-all-students")
def delete_all_students():

    Student.query.delete()
    db.session.commit()

    return "All student records deleted successfully."
"""
if __name__ == "__main__":
    app.run(debug=True)