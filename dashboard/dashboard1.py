import streamlit as st # type: ignore
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import mysql.connector

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
        query = "SELECT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species FROM irisi"  # Replace with your table name
        cursor.execute(query)
        
        # Fetch all the rows from the query
        rows = cursor.fetchall()
        
        # Create a pandas DataFrame from the rows
        data = pd.DataFrame(rows, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
        
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Fetch data from the database
data = fetch_data()

# Check if data was fetched successfully
if data is not None:
    st.title("Iris Dataset Dashboard")

    # Show the data as a table
    st.write("### Data Preview:")
    st.dataframe(data.head())

    # Bar Graph
    st.write("### Species Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='Species', data=data, ax=ax)
    ax.set_title('Species Distribution')
    ax.set_xlabel('Species')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    # Histogram
    st.write("### Petal Length Histogram")
    fig, ax = plt.subplots()
    sns.histplot(data['PetalLengthCm'], bins=5, kde=True, ax=ax)
    ax.set_title('PetalLengthCm Histogram')
    ax.set_xlabel('PetalLengthCm (cm)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Line Graph
    st.write("### PetalWidthCm vs Index")
    fig, ax = plt.subplots()
    sns.lineplot(x=data.index, y='PetalWidthCm', data=data, ax=ax)
    ax.set_title('PetalWidthCm vs Index')
    ax.set_xlabel('Index')
    ax.set_ylabel('PetalWidthCm')
    st.pyplot(fig)

    # Point Graph
    st.write("### PetalWidthCm vs Species")
    fig, ax = plt.subplots()
    sns.pointplot(x='Species', y='PetalWidthCm', data=data, ax=ax)
    ax.set_title('PetalWidthCm vs Species')
    ax.set_xlabel('Species')
    ax.set_ylabel('PetalWidthCm')
    st.pyplot(fig)

    # Scatter Plot
    st.write("### SepalLengthCm vs SepalWidthCm")
    fig, ax = plt.subplots()
    sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=data, ax=ax)
    ax.set_title('SepalLengthCm vs SepalWidthCm')
    ax.set_xlabel('SepalLengthCm (cm)')
    ax.set_ylabel('SepalWidthCm (cm)')
    st.pyplot(fig)

else:
    st.write("Failed to fetch data from the database.")
