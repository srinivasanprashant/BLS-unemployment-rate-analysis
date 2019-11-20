# Monthly unemployment rate as a CSV file from January 1948 to August 2016 - data is saved as unrate.csv
# Read the CSV file into pandas to explore the table representation of this data

import pandas as pd

unrate = pd.read_csv("unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))


