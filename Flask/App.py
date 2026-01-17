from flask import Flask 
'''
  It creates an instance of the Flask class,
  Which is the WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!, My Name is ChatGPT. Welcome to Flask Application. " \
    "This is a simple web application built using Flask framework."

@app.route("/about")
def about():
    return "This Flask application demonstrates the basics of routing and "


if __name__ == "__main__":  ##This is entry point of any Python application
    app.run(debug=True)     ##Run the application in debug mode


