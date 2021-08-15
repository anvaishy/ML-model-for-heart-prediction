import numpy as np
import pickle
from flask import Flask, request, render_template
model = pickle.load(open('model.pkl', 'rb')) 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('frontpage.html')

@app.route('/predict', methods =['POST'])
def predict():
    
     
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)
    output = prediction
    
    if output == 1:
        return render_template('frontpage.html', 
                               result = 'The patient is not likely to have heart disease and maintain current health!')
    else:
        return render_template('frontpage.html', 
                               result = 'The patient is likely to have heart disease and must consult a doctor for diagnosis!')

if __name__ == '__main__':
    app.run()
    
    