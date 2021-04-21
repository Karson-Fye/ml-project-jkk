
# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World"

# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

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
        return render_template('hello.html', name=n, gender=g, age=a)
    return render_template('first_app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)