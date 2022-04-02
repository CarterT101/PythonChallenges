import numpy
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import pandas
from sklearn import linear_model, tree
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pydotplus


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)  # outputs tuple

z1 = list(z)  # convert tuple into list

print("Mean: " + str(x) + "\nMedian: " + str(y) + "\nMode: " + str(z1[0][0]))

x = numpy.std(speed)  # standard deviation
y = x*x  # variance is square root of standard deviation
print("Standard deviation: ", x, "\nVariance: ", y)

# another way to calculate variance

meanspeed = numpy.mean(speed)  # find mean

difflist = []
squarevalue = []

for s in speed:
    diff = s - meanspeed
    difflist.append(diff)
    for d in difflist:
        square = d ** 2
        squarevalue.append(square)

variance = sum(squarevalue) / len(squarevalue)

print("This is the calculated variance:", variance)

variance1 = numpy.var(speed)

print("This is the easier way: ", variance1)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)  # the 75th percentile. the answer being 43, meaning 75% of the people are 43 or younger
print(x)

randomfloats = numpy.random.uniform(0.0, 5.0, 1000)  # creating an array containing 1000 floats between 0 and 5
                                   # low, high, size
"""
print(randomfloats)  # prints random float created
plt.hist(randomfloats, 25)  # visual the data set to draw a histogram. 25 meaning 25 bars
plt.show()  # command to show graph
"""


randomfloats1 = numpy.random.normal(5.0, 1.0, 100000)  # mean value is 5.0, standard deviation is 1.0, 100000 values

"""
plt.hist(randomfloats1, 100)  # 100 bars
plt.show()
"""


# scatter plot needs two arrays equal in length
carage = [5,7,8,7,2,17,2,9,4,11,12,9,6]  # represents age of car

carspeed = [99,86,87,88,111,86,103,87,94,78,77,85,86]  # represents speed of car

# method that returns import key values of linear regression
slope, intercept, r, p, std_err = stats.linregress(carage, carspeed)
# the relationship, the coefficient of correlation, is called 'r'

print("Relationship: ", r)  # prints -.76, not perfect relationship, but close
                            # a bad relationship would be .013, not suitable for linear regression, prediction

# function that uses slope and intercept values to return a new value
# represents where on the y-axis (carspeed) the corresponding x value (carage) will be placed
def myslope(carage):
    return slope * carage + intercept

# run each value of the x array through the function, will result in new array with new values for y-axis
mymodel = list(map(myslope, carage))

"""
plt.scatter(carage, carspeed)  # scatter plot
plt.plot(carage, mymodel)  # linear regreesion line
plt.show()  # display diagram
"""



car1 = myslope(10)  # predicting the speed of a car that is 10 years old

print("Prediction of the speed of a car that is 10 years old: " + str(car1))

mymodel1 = numpy.poly1d(numpy.polyfit(carage, carspeed, 3))
# makes the polynomial model, 3 is the degree to be made fit

myline = numpy.linspace(1, 22, 100)
# specify how the line will display, start at position 1, end at position 22

"""
plt.scatter(carage, carspeed)  # draw scatter plot
plt.plot(myline, mymodel1(myline))  # draw line of polynomial regression
plt.show()
"""

print(r2_score(carspeed, mymodel1(carage)))  # output is .88, which means it has a good relationship
# r-squared finder for relationship, y = carspeed, x = carage

car2 = mymodel1(17)  # prediction
print(car2)


# pandas module allows us to read csv files and return a DataFrame object
df = pandas.read_csv("cars.csv")

# independent values, common practice to have independent values with upper case, dependent with lower case
indvalues = df[['Weight', 'Volume']]
# dependent values
depvalues = df['CO2']

# LinearRegression method to create linear regression object
# this method has fit() method that takes independent and dependent values and fills regression object
# with data that describes the relationship
regr = linear_model.LinearRegression()
regr.fit(indvalues.values, depvalues)  # .values gets rid of error 'valid feature names'

# now we have regression object ready to predict CO2 values based on car weight and volume
# weight is 2300kg, volume is 1300cm^3
predictedCO2 = regr.predict([[2300, 1300]])

print("Predicted CO2: " + str(predictedCO2))

# coefficient value of weight against CO2 and for volume against CO2
print("Coefficient values of regression object: " + str(regr.coef_))
# tells us what would happen if we increase, decrease, one of the independent values
# if we increase the weight by 1kg, the CO2 emission increases by the coefficient given
# if the volume size increase by 1cm^3, the CO2 emission will increase by coefficient given

# increased by 1000kg
predictedCO2 = regr.predict([[3300, 1300]])

print("Predicted CO2 increased by 1000kg: " + str(predictedCO2))

# scaling all values in the weight and volume columns
scale = StandardScaler()
df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]  # independent values to predict CO2
y = df['CO2']  # dependent value trying to predict

scaledX = scale.fit_transform(X)
regr = linear_model.LinearRegression()  # creating model
regr.fit(scaledX, y)

# precict CO2 emission from 1.3 liter car that weighs 2300kg
scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print("Predicted CO2 from different values: ", predictedCO2)

# print(scaledX)  # prints scaled values

numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel2 = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))  # line of polynomial regression

myline1 = numpy.linspace(0, 6, 100)

r2 = r2_score(train_y, mymodel2(train_x))
print("Relationship of Training set: " + str(r2))  # output is .799 which is okay
r2 = r2_score(test_y, mymodel2(test_x))
print("Relationship of Testing set: " + str(r2))  # output is .809 which means it fits well
print(mymodel2(5))  # predicting if they stay in shop for 5 minutes
"""
plt.scatter(train_x, train_y)  # fitting the data set, drawing a line of polynomial regression
plt.plot(myline1, mymodel2(myline1))
plt.show()
"""

"""
plt.scatter(test_x, test_y)  # display testing set
plt.show()
"""
"""
plt.scatter(train_x, train_y)  # display training set
plt.show()
"""
"""
plt.scatter(x,y)  # display normal scatter plot
plt.show()
"""






