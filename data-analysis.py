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

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(unrate.loc[0:11, "DATE"], unrate.loc[0:11, "VALUE"])
ax2 = fig.add_subplot(2,1,2)
ax2.plot(unrate.loc[12:23, "DATE"], unrate.loc[12:23, "VALUE"])
plt.show()

