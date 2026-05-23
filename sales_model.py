import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Ads':[1000,1500,2000,2500,3000,3500,4000],
    'Sales':[16000,14000,12000,10000,8000,6000,4000]
}

df = pd.DataFrame(data)

X = df[['Ads']]
y = df['Sales']

model = LinearRegression()
model.fit(X,y)

def predict_sales(ads):
    prediction = model.predict([[ads]])
    return prediction[0]