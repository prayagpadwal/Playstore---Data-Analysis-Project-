import pandas as pd
import numpy as np
from numpy import nan

df = pd.DataFrame

# Read file
file = pd.read_csv(r"C:\.PRAYAG\LiveProject_LinkedIn\playstore_apps.csv",index_col='App')

# Remove Duplicate data
file.drop_duplicates(keep=False, inplace=True)
file.info() 

# category column
print(file['Category'].unique()) # unique values in category column
print(file[file['Category']=='1.9'])
file.drop("Life Made WI-Fi Touchscreen Photo Frame", inplace=True)
print(file['Category'].unique()) # Check if irrelevant values are removed


# Remove 'M' from size column
# df['Size'] = df['Size'].astype(str).str[:-2].astype(np.int64)

# Remove all the cells having NULL values
df = df.dropna(how='any',axis=0)

#Export the cleaned dataset as a .csv file and prepare the data using excel.
file.to_csv("C:\.PRAYAG\LiveProject_LinkedIn\Folder Edits\cleaned_file.csv")