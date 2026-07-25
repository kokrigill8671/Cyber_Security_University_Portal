from flask import Flask, render_template, request, redirect

from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
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

        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        student_id = request.form["student_id"]
        course = request.form["course"]
        semester = request.form["semester"]
        dob = request.form["dob"]
        address = request.form["address"]
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        with open("users.txt", "a") as f:
            f.write(
                f"{first_name}|{last_name}|{email}|{phone}|{student_id}|{course}|{semester}|{dob}|{address}|{username}|{hashed_password}\n"
            )

        return redirect("/userlogin")

    return render_template("register.html")


@app.route("/userlogin", methods=["GET", "POST"])
def userlogin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if os.path.exists("users.txt"):

            with open("users.txt", "r") as f:

                for line in f:

                    data = line.strip().split("|")

                    saved_username = data[9]
                    saved_password = data[10]

                    if username == saved_username and check_password_hash(saved_password, password):

                        session["user"] = username

                        return redirect("/dashboard")

        return "Invalid Username or Password"

    return render_template("userlogin.html")

if __name__ == "__main__":
    app.run(debug=True)