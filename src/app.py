from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/random_forest_regressor_default_42.sav", "rb"))

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        val1  = float(request.form["CRIM"])
        val2  = float(request.form["ZN"])
        val3  = float(request.form["INDUS"])
        val4  = float(request.form["CHAS"])
        val5  = float(request.form["NOX"])
        val6  = float(request.form["RM"])
        val7  = float(request.form["AGE"])
        val8  = float(request.form["DIS"])
        val9  = float(request.form["RAD"])
        val10 = float(request.form["TAX"])
        val11 = float(request.form["PTRATIO"])
        val12 = float(request.form["B"])
        val13 = float(request.form["LSTAT"])

        data = [[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13 ]]
        prediction = float(model.predict(data)[0])

    else:
        prediction = 0
    return render_template("index.html", prediction = prediction) 

 