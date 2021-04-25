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
        X = np.array([[0, 1, 400, 1, 2, 70, 10300]])
        y,proba = classify(X)
        return render_template('survived.html', name=n, gender=g, age=a, sur=y, pro=proba)
    return render_template('first_app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)