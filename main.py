from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route("/search-form")
def search():
    return render_template('forms.html', title = "Search query for DuckDuckGo")

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form['first_name']
    return render_template('hello_greeting.html', title = "Allow me to welcome you!", name = first_name)

tasks = []

@app.route("/todos", methods = ['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title="Your TODOs list",tasks=tasks)

app.run()