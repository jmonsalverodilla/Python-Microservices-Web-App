# imports
import os
from pathlib import Path
from house_prices_regression_model.predict import make_prediction
import pandas as pd
from flask import request
from models import db, Predictions
from create_app import app

# Primer html: insertar los datos
@app.route('/')
def home():
    return "<h1>Welcome to my App!!</h1>", 200

@app.route('/predict', methods=['GET','POST'])
def predict():
    values = [list(request.form.values())]
    print(request.form)

    # Creation of dataframe
    columns = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'CentralAir', 'FireplaceQu', 'BsmtFinSF1', 'LotArea', 'GarageCars', 'YearBuilt', 'KitchenQual']
    df = pd.DataFrame(values, columns=columns)
    prediction = make_prediction(input_data=df).get('model_output')

    #Prediction can be a string (if an error was found) or a list with the prediction value/s (if no error was found)
    if isinstance(prediction,list):
        model_output = '{:,}'.format(int(prediction[0])) + " $ "
        data = Predictions(
            OverallQual=request.form['OverallQual'],
            GrLivArea=request.form['GrLivArea'],
            TotalBsmtSF=request.form['TotalBsmtSF'],
            CentralAir=request.form['CentralAir'],
            FireplaceQu=request.form['FireplaceQu'],
            BsmtFinSF1=request.form['BsmtFinSF1'],
            LotArea=request.form['LotArea'],
            GarageCars=request.form['GarageCars'],
            YearBuilt=request.form['YearBuilt'],
            KitchenQual=request.form['KitchenQual'],
            Prediction=model_output
            )
        try:
            db.session.add(data)
            db.session.commit()
            status = 'Activity recorded to database'
        except:
            status = 'Something went wrong! Could not be added to Database!' #should have been recorded but something happened
    else:
        model_output = prediction
        status = 'Something went wrong! Could not be added to Database!' #it is not recorded due to wrong column types
    return {'model_output':model_output, 'status':status}

if __name__ == "__main__":
    port = os.environ.get("BACKEND_HOST_PORT")
    app.run(debug=False, host="0.0.0.0",port = port)
    #app.run(debug=True, port=port)


