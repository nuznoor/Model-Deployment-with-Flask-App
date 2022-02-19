from flask import Flask,request,jsonify
import joblib
import pandas as pd

## CREATE FLASK APP
# note that there's 2 underscores on each side
app = Flask(__name__)
## CONNECT POST API CALL ---> predict () Function

## calls flask app and tells to route to predict 
## http://localhost:5000/predict
## We are expecting that if you go to predict, 
## then you should be able to post something
@app.route('/predict', methods=['POST'])
def predict():
    ## GET JSON REQUEST
    ## when we are using api, we send request object
    ## request object is going to have json in it
    ## and we are sending it to predict
    feat_data = request.json
    
    
    ## CONVERT JSON TO PANDAS DF 
    df = pd.DataFrame(feat_data)
    #(make sure colnames match)
    df = df.reindex(columns=col_names)

    ## PREDICT
    ## model and col names are not defined
    ## will be defined down below
    prediction = list((model.predict(df)))
    
    ## RETURN PREDICTION AS JSON
    return jsonify({'prediction':str(prediction)}) 

## LOAD MY MODEL AND LOAD COLUMN NAMES
if __name__ == '__main__':
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('col_names.pkl')
    
    ## in case we make typo, much easier to debug
    app.run(debug=True)