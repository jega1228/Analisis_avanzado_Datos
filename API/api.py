#!/usr/bin/python
from flask import Flask, request
from m09_model_deployment import predict_price

app = Flask(__name__)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        year = request.form.get('year')
        mileage = request.form.get('mileage')
        state = request.form.get('state')
        make = request.form.get('make')
        model = request.form.get('model')
        
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
 
            <a href="/form-example">Back</a>

            """%(year,mileage,state,make,model,forecast)
    
    return """
          <h1>Forecast Price of Car</h1>
          <p> </p>    
          <form method="POST">
              <div><label>Year: <input type="text" name="year"></label></div>
              <div><label>Mileage: <input type="text" name="mileage"></label></div>
              <div><label>State: <input type="text" name="state"></label></div>
              <div><label>Make: <input type="text" name="make"></label></div>
              <div><label>Model: <input type="text" name="model"></label></div>
              <input type="submit" value="Submit">
          </form>"""

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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

    
#            <button onclick="goBack()">Go Back</button>
#            <script>
#            function goBack() {window.history.back();}
#            </script>
