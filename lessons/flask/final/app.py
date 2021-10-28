from flask import Flask, url_for, redirect, request, render_template
app = Flask(__name__)

# @app.route('/type/<int:var>')
# def check_type(var):
#    print(type(var))
#    return "the type is: {}".format(type(var).__name__)

@app.route('/emoji/')
def emoji():
   return render_template('static.html')

@app.route('/form/')
def index():
   return render_template("login.html")

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   elif request.method == 'GET':
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
   else:
      return "unkown method"

@app.route('/user/<name>')
def hello_user(name):
   if name == 'admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', name=name))

@app.route('/admin/')
def hello_admin():
   return "Hello Admin!"

@app.route('/guest/<name>')
def hello_guest(name):
   return "Hello {}!".format(name)

def hello_world(msg):
   return "{}!".format(msg)
app.add_url_rule("/<msg>", view_func=hello_world)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
   app.run()