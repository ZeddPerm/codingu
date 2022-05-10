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

# df = pd.read_csv('D:/Downloads/diabetes2.csv')
# # print(df.isnull().any())
# x = df.iloc[:,0:8]
# y = df['Outcome'][:]
# X_train, X_test, Y_train, test_y = train_test_split(x, y, test_size=0.2)
# plt.scatter(df['BloodPressure'][:],y)
# plt.show()
# model = sklearn.linear_model.LogisticRegression()
# model.fit(X_train,Y_train)
# prediction = model.predict(X_test)
# df2 = pd.DataFrame({'actual_y':test_y[:10],'predicted_y':prediction[:10]})
# print(metrics.confusion_matrix(test_y,prediction))
# print(metrics.accuracy_score(test_y,prediction))
# falsepos,truepos,_ = metrics.roc_curve(test_y,prediction)
# plt.plot(falsepos,truepos)
# print(metrics.roc_auc_score(test_y,prediction))
# plt.show()

# df = pd.read_csv('D:/Documents/codingu/suv_data.csv')
# df['Gender'] = df['Gender'].map({'Male':0,'Female':1})
# x = df.iloc[:,1:3]
# y = df['Purchased'][:]
# X_train, X_test, Y_train, test_y = train_test_split(x, y, test_size=0.2)
# model = sklearn.linear_model.LogisticRegression()
# model.fit(X_train,Y_train)
# prediction = model.predict(X_test)
# df2 = pd.DataFrame({'actual_y':test_y[:10],'predicted_y':prediction[:10]})
# print(metrics.confusion_matrix(test_y,prediction))
# print(metrics.accuracy_score(test_y,prediction))
# falsepos,truepos,_ = metrics.roc_curve(test_y,prediction)
# plt.plot(falsepos,truepos)
# print(metrics.roc_auc_score(test_y,prediction))
# plt.show()

# df = pd.read_csv('D:/Documents/codingu/SMSSpamCollection.txt',sep='	')
# df['Label'] = df['Label'].map({'spam':0,'ham':1})
# x = df['Text'][:]
# y = df['Label'][:]
# X_train, X_test, Y_train, test_y = train_test_split(x, y, test_size=0.2)
# # vector = CountVectorizer()
# # vector.fit(X_train)
# # # print(vector.get_feature_names())
# # X_train = vector.transform(X_train)
# # X_test = vector.transform(X_test)
# vector = TfidfVectorizer(stop_words='english')
# vector.fit(X_train)
# X_train = vector.transform(X_train)
# X_test = vector.transform(X_test)
# model = sklearn.linear_model.LogisticRegression(max_iter=5000)
# model.fit(X_train,Y_train)
# prediction = model.predict(X_test)
# df2 = pd.DataFrame({'actual_y':test_y[:10],'predicted_y':prediction[:10]})
# print(metrics.confusion_matrix(test_y,prediction))
# print(metrics.accuracy_score(test_y,prediction))
# falsepos,truepos,_ = metrics.roc_curve(test_y,prediction)
# plt.plot(falsepos,truepos)
# print(metrics.roc_auc_score(test_y,prediction))
# plt.show()

# trainingpath = 'D:/Documents/codingu/archive (5)/dog vs cat/dataset/training_set/'
# testpath = 'D:/Documents/codingu/archive (5)/dog vs cat/dataset/test_set/'
# categories = ['cats/','dogs/']
# trainimages = []
# testimages = []
# train_x = []
# train_y = []
# test_x = []
# test_y = []
# for i in categories:
#     path = trainingpath + i
#     for j in os.listdir(path):
#         trainimages.append(path + j)
#         img = cv2.cvtColor(cv2.imread(path + j),cv2.COLOR_BGR2GRAY)
#         img = cv2.resize(img,(64,64))
#         train_x.append(img.flatten())
#         train_y.append(categories.index(i))
# print('training set loaded')
# for i in categories:
#     path = testpath + i
#     for j in os.listdir(path):
#         testimages.append(path + j)
#         img = cv2.cvtColor(cv2.imread(path + j),cv2.COLOR_BGR2GRAY)
#         img = cv2.resize(img,(64,64))
#         test_x.append(img.flatten())
#         test_y.append(categories.index(i))
# print('test set loaded')
# internetdog = cv2.resize(cv2.cvtColor(cv2.imread('D:/Documents/codingu/Yellow-Labrador-Retriever.jpg'),cv2.COLOR_BGR2GRAY),(64,64)).flatten()
# # abcd = cv2.imread('D:/Documents/codingu/Yellow-Labrador-Retriever.jpg')
# # abcd = cv2.cvtColor(abcd,cv2.COLOR_BGR2GRAY)
# # print(np.shape(abcd))
# # cv2.imshow('a',abcd)
# # cv2.waitKey()
# # cv2.destroyAllWindows()
# train_x = np.array(train_x)
# train_y = np.array(train_y)
# test_x = np.array(test_x)
# test_y = np.array(test_y)
# testingimages = []
# model = joblib.load('graycatsanddogs.pkl')
# prediction = model.predict(test_x)
# # for i in range(10):
# #     testingimages.append(test_x[np.random.randint(0,len(test_x)-1)])
# # for i in testingimages:
# #     i = i.reshape(1,-1)
# #     prediction = model.predict(i)
#     # if prediction:
#     #     plt.title('Dog')
#     # elif not prediction:
#     #     plt.title('Cat')
#     # i = i.reshape(64,64,3)
#     # plt.imshow(i)
#     # plt.show()
# internetdog = internetdog.reshape(1,-1)
# prediction = model.predict(internetdog)
# if prediction:
#     plt.title('Dog')
# elif not prediction:
#     plt.title('Cat')
# internetdog = internetdog.reshape(64,64)
# plt.imshow(internetdog)
# plt.show()
# print(train_x[0],train_x.shape,train_y[0],train_y,train_y.shape)
# model = sklearn.linear_model.LogisticRegression()
# print('model creation')
# model.fit(train_x,train_y)
# print('model trained')
# joblib.dump(model,"graycatsanddogs.pkl")
# print('model saved')
# prediction = model.predict(test_x)
# print(metrics.confusion_matrix(test_y,prediction))
# print(metrics.accuracy_score(test_y,prediction))

