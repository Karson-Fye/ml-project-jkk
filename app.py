from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
rf = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'classifier.pkl'), 'rb'))
# db = os.path.join(cur_dir, 'reviews.sqlite')

def classify(data):
    label = {0: 'Eliminated', 1: 'Survived'}
    y = rf.predict(data)[0]
    proba = rf.predict_proba(data)
    return label[y], proba

######## Flask
class HelloForm(Form):
    name = TextAreaField('',[validators.DataRequired()])
    sex = TextAreaField('')
    age = TextAreaField('',[validators.DataRequired()])
    ticket = TextAreaField('',[validators.DataRequired()])
    fare = TextAreaField('',[validators.DataRequired()])
    clas = TextAreaField('')
    children = TextAreaField('')
    port = TextAreaField('')

@app.route('/')
def indexpage():
    return render_template('index.html')

@app.route('/index')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)

@app.route('/survived', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        sex = request.form['sex']
        age = request.form['age']
        ticket = request.form['ticket']
        fare = request.form['fare']
        clas = request.form['clas']
        children = request.form['children']
        port = request.form['port']

        X = np.array([[sex, clas, fare, port, children, age, ticket]])
        y,proba = classify(X)
        proba = str(round(np.max(proba)*100,2)) + '0%'
        return render_template('survived.html', name=name, sur=y, pro=proba)
    return render_template('first_app.html', form=form)

@app.route('/algopage')
def algopage():
    return render_template('algorithms.html')

@app.route('/cleandata')
def cleandata():
    return render_template('cleandata.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/validation')
def validation():
    return render_template('validation.html')

if __name__ == '__main__':
    app.run(debug=True)