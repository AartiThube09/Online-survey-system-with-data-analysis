from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Set matplotlib to non-interactive backend
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# Connect to the MySQL database and fetch data
def fetch_data():
    try:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(
            user='root',
            password='PRITI@2205thube',
            host='localhost',
            database='data_db'
        )
        cursor = cnx.cursor()
        
        # Execute the query
        query = "SELECT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species FROM irisi"
        cursor.execute(query)
        
        # Fetch all rows and create DataFrame
        rows = cursor.fetchall()
        data = pd.DataFrame(rows, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
        
        # Close cursor and connection
        cursor.close()
        cnx.close()
        
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

# Fetch data at the start of the app
data = fetch_data()

@app.route('/')
def index():
    return render_template('dashboard.html')

# Bar Graph
@app.route('/bar_graph')
def bar_graph():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Species', data=data)
    plt.title('Species Distribution')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.savefig('static/bar_graph.png')
    plt.close()
    return render_template('bar_graph.html')

# Histogram
@app.route('/histogram')
def histogram():
    plt.figure(figsize=(8, 6))
    sns.histplot(data['PetalLengthCm'], bins=5, kde=True)
    plt.title('PetalLengthCm Histogram')
    plt.xlabel('PetalLengthCm (cm)')
    plt.ylabel('Frequency')
    plt.savefig('static/histogram.png')
    plt.close()
    return render_template('histogram.html')

# Point Graph
@app.route('/point_graph')
def point_graph():
    plt.figure(figsize=(8, 6))
    sns.pointplot(x='Species', y='PetalWidthCm', data=data)
    plt.title('PetalWidthCm vs Species')
    plt.xlabel('Species')
    plt.ylabel('PetalWidthCm')
    plt.savefig('static/point_graph.png')
    plt.close()
    return render_template('point_graph.html')

# Line Graph
@app.route('/line_graph')
def line_graph():
    plt.figure(figsize=(8, 6))
    sns.lineplot(x=data.index, y='PetalWidthCm', data=data)
    plt.title('PetalWidthCm vs Index')
    plt.xlabel('Index')
    plt.ylabel('PetalWidthCm')
    plt.savefig('static/line_graph.png')
    plt.close()
    return render_template('line_graph.html')

# Scatter Plot
@app.route('/scatter_plot')
def scatter_plot():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=data)
    plt.title('SepalLengthCm vs SepalWidthCm')
    plt.xlabel('SepalLengthCm (cm)')
    plt.ylabel('SepalWidthCm (cm)')
    plt.savefig('static/scatter_plot.png')
    plt.close()
    return render_template('scatter_plot.html')

if __name__ == '__main__':
    app.run(debug=True)
