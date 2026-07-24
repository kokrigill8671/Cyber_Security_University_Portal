<<<<<<< HEAD
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

        # Demo Login
        if username == "admin" and password == "admin123":
            return redirect("/admin")

        return redirect("/dashboard")

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

        # Display submitted data in the terminal
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
    return render_template("register.html")


if __name__ == "__main__":
=======
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

        # Demo Login
        if username == "admin" and password == "admin123":
            return redirect("/admin")

        return redirect("/dashboard")

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

        # Display submitted data in the terminal
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
    return render_template("register.html")


if __name__ == "__main__":
>>>>>>> 856e12cee79502ecf54a6c0b66c9d2720f3d7548
    app.run(debug=True)