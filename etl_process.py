import pandas as pd

## Extraction Process
## First we read all the csv files and extract all the data, assigning each of them to individual dataframes.
customer = pd.read_csv (r"Customer_ID_Superstore.csv")
order = pd.read_csv (r"final_Superstore.csv")
product = pd.read_csv (r"Product_ID_Superstore.csv")

## Transform Process
## We combine the order and customer dataframes to give us a detailed order df, containing the details of the customer.
## We do this by using the merge command in pandas which function like the join function in SQL.
order_cust = pd.merge(order, customer)
## We further combine the previous dataset with the product df to give us the complete details of the orders.
complete_data = pd.merge(order_cust, product)
## Now that we have the complete data, we would like to filter rows that contain null values.
complete_data = complete_data.dropna()
## After making sure that the data has no null values, we remove duplicates from the data.
complete_data = complete_data.drop_duplicates()
## order based on row_id
complete_data = complete_data.sort_values(by='row_id')

## There are multiple ways for us to sort this dataframe, which includes:
## sort based on ship mode
first_class = complete_data.loc[(complete_data['ship_mode'] == 'First Class')]
second_class = complete_data.loc[(complete_data['ship_mode'] == 'Second Class')]
standard_class = complete_data.loc[(complete_data['ship_mode'] == 'Standard Class')]
## sort based on category
furniture = complete_data.loc[(complete_data['category'] == 'Furniture')]
office = complete_data.loc[(complete_data['category'] == 'Office Supplies')]
technology = complete_data.loc[(complete_data['category'] == 'Technology')]
## sort based on region
north = complete_data.loc[(complete_data['region'] == 'North')]
south = complete_data.loc[(complete_data['region'] == 'South')]
east = complete_data.loc[(complete_data['region'] == 'East')]
west = complete_data.loc[(complete_data['region'] == 'West')]
central = complete_data.loc[(complete_data['region'] == 'Central')]
## and many other options


## Loading Process
complete_data.to_csv('transformed_data.csv', index= 0)