# $pip install Flask
from flask import Flask, jsonify, request
import pandas as pd 
import csv

#print(df)

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World!</p>"

@app.route("/sum", methods=["GET"])
def sum():
    """Return the sum of two numbers."""

    a = request.args.get("a")
    b = request.args.get("b")

    return jsonify({"sum": int(a) + int(b)})

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
@app.route("/factorial", methods=["GET"])
def factorial_route():
    """Return the factorial of a number."""

    n = request.args.get("n",10)
    r = factorial(int(n))
    response = f'{n}! equals {r}'
    return response

@app.route("/whole_data", methods=["GET"])
def whole_data():
    """Return the whole dataset."""
    df = pd.read_csv('NYPD_Hate_Crimes_20250131.csv')
    df1 = df.to_csv()
    return df1

@app.route("/filtered_data", methods=["GET"])
def filtered_data():
    df = pd.read_csv('NYPD_Hate_Crimes_20250131.csv')
    return jsonify(df["Complaint Year Number"].tolist())

if __name__ == "__main__":
    app.run(debug=True)
