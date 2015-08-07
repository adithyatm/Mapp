from flask import Flask, request, render_template, redirect
import requests
import json
# import subprocess
# from postticket import test
from helpers import post_hf, request_hf

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        x = request.form['ename']
        return render_template('/hi.html', name=x)
    else:
        return render_template('home.html')

#@app.route('/', methods=['GET','POST'])


def form():
    x = request.form['ename']
    return render_template('/hi.html', name=x)


@app.route('/w3')
def w3():
    test()


@app.route('/testbootstrap')
def testbootstrap():
    return render_template('/testbootstrap.html')


def form(gobutton='none'):
    value = request.form['gobutton']
    return manual_redirect()


@app.route('/adithya/')
def adithya():
    return 'This is Adithya Page'

#@app.route('/<username>')
# def any_user(username=None):
#	return render_template('hi.html',name=username)


@app.route('/hi')
def image():
    return render_template('/home.html')


@app.route('/whatsapp')
def whatsapp():
    return render_template('/whatsapp.php')


@app.route('/map', methods=['GET', 'POST'])
def map(lat=None, lng=None):
    a = request.form['lat']
    b = request.form['lng']
    return render_template('/map.html', lat=a, lng=b)


@app.route('/orgtable1')
def org_table1():
    return manual_redirect()


@app.route('/orgtable')
def org_table():
    return render_template('orgtable.html')


@app.route('/sublime')
def sublime():
    return render_template('sublime.html')


def manual_redirect():
    return redirect('/orgtable')


@app.route('/hfticket')
def hfticket():
    return render_template('/form.html')


@app.route('/success', methods=['GET', 'POST'])
def success(Fname=None, Cat=None, Email=None, Sub=None, Priority=None, Content=None):
    payload = {
        'category': request.form['Cat'],
        'name': request.form['Fname'],
        'email': request.form['Email'],
        'priority': request.form['Priority'],
        'subject': request.form['Sub'],
        'text': request.form['Content'],
        'c-cf-17': '1234',
        'c-cf-18': 3,
        'c-cf-4': '1234'
    }
    url = 'https://tenmilesadithya.happyfox.com/api/1.1/json/tickets/'
    res = post_hf(url, payload)
    return render_template('/form.html')

if __name__ == '__main__':
    app.debug = True
    app.run()