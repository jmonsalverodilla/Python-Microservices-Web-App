import requests
import html_to_json
import json

# URL = "https://modelo-prueba.herokuapp.com/result"
url = "http://localhost:5000/predict"
columns = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'CentralAir', 'FireplaceQu', 'BsmtFinSF1', 'LotArea', 'GarageCars', 'YearBuilt', 'KitchenQual']
values = [1, 1710, '1000', 'Y', 'NaN', 706, 8450, 2, 2003, 'Gd']
data = dict(zip(columns, values))
print(data)

####################Requests###############################
try:
    r = requests.post(url, data=data)
    dict = json.loads(html_to_json.convert(r.content)['_value'])
    result = dict['model_output']
    status = dict['status']
    print(result) ; print(status)
except:
    print("Cannot connect")