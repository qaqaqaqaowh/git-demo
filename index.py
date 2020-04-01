from flask import Flask, render_template, request, redirect
from models.todo import Todo

app = Flask(__name__)

@app.route("/")
def index():
	todos = Todo.select()
	return render_template("hello_world.html", todos=todos)

@app.route("/profile")
def profile():
	return render_template("profile.html")

@app.route("/submit", methods=["POST"])
def submit():
	Todo.create(todo=request.form.get("todo_task"))
	return redirect("/")

@app.route("/asd")
def asd():
	pass

app.run()

# 1. pip install python-dotenv
# 2. create .env file
# 3. insert FLASK_ENV and FLASK_APP