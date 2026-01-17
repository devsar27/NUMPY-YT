###Building URL Dynamically 
###Variable Rule
###Jinja2 Template Engine

##Jinja2 template engine 
'''
{{ }} expressions to print output in html 
{%...%} conditions, for loops 
{#...#} this is for comments
'''

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

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# #Variable Rule
# @app.route('/success/<int:score>')          #Wheneverr you assign a rule to a variable you have to tyoe cast it. so that you can get an error.
# def success(score):
#     return "The marks you got is "+ str(score)     

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template('result.html', results = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score':score, "res":res}

    return render_template('result1.html', results = exp)

#If condition 
@app.route('/successif/<int:score>')
def successif(score):   
    return render_template('result.html', results = score)


@app.route('/fail/<int:score>')
def fail(score):    

    return render_template('result.html', results = score)

# @app.route('/submit', methods = ['POST', 'GET'])
# def submit(): 
#Complete karna hau 

if __name__ == "__main__":  
    app.run(debug=True)     