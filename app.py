from flask import Flask, render_template

app = Flask(__name__)

# Render HTML template
@app.route("/")
def index():
    return render_template('index.html')