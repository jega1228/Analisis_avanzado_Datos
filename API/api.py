#!/usr/bin/python
from flask import Flask, request
from m09_model_deployment import predict_price

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def PRICEpredict():
    return {
         
        "Year" : request.args.get('year'),
        "Mileage": request.args.get ('mileage'),
        "State": request.args.get('state'),
        "Make": request.args.get('make'),
        "Model": request.args.get('model'),
        
        "Forecats Price of Car": predict_price(request.args.get('year','mileage','state','make','model'))
        }, 200

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

