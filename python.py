from flask import Flask, render_template, request,session#z flasku importujeme potřebné záležitosti

app = Flask(__name__)


statistika = {    #list pro statistiku
    "senior_s" : 0, "vydej_s" : 0, "beskydy_s" : 0, "komunitzah_s" : 0, "promale_s" : 0
}
uzivatele = []#definování prázdných polí
uzivatele1 = []
uzivatele2 = []
uzivatele3 = []
uzivatele4 = []
uzivatele5 = []

#p_x = přihlašovací ...
app.secret_key = "nikdonicnetusit"#zabezbečení aplikace
@app.route("/", methods=["GET", "POST"])#routa pro základní stránku
def home():
    if request.method == "POST":#díky tomu if request.... - až uživatel zmáčkne tlačítko - což je POST, tak teprve pak proměnné načtou zadané hodnoty
        jmeno = request.form.get("jmeno")#načítám si hodnoty do proměnných, co zadal uživatel jako vytvoření účtu
        prijmeni = request.form.get("prijmeni")
        email = request.form.get("email")
        telefon = request.form.get("telefon")
        heslo = request.form.get("heslo")

        pole = [jmeno, prijmeni, email, telefon, heslo] #definuji si pole a do něj vložím proměnné, s hodnotami uživatele - tento krok slouží k - pole se stává "jedním" uživatelem
        uzivatele.append(pole)#pole jde do uživatelů - append. = do tohohle přidej tamto - do uživatelů přidej pole
        #tím, že jsem si na začátku stránky nadefinoval prázdné pole uzivatele = [] - teď si do celého jednoho pole uzivatele - slouží jako pytlíček pro uživatele. - budu do něj vkládat "pole" - a budu mít jednotný celek, kde budou všichni uživatelé. Díky indexům si z nich pak mohu vybírat jakého chci atd..
        session ["uzivatele"] = uzivatele #session ... session je relace - hodnota se v podstatě "uloží" na server a ten si ji zapamatuje - vhodné pro přihlášení. Taky je to dobré v tom, že si díky tomuto uložení do "třetího prostoru" mohu jednoduše hodnoty předávat mezi funkcemi v pythonu - velká výhoda

        session['jmeno'] = jmeno
        session['prijmeni'] = prijmeni
        session['email'] = email
        session['telefon'] = telefon
        session['heslo'] = heslo
    return render_template("stranka.html")#vracím stranka.html (hlavní stránka)


#zde mám dlouhý list deklarování všech tlačítek a odkazů na další stránky. Vždy jen vrátím stránku, kde chci, ať se objeví uživatel - jde mi jen o přesměrování.
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

    uzivatele = session.get("uzivatele")#převedu si celé pole uživatelů. / session.get(*jakou uloženou hodnotu chci vzít) - získám si do proměnné uzivatele uloženou hodnotu, kterou jsem ukládal pomocí session["x"] = y

    p_jmeno = request.form.get("p_jmeno")#získám hodnoty přihlášení od uživatele
    p_prijmeni = request.form.get("p_prijmeni")
    p_email = request.form.get("p_email")
    p_telefon = request.form.get("p_telefon")
    p_heslo = request.form.get("p_heslo")
    p_pole = [p_jmeno, p_prijmeni, p_email, p_telefon, p_heslo] #uložím si hodnoty přihlášení od uživatele do pole p_pole
    #poznámka - není třeba dělat pole v poli u přihlašování, protože tam nebude více než jedno zadané tím člověkem... stačí jedno pole

    spravne = 0 #definuji si proměnnou, díky které budu vyhodnocovat jestli uživatel zadal všechny přihlašovací údaje správně
    mam_te = 0 #definuji si proměnnou, která mi bude sloužit jako vyhodnocení pro uživatele, díky ní se později v kódu uloží aktuální uživatel
    if request.method == "POST":#jakmile uživatel odešle ...
        for i in range(len(uzivatele)):  #cyklus s počtem opakování podle toho, kolik je celkem v pytlíčku uživatelů uživatelů - procházíme a budeme kontrolovat postupně každého uživatele, než najdeme shodu. Pokud shodu nenajdeme, vypíše se - něco nám nesedí.
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
            session['hl_jmeno'] = hl_jmeno #uložím do relace jméno přihlášeného uživatele - budu používat pro statistiku
            session['hl_prijmeni'] = hl_prijmeni #uložím do relace příjmení přihlášeného uživatele - budu používat pro statistiku
            
        if mam_te != 1:
            porovnani = "Něco nám nesedí..vyplň formulář." 
            
    
    return render_template("prihlas_se.html",spravne=porovnani) #vracíme stránku prihlas_se a porovnání jestli je uživatel přihlášen, či něco není dobře
 

#seznam rout, který slouží - jakmile se uživatel zapojí do nějakého projektu
@app.route("/senior_s", methods=["GET", "POST"])
def senior_s():
    if request.method == "POST":
        statistika["senior_s"] += 1 #náš list statistika - vybere se prvek senior_s a přidá se mu +1 (v základě nastavený na nulu) pokaždé, co se zmáčkne tlačítko pro zapojení do tohoto projektu
        hl_jmeno = session.get("hl_jmeno")#získám hodnotu z uložené relace - jméno uživatele, co se zapojuje do projektu
        hl_prijmeni = session.get("hl_prijmeni")#získám hodnotu z uložené relace - příjmení uživatele, co se zapojuje do projektu
        uzivatele1.append(hl_jmeno) # do pole uzivatelex si uložím jméno uživatele- v každé routě je x jiné, abych rozlišil na konci jednotlivé zapojení do jednotlivých projektů 
        uzivatele1.append(hl_prijmeni)# do pole uzivatelex si uložím příjmení uživatele
        #neboli v poli uzivatelex budu mít jak jméno, tak příjmení uživatele
    return render_template("senior.html")#vracím stránku s projektem

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

@app.route("/statistika", methods = ["GET", "POST"])#routa pro načtení stránky statistika
def statistikafunkce():
    
    return render_template("statistika.html", statistika=statistika,jmeno1 = uzivatele1, jmeno2 = uzivatele2, jmeno3 = uzivatele3, jmeno4 = uzivatele4, jmeno5 = uzivatele5)#vracím statistiku, získaná jednotlivé data pro jednotlivý projekt
    
if __name__ == "__main__":
    app.run()




