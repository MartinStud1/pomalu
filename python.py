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
        heslo = request.form.get("heslo")

        pole = [jmeno, prijmeni, email, telefon, heslo]
        uzivatele.append(pole)
    return render_template("stranka.html", jmeno=uzivatele)



@app.route("/uzivatele", methods = ["POST"])
def funkce():
    return render_template("uzivatele.html", uzivatele=uzivatele)

if __name__ == "__main__":
    app.run(debug=True)
