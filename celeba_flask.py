import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('Celeba_Model.joblib')

@app.route('/')
def home():
    return render_template('celeba_index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = np.round(prediction) 

    return render_template('celeba_index.html', prediction_text='Your Value Of Pale_Skin & Smilling Are :- {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)