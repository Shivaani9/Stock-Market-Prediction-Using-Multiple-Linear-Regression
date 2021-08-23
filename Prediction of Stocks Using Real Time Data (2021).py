import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


#Prediction of Stock Price for Apple INC. Stocks from September 2019 to September 2020

#Import the data
data = pd.read_csv("AAPL.csv")
print('Raw data from Yahoo Finance : ')
print(data.head())

#Remove date and Adj Close columns
data = data.drop('Date',axis=1) 
data = data.drop('Adj Close',axis = 1)
print('\n\nData after removing Date and Adj Close : ')
print(data.head())

#Split into train and test data
data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())

#Creating the Regressor
regressor = LinearRegression()
regressor.fit(train_X,train_y)

#Make Predictions and Evaluate the results
predict_y = regressor.predict(test_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))
error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)

#Plot the predicted and the expected values
fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='Close ($)',ylabel='Open ($)', title='Apple Stock Prediction using Linear Regression')
ax.plot(test_X['Open'],test_y)
ax.plot(test_X['Open'],predict_y)
fig.savefig('LRPlot.png')
plt.show()


#Prediction of Stock Price for Alphabet INC.(Google) Stocks from September 2019 to September 2020

#Import the data
data = pd.read_csv("GOOG.csv")
print('Raw data from Yahoo Finance : ')
print(data.head())

#Remove date and Adj Close columns
data = data.drop('Date',axis=1) 
data = data.drop('Adj Close',axis = 1)
print('\n\nData after removing Date and Adj Close : ')
print(data.head())

#Split into train and test data
data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())

#Creating the Regressor
regressor = LinearRegression()
regressor.fit(train_X,train_y)

#Make Predictions and Evaluate the results
predict_y = regressor.predict(test_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))
error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)

#Plot the predicted and the expected values
fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='Close ($)',ylabel='Open ($)', title='Google Stock Prediction using Linear Regression')
ax.plot(test_X['Open'],test_y)
ax.plot(test_X['Open'],predict_y)
fig.savefig('LRPlot.png')
plt.show()


#Prediction of Stock Price for Microsoft Corp. (MSFT) Stocks from September 2019 to September 2020

#Import the data
data = pd.read_csv("MSFT.csv")
print('Raw data from Yahoo Finance : ')
print(data.head())

#Remove date and Adj Close columns
data = data.drop('Date',axis=1) 
data = data.drop('Adj Close',axis = 1)
print('\n\nData after removing Date and Adj Close : ')
print(data.head())

#Split into train and test data
data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())

#Creating the Regressor
regressor = LinearRegression()
regressor.fit(train_X,train_y)

#Make Predictions and Evaluate the results
predict_y = regressor.predict(test_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))
error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)

#Plot the predicted and the expected values
fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='Close ($)',ylabel='Open ($)', title='Microsoft Stock Prediction using Linear Regression')
ax.plot(test_X['Open'],test_y)
ax.plot(test_X['Open'],predict_y)
fig.savefig('LRPlot.png')
plt.show()

#Prediction of Stock Price for Amazon INC. (AMZN) Stocks from September 2019 to September 2020

#Import the data
data = pd.read_csv("AMZN.csv")
print('Raw data from Yahoo Finance : ')
print(data.head())

#Remove date and Adj Close columns
data = data.drop('Date',axis=1) 
data = data.drop('Adj Close',axis = 1)
print('\n\nData after removing Date and Adj Close : ')
print(data.head())

#Split into train and test data
data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())

#Creating the Regressor
regressor = LinearRegression()
regressor.fit(train_X,train_y)

#Make Predictions and Evaluate the results
predict_y = regressor.predict(test_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))
error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)

#Plot the predicted and the expected values
fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='Close ($)',ylabel='Open ($)', title='Amazon Stock Prediction using Linear Regression')
ax.plot(test_X['Open'],test_y)
ax.plot(test_X['Open'],predict_y)
fig.savefig('LRPlot.png')
plt.show()


#Prediction of Stock Price for Tesla INC. Stocks from September 2019 to September 2020

#Import the data
data = pd.read_csv("TSLA.csv")
print('Raw data from Yahoo Finance : ')
print(data.head())

#Remove date and Adj Close columns
data = data.drop('Date',axis=1) 
data = data.drop('Adj Close',axis = 1)
print('\n\nData after removing Date and Adj Close : ')
print(data.head())

#Split into train and test data
data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())

#Creating the Regressor
regressor = LinearRegression()
regressor.fit(train_X,train_y)

#Make Predictions and Evaluate the results
predict_y = regressor.predict(test_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))
error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)

#Plot the predicted and the expected values
fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='Close ($)',ylabel='Open ($)', title='Tesla Stock Prediction using Linear Regression')
ax.plot(test_X['Open'],test_y)
ax.plot(test_X['Open'],predict_y)
fig.savefig('LRPlot.png')
plt.show()
