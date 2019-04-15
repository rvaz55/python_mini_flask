#Using python to program the 'hello.py' app
#the app is written in python
#and uses the Flask framework to display the
#app on a web browser

#Files for a complete version of this project can be found at:
#https://github.com/jekwatt/mini-flask-app

#Things to remember:
#used pip (the package manager for python) to download the 'flask' package
#After installing 'flask', the program can be run using the command:
#python name_of_file.py 
#'python' keyword and 'name_of_file.py' file  command runs the program
#when run, flask places creates a 'hello world' on a local web server!

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()