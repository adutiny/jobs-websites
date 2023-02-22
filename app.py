from flask import Flask,render_template

# create Flask application
#app = Flask(__name__)
app=Flask(__name__,template_folder='Templates')

@app.route("/")
def home_page():
    return render_template("home.html") 

@app.route("/Custom Solutions")
def custom_page():
    return render_template("custom.html") 

# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 


 
