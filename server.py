from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_words(num, word):
    return num * word

@app.route('/hello_world')
def hello_again():
    return render_template("hello_world.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug = True)