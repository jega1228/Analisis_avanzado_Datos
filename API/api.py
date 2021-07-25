#!/usr/bin/python
from flask import Flask, request, render_template
from m09_model_deployment import predict_price

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def PRICEpredict():
   
    year = request.args.get('year')
    mileage = request.args.get ('mileage')
    state = request.args.get('state')
    make = request.args.get('make')
    model = request.args.get('model')
    
#   return {
#        
#       "Year" : year,
#       "Mileage": mileage,
#       "State": state,
#       "Make": make,
#       "Model": model,
#       
#       "Forecats Price of Car": predict_price(year,mileage,state,make,model)
#       }, 200


@app.route('/')
def home():
    
    return render_template('home.html')

#@app.route('/hola', methods=['GET'])
#def hola():
#    return {
#         "result": "todo bien"
#        }, 200


#@app.route('/nombre', methods=['GET'])
#def nombre():
#    return {
#         "nombre": request.args.get('NOMBRE'),
#         "apellido": request.args.get('APELLIDO')
#        }, 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

