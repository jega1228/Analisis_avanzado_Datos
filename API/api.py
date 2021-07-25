#!/usr/bin/python
from flask import Flask, request, render_template
from m09_model_deployment import predict_price

app = Flask(__name__)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''


@app.route('/predict', methods=['GET'])
def PRICE():
   
    year = request.args.get('year')
    mileage = request.args.get ('mileage')
    state = request.args.get('state')
    make = request.args.get('make')
    model = request.args.get('model')
    
    forecast = predict_price(year,mileage,state,make,model)

    return """
    <h1>Forecast Price of Car</h1>
    <p> </p>
    <p>Inputs:</p>
    <p>- Year:    %s </p>
    <p>- Mileage: %s </p>
    <p>- State:   %s </p>
    <p>- Make:    %s </p>
    <p>- Model:   %s </p>
    <p> </p>
    <p>Results:   %s </p>
    """%(year,mileage,state,make,model,forecast)




#   return {
#        
#       "Year" : year,
#       "Mileage": mileage,
#       "State": state,
#       "Make": make,
#       "Model": model,
#       
#       "Forecast Price of Car": predict_price(year,mileage,state,make,model)
#       }, 200

#@app.route('/')
#def home():
#    
#    return render_template('home.html')
#
##@app.route('/hola', methods=['GET'])
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

