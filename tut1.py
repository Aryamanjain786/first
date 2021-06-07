from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route("/aman")
def harry():
    return render_template('chat.html')

@app.route("/jain")
def aman():
    return "aman jia"
app.run(debug=True)