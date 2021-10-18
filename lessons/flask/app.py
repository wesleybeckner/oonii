from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World!"

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
   app.run()