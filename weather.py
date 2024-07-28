import pandas as pd

data=pd.read_csv("weatherHistory.csv")



#Find all the unique wind speed values

print(data['Wind Speed (km/h)'].nunique())

print(data['Wind Speed (km/h)'].unique())

#Find all weather is clear

arr=data['Summary'] == 'Clear'

print(data[arr])


#find the number of times when the wind speed greater than 4km/h

print(data[(data['Wind Speed (km/h)']>4)])

#find out the null values in the data

print(data.isnull().sum())

print(data.notnull().sum())

#rename the column summary to Weather

data.rename(columns={'Summary':'Weather'},inplace=True)

#find the mean value of visibility

print(data['Visibility (km)'].mean())

#find the std deviation of pressure

print(data['Pressure (millibars)'].std())

#find the variance of relative humidity

print(data['Humidity'].var())

#find all the instances of Snow

print(data[data['Daily Summary'].str.contains('Snow')])


#find all instances with wind speed is above 24 and visiblity is above 25

print(data[(data['Wind Speed (km/h)'] > 24) & data['Visibility (km)']>25])

#mean value of weather condition

print(data['Temperature (C)'].mean())