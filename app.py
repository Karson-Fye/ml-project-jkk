from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
rf = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'reviews.sqlite')

def classify(data):
    label = {0: 'Eliminated', 1: 'Survived'}
    y = rf.predict(data)[0]
    proba = np.max(rf.predict_proba(data))
    return label[y], proba

######## Flask
class HelloForm(Form):
    n = TextAreaField('',[validators.DataRequired()])
    g = TextAreaField('',[validators.DataRequired()])
    a = TextAreaField('',[validators.DataRequired()])

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)

@app.route('/hello', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        n = request.form['n']
        g = request.form['g']
        a = request.form['a']
        X =np.arr([[1, 2, 200, 1, 2, 25, 10300]])
        classify(X)

        
        y, proba = classify(review)
        return render_template('hello.html', name=n, gender=g, age=a, survived=y, proba=proba)
    return render_template('first_app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)