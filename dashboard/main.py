from datetime import date
from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

# Bar Graph
@app.route('/bar_graph')
def bar_graph():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Species', data=date)
    plt.title('Species Distribution')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.savefig('static/bar_graph.png')
    plt.close()  # Close the plot to free up memory
    return render_template('./bar_graph.html')

#Histogram
@app.route('/histogram')
def histogram():
    plt.figure(figsize=(8, 6))
    sns.histplot(data['PetalLengthCm'], bins=5, kde=True)
    plt.title('PetalLengthCm Histogram')
    plt.xlabel('PetalLengthCm (cm)')
    plt.ylabel('Frequency')
    plt.savefig('static/histogram.png')
    plt.close()  # Close the plot to free up memory
    return render_template('histogram.html')

#Point graph
@app.route('/point_graph')
def point_graph():
    plt.figure(figsize=(8, 6))
    sns.pointplot(x='Species', y='PetalWidthCm', data=date)
    plt.title('PetalWidthCm vs Species')
    plt.xlabel('Species')
    plt.ylabel('PetalWidthCm')
    plt.savefig('static/point_graph.png')
    plt.close()  # Close the plot to free up memory
    return render_template('point_graph.html')

#Line graph
@app.route('/line_graph')
def line_graph():
    plt.figure(figsize=(8, 6))
    sns.lineplot(x=date.index, y='PetalWidthCm', data=date)
    plt.title('PetalWidthCm vs Index')
    plt.xlabel('Index')
    plt.ylabel('PetalWidthCm')
    plt.savefig('static/line_graph.png')
    plt.close()  # Close the plot to free up memory
    return render_template('line_graph.html')

#Scatter Plot
@app.route('/scatter_plot')
def scatter_plot():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=date)
    plt.title('SepalLengthCm vs SepalWidthCm')
    plt.xlabel('SepalLengthCm (cm)')
    plt.ylabel('SepalWidthCm (cm)')
    plt.savefig('static/scatter_plot.png')
    plt.close()  # Close the plot to free up memory
    return render_template('scatter_plot.html')

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)