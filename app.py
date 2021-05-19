import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('linear_hire_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features)
    output = model.predict([final_features])[0][0].round(2)

    return render_template('index.html', prediction_text='Employee  Salary  should  be  $ {} if  they  compleate  the  Prerequist '.format(output))


if __name__ == "__main__":
    app.run(debug=True)