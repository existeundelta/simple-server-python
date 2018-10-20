from flask import Flask
app = Flask(__name__)
from sense_hat import SenseHat
import time

sense = SenseHat()

@app.route('/')
def hello_world():
    return '<h1>Que pasa perro</h1>'
	
@app.route('/temp')
def printemp():
	temp = sense.get_temperature()
	return str(temp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
