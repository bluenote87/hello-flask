from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render(title = "Hello.")

@app.route("/search-form")
def search():
    template = jinja_env.get_template('forms.html')
    return template.render(title = "Search query for DuckDuckGo")

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(title = "Allow me to welcome you!", name = first_name)

tasks = []

@app.route("/todos", methods = ['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    template = jinja_env.get_template('todos.html')
    return template.render(title="Your TODOs list",tasks=tasks)

app.run()