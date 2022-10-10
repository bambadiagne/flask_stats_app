import os
from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
app = Flask(__name__,)
app.secret_key = os.getenv("SECRET_KEY")


def open_csv():
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    df = pd.read_csv(fr'{path}\fake_data.csv')
    return df


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def show_data():
    """
      Affiche des données du csv
    """
    df = open_csv()
    return render_template("datatables/datatable.html", rows=df.values.tolist(), titles=df.columns.values)


@app.route("/charts")
def show_chart():
    """
      Affiche des graphiques sur le genre ,et les salaires de personnes
    """
    df = open_csv()
    # Logique du filtrage des genres
    gender_list = df['gender'].to_list()
    TYPE_GENDER = list(set(gender_list))
    TYPE_GENDER.sort()
    gender_list = [gender_list.count(gender) for gender in TYPE_GENDER]
    # Logique du filtrage des salaires
    #wages_list=[list(filter(lambda row:row[-2]==gender,df.values.tolist()))  for gender in ['Female','Male'] ]
    female_wages = sorted(df[df["gender"] == "Female"]["wage"].to_list())
    male_wages = sorted(df[df["gender"] == "Male"]["wage"].to_list())
    wages_list = [female_wages, male_wages]
    print("sd", wages_list)
    return render_template("chart/chart.html", wages_list=wages_list, gender_list=gender_list)
