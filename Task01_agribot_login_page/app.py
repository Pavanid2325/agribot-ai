from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_very_secret_and_random_key_for_security'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# --- Database Model with User Role ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

# --- Main Landing/Chooser Page ---
@app.route("/")
def chooser():
    return render_template("chooser.html")

# --- Registration with Constraints ---
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # --- Basic Constraints ---
        if len(username) < 4:
            flash("Username must be at least 4 characters long.", "error")
            return redirect(url_for("register"))
        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "error")
            return redirect(url_for("register"))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.", "error")
            return redirect(url_for("register"))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, role='user')
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in as a User.", "success")
        return redirect(url_for("user_login"))
    return render_template("register.html")

# --- Separate Login Routes ---
@app.route("/login/user", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, role='user').first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for("user_dashboard"))
        else:
            flash("Invalid user credentials.", "error")
    return render_template("login.html")

@app.route("/login/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        admin = User.query.filter_by(username=username, role='admin').first()
        if admin and bcrypt.check_password_hash(admin.password, password):
            session['user_id'] = admin.id
            session['username'] = admin.username
            session['role'] = admin.role
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid admin credentials.", "error")
    return render_template("admin_login.html")

# --- Dashboards & Logout ---
@app.route("/dashboard/user")
def user_dashboard():
    if session.get('role') != 'user':
        flash("Please log in to access this page.", "error")
        return redirect(url_for("user_login"))
    return f"<h1>Welcome, {session.get('username')}! This is the User Dashboard.</h1><a href='/logout'>Logout</a>"

@app.route("/dashboard/admin")
def admin_dashboard():
    # Check if the logged-in user is an admin
    if session.get('role') != 'admin':
        flash("You do not have permission to access this page.", "error")
        return redirect(url_for("chooser"))

    # Fetch all users who are not admins
    users = User.query.filter_by(role='user').all()

    # Pass the list of users to the template
    return render_template("admin_dashboard.html", user_list=users)

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("chooser"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Create a default admin user if one doesn't exist
        if not User.query.filter_by(username='admin').first():
            hashed_pw = bcrypt.generate_password_hash('admin123').decode('utf-8')
            default_admin = User(username='admin', password=hashed_pw, role='admin')
            db.session.add(default_admin)
            db.session.commit()
    app.run(debug=True)