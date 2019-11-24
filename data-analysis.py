# Monthly unemployment rate as a CSV file from January 1948 to August 2016 - data is saved as unrate.csv
# Read the CSV file into pandas to explore the table representation of this data

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))

# we'll use the matplotlib library, which allows us to quickly create common plots using high-level functions,
# extensively tweak plots, and create new kinds of plots from the ground up

# create plot using data
# customize the appearance of the plot
# display the plot
# edit and repeat until satisfied

# Generate a line chart that visualizes the unemployment rates for 1948
# plt.plot(unrate.loc[0:11, "DATE"], unrate.loc[0:11, "VALUE"])
# # Rotate the x-axis tick labels by 90 degrees.
# plt.xticks(rotation=90)
# # Set the x-axis label to "Month".
# plt.xlabel("Month")
# # Set the y-axis label to "Unemployment Rate".
# plt.ylabel("Unemployment Rate")
# plt.title("Monthly Unemployment Trends, 1948")

unrate['MONTH'] = unrate['DATE'].dt.month
# Let's visualize 5 years worth of unemployment rates on the same subplot.
# Set the plotting area to a width of 10 inches and a height of 6 inches.
plot = plt.figure(figsize=(10, 6))
# Generate the  plots in the base subplot using loops
colors = ["red", "blue", "green", "orange", "black"]
# Set the years for the labels
years = ["1948", "1949", "1950", "1951", "1952"]

for i in range(0,5):
    plt.plot(unrate.loc[(i*12):(i*12+11), "MONTH"], unrate.loc[(i*12):(i*12+11), "VALUE"], c=colors[i], label=years[i])
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()

#TODO: More analysis and plots based on the dataset - review for interesting problems to answer