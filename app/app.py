import os
from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
app = Flask(__name__,)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def show_data():

    df = pd.read_csv(fr'{os.getcwd()}\app\fake_data.csv')
    return render_template("datatables/datatable.html", rows=df.values.tolist(), titles=df.columns.values)
