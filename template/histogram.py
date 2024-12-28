import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import mysql.connector
from sklearn.datasets import load_iris
import plotly.express as px
import os

# Connect to the MySQL database
cnx = mysql.connector.connect(
  user='root',
  password='PRITI@2205thube',
  host='localhost',
  database='data_db'
)

# Create a cursor object
cursor = cnx.cursor()

# Function to fetch data from the database
def fetch_data():
    try:
        # Query the data
        query = "SELECT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm,Species FROM irisi"  # Replace with your table name
        cursor.execute(query)
        print("success")
        
        # Fetch all the rows from the query
        rows = cursor.fetchall()
        
        # Create a pandas DataFrame from the rows
        data = pd.DataFrame(rows, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
        
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

# Fetch data from the database
data = fetch_data()
print(data)

# Check if data was fetched successfully
if data is not None:


# Histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(data['PetalLengthCm'], bins=5, kde=True)
    plt.title('PetalLengthCm Histogram')
    plt.xlabel('PetalLengthCm (cm)')
    plt.ylabel('Frequency')
    plt.show()
    
else:
    print("Failed to fetch data from the database.")