# trainingpath = 'D:/Documents/codingu/messyvsclean/images/train/'
# testpath = 'D:/Documents/codingu/messyvsclean/images/val/'
# categories = ['messy/','clean/']
# trainimages = []
# testimages = []
# train_x = []
# train_y = []
# test_x = []
# test_y = []

# for i in categories:
#     path = trainingpath + i
#     for j in os.listdir(path):
#         trainimages.append(path + j)
#         # img = cv2.cvtColor(cv2.imread(path + j),cv2.COLOR_BGR2GRAY)
#         img = cv2.imread(path + j)
#         img = cv2.resize(img,(64,64))
#         train_x.append(img.flatten())
#         train_y.append(categories.index(i))
# print('training set loaded')

# for i in categories:
#     path = testpath + i
#     for j in os.listdir(path):
#         testimages.append(path + j)
#         # img = cv2.cvtColor(cv2.imread(path + j),cv2.COLOR_BGR2GRAY)
#         img = cv2.imread(path + j)
#         img = cv2.resize(img,(64,64))
#         test_x.append(img.flatten())
#         test_y.append(categories.index(i))
# print('test set loaded')

# train_x = np.array(train_x) / 255
# test_x = np.array(test_x) / 255
# train_y = np.array(train_y)
# test_y = np.array(test_y)
# # print(train_x[0],train_x.shape,train_y[0],train_y,train_y.shape)
# print(test_x[0],test_x.shape,test_y[0],test_y,test_y.shape)
# # model = joblib.load('graycatsanddogs.pkl')
# # prediction = model.predict(test_x)
# testingimages = []

# # for i in range(10):
# #     testingimages.append(cv2.resize(cv2.imread('D:/Documents/codingu/messyvsclean/images/test' + f'/{i}.png'),(64,64)))
# # for i in testingimages:
# #     plt.imshow(i)
# #     i = i.reshape(1,-1)
# #     prediction = model.predict(i)
# #     if prediction:
# #         plt.title('Clean')
# #     elif not prediction:
# #         plt.title('Messy')
# #     plt.show()

# # Creating the model and saving
# model = sklearn.linear_model.LogisticRegression()
# print('model creation')
# model.fit(train_x,train_y)
# print('model trained')
# # joblib.dump(model,"messyvsclean.pkl")
# # print('model saved')
# prediction = model.predict(test_x)
# print(metrics.confusion_matrix(test_y,prediction))
# print(metrics.accuracy_score(test_y,prediction))

# df = pd.read_csv('D:/Documents/codingu/Iris.csv')
# x = df.iloc[:,1:5]
# y = df[:]['Species'].map({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})
# # print(y.head())
# train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)
# # print(test_x)
# model = sklearn.linear_model.LogisticRegression()
# model.fit(train_x,train_y)
# prediction = model.predict(test_x)
# test_eye = model.predict(np.array([5.1,3,1.7,0.9]).reshape(1,-1))
# print(test_eye)
# df2 = pd.DataFrame({'actual_y':test_y[:10],'predicted_y':prediction[:10]})
# print(metrics.confusion_matrix(test_y,prediction))
# print(metrics.accuracy_score(test_y,prediction))

# catdogpandas = 'D:/Documents/codingu/archive (6)/'
# categories = ['cats/','dogs/','panda/']
# x = []
# y = []
# trainimages = []
# for i in categories:
#     path = catdogpandas + i
#     for j in os.listdir(path):
#         trainimages.append(path + j)
#         img = cv2.imread(path + j)
#         img = cv2.resize(img,(64,64))
#         x.append(img.flatten())
#         y.append(categories.index(i))
# train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)
# train_x = np.array(train_x) / 255
# test_x = np.array(test_x) / 255
# train_y = np.array(train_y)
# test_y = np.array(test_y)
# print(train_x.shape)
# print(train_y.shape)
# print(train_x[0],train_x.shape,train_y[0],train_y,train_y.shape)
# print(test_x[0],test_x.shape,test_y[0],test_y,test_y.shape)

# model = joblib.load('catsanddogsandpandas.pkl')
# testingimages = []
# for i in range(10):
#     testingimages.append(test_x[np.random.randint(0,len(test_x)-1)])
# for i in testingimages:
#     i = i.reshape(1,-1)
#     prediction = model.predict(i)
#     if prediction:
#         plt.title('Dog')
#     elif not prediction:
#         plt.title('Cat')
#     else:
#         plt.title('Panda')
#     i = i.reshape(64,64,1)
#     plt.imshow(i)
#     plt.show()

## # creating the model
## model = sklearn.linear_model.LogisticRegression(max_iter=500)
## print('model creation')
## model.fit(train_x,train_y)
## print('model trained')
## joblib.dump(model,"catsanddogsandpandas.pkl")
## print('model saved')
## prediction = model.predict(test_x)
## print(metrics.confusion_matrix(test_y,prediction))
## print(metrics.accuracy_score(test_y,prediction))
