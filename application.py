import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import webbrowser
from threading import Timer
import os

application = Flask(__name__)
app = application


ridge_model = pickle.load(open('pickle_models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('pickle_models/scaler.pkl', 'rb'))

# Column names used for scaler/model
columns = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region']

# Route for welcome page
@app.route("/")
def index():
    return render_template('index.html')

# Route for input form and prediction
@app.route("/home", methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == "POST":
        try:
            Temperature = float(request.form.get('Temperature', 0))
            RH = float(request.form.get('RH', 0))
            Ws = float(request.form.get('Ws', 0))
            Rain = float(request.form.get('Rain', 0))
            FFMC = float(request.form.get('FFMC', 0))
            DMC = float(request.form.get('DMC', 0))
            ISI = float(request.form.get('ISI', 0))
            Classes = float(request.form.get('Classes', 0))
            Region = float(request.form.get('Region', 0))

            input_df = pd.DataFrame([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
                                    columns=columns)
            
            scaled_input = standard_scaler.transform(input_df)

            # Predict using Ridge model
            prediction = ridge_model.predict(scaled_input)

            # Clip negative predictions to 0
            prediction = max(prediction[0], 0)

            result = round(prediction, 2)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('home.html', result=result)


if __name__ == "__main__":
    port = 5000
    url = f"http://127.0.0.1:{port}/"

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        Timer(1, lambda: webbrowser.open(url)).start()

    app.run(host="0.0.0.0", port=port, debug=True)
