import numpy as np
from numpy.random import logistic
from pandas.core.tools.datetimes import to_datetime
import sklearn.linear_model
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data, test
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import os
import cv2
import joblib
import time
rockpaperscissors = 'D:/Documents/codingu/rockpaperscissors/images/'
categories = ['rock/','paper/','scissors/','nothing/']
x = []
y = []
trainimages = []
for i in categories:
    path = rockpaperscissors + i
    for j in os.listdir(path):
        trainimages.append(path + j)
        img = cv2.imread(path + j)
        # img = cv2.resize(img,(64,64,3))
        x.append(img.flatten())
        y.append(categories.index(i))
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)
train_x = np.array(train_x) / 255
test_x = np.array(test_x) / 255
train_y = np.array(train_y)
test_y = np.array(test_y)
print(train_x.shape)
print(train_y.shape)
print(train_x[0],train_x.shape,train_y[0],train_y,train_y.shape)
print(test_x[0],test_x.shape,test_y[0],test_y,test_y.shape)

# creating the model
model = sklearn.linear_model.LogisticRegression()
print('model creation')
model.fit(train_x,train_y)
print('model trained')
joblib.dump(model,"rockpaperscissors.pkl")
print('model saved')
prediction = model.predict(test_x)
print(metrics.confusion_matrix(test_y,prediction))
print(metrics.accuracy_score(test_y,prediction))
