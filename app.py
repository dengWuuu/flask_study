from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/hello')
def test():
    return 'Test'


@app.route('/var/<name>')
def getName(name):
    return 'hello %s !' % name


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(1)
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        print(2)
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run("127.0.0.1", 8085, True)
