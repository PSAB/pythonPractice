import pandas as pd


csv_path = 'income_data.csv'
# '/income_data.csv'

# pandas allows you to work with data using a dataframe made of rows and columns
df = pd.read_csv(csv_path)

# print(df)
# print(df.head()) # This function prints the first five rows

# We can also create a dataframe out of a dictionary
# keys are the table headers, values are the rows of the table

songs_dict = {'Album': ['Thriller', 'Back in Black', 'THe Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell'], 'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33'], 'Released': ['1982', '1980', '1973', '1992', '1977']}
songs_df = pd.DataFrame.from_dict(songs_dict) # take the dictionary and convert it to a pandas dataframe
print(str(songs_df) + "\n\n")

# Accessing only the first 2 rows of the data set [row selection, column selection]
two_rows_df = songs_df.iloc[0:2]
# print(two_rows_df)

# Accessing the second column data of the first row
thriller_length = songs_df.iloc[0, 1]
#print(thriller_length)











