from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def load_categories():
    #return 'Hello, World!'
    #categories = db.execute("SELECT * FROM categories")
    return render_template("index.html")#, category=categories)
