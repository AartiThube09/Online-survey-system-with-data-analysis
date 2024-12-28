import mysql.connector
import pandas as pd

# Connect to the MySQL database
cnx = mysql.connector.connect(
    user='root',
    password='PRITI@2205thube',
    host='localhost',
    database='data_db'
)

# Create a cursor object
cursor = cnx.cursor()
                         
# Execute the query to select all records from the 'irisi' table
query = "SELECT * FROM irisi"
cursor.execute(query)

# Fetch all results from the query
records = cursor.fetchall()

# Display the first 150 records on the console
print("All the records from the 'irisi' table:")
for record in records[:150]:    
    print(record)

# Close the cursor and connection 
cursor.close()
cnx.close()
