from flask import Flask, render_template


# create Flask application
app = Flask(__name__)


# create route
@app.route("/")
def hello_world():
    return "Hello, World"

# run the application
if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)