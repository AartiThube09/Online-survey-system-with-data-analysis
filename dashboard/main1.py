from flask import Flask, render_template, jsonify
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

app = Flask(__name__)

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
        query = "SELECT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species FROM irisi"
        cursor.execute(query)
        print("Success")
        rows = cursor.fetchall()
        data = pd.DataFrame(rows, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

# Function to save and return paths of the visualizations
def save_visualizations(data):
    image_paths = {}

    try:
        # Bar Graph
        plt.figure(figsize=(8, 6))
        sns.countplot(x='Species', data=data)
        plt.title('Species Distribution')
        plt.xlabel('Species')
        plt.ylabel('Count')
        bar_graph_path = 'static/bar_graph.png'
        plt.savefig(bar_graph_path)
        plt.close()
        image_paths['bar_graph'] = bar_graph_path

        # Histogram
        plt.figure(figsize=(8, 6))
        sns.histplot(data['PetalLengthCm'], bins=5, kde=True)
        plt.title('PetalLengthCm Histogram')
        plt.xlabel('PetalLengthCm (cm)')
        plt.ylabel('Frequency')
        histogram_path = 'static/histogram.png'
        plt.savefig(histogram_path)
        plt.close()
        image_paths['histogram'] = histogram_path

        # Line Graph
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=data.index, y='PetalWidthCm', data=data)
        plt.title('PetalWidthCm vs Index')
        plt.xlabel('Index')
        plt.ylabel('PetalWidthCm')
        line_graph_path = 'static/line_graph.png'
        plt.savefig(line_graph_path)
        plt.close()
        image_paths['line_graph'] = line_graph_path

        # Point Graph
        plt.figure(figsize=(8, 6))
        sns.pointplot(x='Species', y='PetalWidthCm', data=data)
        plt.title('PetalWidthCm vs Species')
        plt.xlabel('Species')
        plt.ylabel('PetalWidthCm')
        point_graph_path = 'static/point_graph.png'
        plt.savefig(point_graph_path)
        plt.close()
        image_paths['point_graph'] = point_graph_path

        # Scatter Plot
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=data)
        plt.title('SepalLengthCm vs SepalWidthCm')
        plt.xlabel('SepalLengthCm (cm)')
        plt.ylabel('SepalWidthCm (cm)')
        scatter_plot_path = 'static/scatter_plot.png'
        plt.savefig(scatter_plot_path)
        plt.close()
        image_paths['scatter_plot'] = scatter_plot_path

        return image_paths
    except Exception as e:
        print("Error saving visualizations:", e)
        return None

# Route to serve real-time visualizations via AJAX
@app.route('/get_visualization_data')
def get_visualization_data():
    data = fetch_data()
    if data is not None:
        images = save_visualizations(data)
        return jsonify(images)
    else:
        return jsonify({"error": "Failed to fetch data from the database"}), 500

# Main route to display the dashboard
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
