# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('survived.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World, bb!"

if __name__ == '__main__':
    app.run()