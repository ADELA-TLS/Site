from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/', methods=['GET'])
@app.route('/presentation', methods=['GET'])
def presentation():
    return render_template('presentation.html')

@app.route('/charte', methods=['GET'])
def charte():
    return render_template('charte.html')

@app.route('/projets', methods=['GET'])
def projets():
    return render_template('projets.html')

@app.route('/openData', methods=['GET'])
def openData():
    return render_template('openData.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()