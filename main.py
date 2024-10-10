from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    temperature = float(request.form['temperature'])
    if temperature <= 0:
        message = "A cold, Isn't it?"
    elif 0 < temperature < 10:
        message = "Cool."
    else:
        message = "Nice weather we're having."
    return render_template('index.html', message=message, port=1939)

if __name__ == '__main__':
    app.run(debug=True)
