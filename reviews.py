# add your code here
import pandas as pd

# Path to the zipped CSV file
file_path = 'data/winemag-data-130k-v2.csv.zip'

# Reading the zipped CSV file
data = pd.read_csv(file_path, compression='zip')

# Grouping the data by 'country' and calculating the needed statistics
summary = data.groupby('country').agg(
    count=('country', 'size'),  # Counts the number of reviews per country
    points=('points', 'mean')   # Computes the average points per country
)

# Rounding the points to one decimal place
summary['points'] = summary['points'].round(1)

# Path for the output CSV file
output_file_path = 'data/reviews-per-country.csv'

# Writing the summary DataFrame to a CSV file
summary.to_csv(output_file_path)
