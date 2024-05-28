from flask import Flask, render_template, request

app = Flask(__name__)
uzivatele = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        jmeno = request.form.get("jmeno")
        prijmeni = request.form.get("prijmeni")
        email = request.form.get("email")
        telefon = request.form.get("telefon")

        pole = [jmeno, prijmeni, email, telefon]
        uzivatele.append(pole)
    return render_template("stranka.html")



@app.route("/uzivatele", methods = ["POST"])
def f_uzivatele():
    return render_template("uzivatele.html", uzivatele=uzivatele)

@app.route("/tvurce",methods = ["POST"])
def tvurce():
    return render_template("tvurce.html")

@app.route("/aktualniprojekty",methods = ["POST"])
def aktualniprojekty():
    return render_template("aktualniprojekty.html")

@app.route("/beskydy",methods = ["POST"])
def beskydy():
    return render_template("beskydy.html")

@app.route("/promale",methods = ["POST"])
def promale():
    return render_template("promale.html")

@app.route("/senior",methods = ["POST"])
def senior():
    return render_template("senior.html")

@app.route("/vydej",methods = ["POST"])
def vydej():
    return render_template("vydej.html")

@app.route("/komunitzah",methods = ["POST"])
def komunitzah():
    return render_template("komunitzah.html")

if __name__ == "__main__":
    app.run(debug=True)
