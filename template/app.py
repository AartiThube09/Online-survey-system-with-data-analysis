from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('dashboard1.html')  # Render the template "index.html" from the templates folder

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
