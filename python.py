from flask import Flask, render_template, request,session

app = Flask(__name__)
uzivatele = []
#p_x = přihlašovací ...
app.secret_key = "nikdonicnetusit"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        jmeno = request.form.get("jmeno")
        prijmeni = request.form.get("prijmeni")
        email = request.form.get("email")
        telefon = request.form.get("telefon")

        pole = [jmeno, prijmeni, email, telefon]
        uzivatele.append(pole)#pole jde do uživatelů - append. = do tohohle přidej tamto

        session ["uzivatele"] = uzivatele

        session['jmeno'] = jmeno
        session['prijmeni'] = prijmeni
        session['email'] = email
        session['telefon'] = telefon
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

hlavni_jmeno = None
hlavni_prijmeni = None
@app.route("/prihlas_se", methods=["GET","POST"])
def prihlas_se():
    jmeno = session.get("jmeno")
    prijmeni = session.get("prijmeni")
    email = session.get("email")
    telefon = session.get("telefon")
#pole všech uživatelů :
    uzivatele = session.get("uzivatele")#převedu si celé pole. Tak... mám tady pole. Vyzkouším porovnat pole s polem, co vytvoří uživatel v přihlášení
#--------------


    p_jmeno = request.form.get("p_jmeno")
    p_prijmeni = request.form.get("p_prijmeni")
    p_email = request.form.get("p_email")
    p_telefon = request.form.get("p_telefon")


    p_pole = [p_jmeno, p_prijmeni, p_email, p_telefon] #poznámka - není třeba dělat pole v poli u přihlašování, protože tam nebude více než jedno zadané tím člověkem... stačí jedno pole

    #if request.method == "POST":
     #   if jmeno == p_jmeno and prijmeni == p_prijmeni and email == p_email and telefon == p_telefon:
      #      porovnani = "Výborně! Jsi přihlášen/a!"
        
       # else:
        #    porovnani = "Špatné přihlášení..."
    #return render_template("prihlas_se.html",spravne=porovnani)
    spravne = 0
    mam_te = 0
    if request.method == "POST":
        for i in range(len(uzivatele)):
            
            for n in range(len(p_pole)):
                 
                                                                    
                if uzivatele[i][n] == p_pole[n]:
                    spravne += 1
                       
            if spravne == 4:
                mam_te = 1
                
                break
            else:
                spravne = 0  
                mam_te = 0
                
        if mam_te == 1:
            porovnani = "Jsi přihlášen."
            hlavni_jmeno = p_pole[0]
            hlavni_prijmeni = p_pole[1]
        if mam_te != 1:
            porovnani = "něco nám nesedí" 
            hlavni_jmeno = None
            hlavni_prijmeni = None
    print(hlavni_jmeno)
    print(hlavni_prijmeni)
    return render_template("prihlas_se.html",spravne=porovnani)   

               
        



if __name__ == "__main__":
    app.run(debug=True)
#hlavně nezapomeň přidat heslo vole..