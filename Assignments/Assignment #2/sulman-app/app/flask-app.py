# Import Packages
from bmi_calculator import BMI_calculator
from flask import Flask, jsonify, request

# Instantiate Flask Object
app = Flask('__name__')

@app.route('/', methods = ['GET', 'POST'])

def get_input():
    """ A function to get results using flasks, evaluate and return flasks."""

    # Packets
    packet = request.get_json(force = True)
    weight = packet['weight']
    height = packet['height']

    # Calculate BMI
    bmi = BMI_calculator(weight, height)

    return jsonify(packet, bmi)

# Driver function
if __name__ == '__main__':
    app.run(debug=True)