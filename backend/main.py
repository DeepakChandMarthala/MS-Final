
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../frontend/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    return "<h1>Hello from the Backend!</h1>"

#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

