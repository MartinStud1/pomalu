from flask import Flask, render_template, request,session

app = Flask(__name__)
uzivatele = []
statistika = {    #list pro statistiku
    "senior_s" : 0, "vydej_s" : 0, "beskydy_s" : 0, "komunitzah_s" : 0, "promale_s" : 0
}
uzivatele1 = []
uzivatele2 = []
uzivatele3 = []
uzivatele4 = []
uzivatele5 = []

#p_x = přihlašovací ...
app.secret_key = "nikdonicnetusit"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        jmeno = request.form.get("jmeno")
        prijmeni = request.form.get("prijmeni")
        email = request.form.get("email")
        telefon = request.form.get("telefon")
        heslo = request.form.get("heslo")

        pole = [jmeno, prijmeni, email, telefon, heslo]
        uzivatele.append(pole)#pole jde do uživatelů - append. = do tohohle přidej tamto

        session ["uzivatele"] = uzivatele

        session['jmeno'] = jmeno
        session['prijmeni'] = prijmeni
        session['email'] = email
        session['telefon'] = telefon
        session['heslo'] = heslo
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




@app.route("/prihlas_se", methods=["GET","POST"])
def prihlas_se():
    jmeno = session.get("jmeno")
    prijmeni = session.get("prijmeni")
    email = session.get("email")
    telefon = session.get("telefon")
    heslo = session.get("heslo")
#pole všech uživatelů :
    uzivatele = session.get("uzivatele")#převedu si celé pole. Tak... mám tady pole. Vyzkouším porovnat pole s polem, co vytvoří uživatel v přihlášení
#--------------


    p_jmeno = request.form.get("p_jmeno")
    p_prijmeni = request.form.get("p_prijmeni")
    p_email = request.form.get("p_email")
    p_telefon = request.form.get("p_telefon")
    p_heslo = request.form.get("p_heslo")
    p_pole = [p_jmeno, p_prijmeni, p_email, p_telefon, p_heslo] #poznámka - není třeba dělat pole v poli u přihlašování, protože tam nebude více než jedno zadané tím člověkem... stačí jedno pole

    spravne = 0
    mam_te = 0
    if request.method == "POST":
        for i in range(len(uzivatele)):  
            for n in range(len(p_pole)):
                                                                      
                if uzivatele[i][n] == p_pole[n]:
                    spravne += 1          
            if spravne == len(p_pole):
                mam_te = 1
                
                break
            else:
                spravne = 0  
                mam_te = 0
                
        if mam_te == 1:
            porovnani = "Jsi přihlášen/a. Výborně!"
            hl_jmeno = request.form.get("p_jmeno")
            hl_prijmeni = request.form.get("p_prijmeni")
            session['hl_jmeno'] = hl_jmeno #uložím do relace
            session['hl_prijmeni'] = hl_prijmeni #uložím do relace
            
        if mam_te != 1:
            porovnani = "Něco nám nesedí..vyplň formulář." 
            
    
    return render_template("prihlas_se.html",spravne=porovnani) 
 


@app.route("/senior_s", methods=["GET", "POST"])
def senior_s():
    if request.method == "POST":
        statistika["senior_s"] += 1
        hl_jmeno = session.get("hl_jmeno")
        hl_prijmeni = session.get("hl_prijmeni")
        uzivatele1.append(hl_jmeno)
        uzivatele1.append(hl_prijmeni)
    return render_template("senior.html")

@app.route("/beskydy_s", methods=["GET", "POST"])
def beskydy_s():
    if request.method == "POST":
        statistika["beskydy_s"] += 1
        hl_jmeno = session.get("hl_jmeno")
        hl_prijmeni = session.get("hl_prijmeni")
        uzivatele2.append(hl_jmeno)
        uzivatele2.append(hl_prijmeni)
        
    return render_template("beskydy.html")

@app.route("/promale_s", methods=["GET", "POST"])
def promale_s():
    if request.method == "POST":
        statistika["promale_s"] += 1
        hl_jmeno = session.get("hl_jmeno")
        hl_prijmeni = session.get("hl_prijmeni")
        uzivatele3.append(hl_jmeno)
        uzivatele3.append(hl_prijmeni)
    return render_template("promale.html")

@app.route("/komunitzah_s", methods=["GET", "POST"])
def komunitzah_s():
    if request.method == "POST":
        statistika["komunitzah_s"] += 1
        hl_jmeno = session.get("hl_jmeno")
        hl_prijmeni = session.get("hl_prijmeni")
        uzivatele4.append(hl_jmeno)
        uzivatele4.append(hl_prijmeni)
    return render_template("komunitzah.html")

@app.route("/vydej_s", methods=["GET", "POST"])
def vydej_s():
    if request.method == "POST":
        statistika["vydej_s"] += 1
        hl_jmeno = session.get("hl_jmeno")
        hl_prijmeni = session.get("hl_prijmeni")
        uzivatele5.append(hl_jmeno)
        uzivatele5.append(hl_prijmeni)
    return render_template("vydej.html")

@app.route("/statistika", methods = ["GET", "POST"])
def statistikafunkce():
    
    return render_template("statistika.html", statistika=statistika,jmeno1 = uzivatele1, jmeno2 = uzivatele2, jmeno3 = uzivatele3, jmeno4 = uzivatele4, jmeno5 = uzivatele5)
    
if __name__ == "__main__":
    app.run(debug=True)




