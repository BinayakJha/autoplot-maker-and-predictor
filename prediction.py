
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from pyautogui import prompt, alert, confirm
def predicts(df,X,y,x_label,y_label):
    model = LinearRegression()
    model.fit(df[[X]], df[[y]])
    # ask a value to predict
    predict_value = prompt(text = 'Please enter a value  of '+str(x_label)+' to predict '+str(y_label) , title = 'Predict')
    predict = model.predict([[predict_value]])
    confirm(text = 'Predicted value of '+ str(y_label)+ ' is ' + str(int(predict)) , title = 'Predict')