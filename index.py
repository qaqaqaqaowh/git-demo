from flask import Flask, render_template, request, redirect, url_for
from models.user import User

app = Flask(__name__)

@app.route("/")
def index():
	users = User.select()
	return render_template("hello_world.html", users=users)

@app.route("/profile/<username>")
def profile(username):
	return render_template("profile.html", username=username)

@app.route("/submit", methods=["POST"])
def submit():
	User.create(username=request.form.get("username"))
	return redirect("/")

@app.route("/users/<username>", methods=["POST"])
def update(username):
	return redirect(f"/profile/{username}")

app.run()

# 1. pip install python-dotenv
# 2. create .env file
# 3. insert FLASK_ENV and FLASK_APP