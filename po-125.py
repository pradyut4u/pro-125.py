from flask import Flask,jsonify,request
from imageprediction import prediction

app = Flask(__name__)

@app.route("/predict",methods = ["POST"])
def predict():
    image = request.files.get("digit")
    prediction1 = prediction(image)
    return jsonify({
        "message" : "Predicted",
        "prediction" : prediction1
    })
    
if(__name__=="__main__"):
    app.run(debug = True)