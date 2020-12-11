from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

#Help with Importing SQL and working with it: https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

rows = ['Asset Class', 'Portfolio Monitoring', 'Trade Simulation', 'Core Capabilities', 'OMS Connectivity']

@app.route("/")
def load_categories():
    #connection = sqlite3.connect("categories.db")
    #db = connection.cursor()
    #rows = db.execute("SELECT * FROM categories")
    return render_template("index.html", rows=rows)

@app.route("/about")
def load_about():
    return render_template("about.html")

#@aprows
