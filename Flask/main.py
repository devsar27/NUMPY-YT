from flask import Flask, render_template

#render_template will be responsible for rendering HTML templates

app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask coourse</h1></html>"

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":  
    app.run(debug=True)     