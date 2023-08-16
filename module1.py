import numpy as np
import pickle
from flask import Flask
from flask import request,render_template
app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
model=pickle.load(open("heart_model.pkl","rb"))
model=pickle.load(open("parkinson_model.pkl","rb"))
@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction1=model1.predict(features)
    prediction2=model2.predict(features)
    prediction3=model3.predict(features)
    return render_template("index.html",f"prediction_text:{prediction1},{prediction2},{prediction3}")

if __name__=="__main__":
    app.run(debug=True)
