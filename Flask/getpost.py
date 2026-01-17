from flask import Flask, render_template, request

#render_template will be responsible for rendering HTML templates

app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask coourse</h1></html>"

@app.route("/about", methods = ['GET'])
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == "__main__":  
    app.run(debug=True)     