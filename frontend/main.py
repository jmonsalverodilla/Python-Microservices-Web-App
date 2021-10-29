#imports
from flask import Flask, render_template, request
import os
import requests
import html_to_json
import json

#Flask app
app = Flask(__name__)

#Primer html: insertar los datos
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
  values = list(request.form.values())
  columns = ['OverallQual','GrLivArea','TotalBsmtSF','CentralAir','FireplaceQu','BsmtFinSF1','LotArea','GarageCars','YearBuilt','KitchenQual']
  print(values)
  print(columns)
  data_dict = dict(zip(columns,values))
  #url = "http://127.0.0.1:5000/predict"
  backend_port = os.environ.get("BACKEND_PORT")
  url = f"http://backend:{backend_port}/predict"
  try:
    r = requests.post(url, data=data_dict)
    dict_output = json.loads(html_to_json.convert(r.content)['_value'])
    result = dict_output['model_output']
    status = dict_output['status']
  except:
    result = "The frontend could not connect to the backend."
    status = 'Something went wrong!'

  #if isinstance(result,float):# != 'Errors making prediction:Check the data type of each input variable. Make sure all numeric columns are positive.'
  if any(str.isdigit(c) for c in result):
    print("Without errors")
    return render_template("result.html",output1 = "Estimated house price:" ,output2 = result, status = status)

  else:
    print("With errors")
    return render_template("index.html", output_errors = result, status = status)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__=="__main__":
  frontend_port = os.environ.get("$FRONTEND_PORT")
  app.run(debug=False, host="0.0.0.0",port=frontend_port)
  #app.run(debug=True, port=port)