from flask import *
import sqlite3

sqlite_file = 'bazaStupar.sqlite'
app = Flask(__name__)
app.secret_key = "DOSADA"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stanje")
def stanje():
    conn = sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("select artikli.naziv, artikli.tip, stanje.kolicina, police.broj_police, police.tip, fridge.lokacija from artikli, stanje, police, fridge where artikli.id=stanje.id_artikla and stanje.id_police=police.id and police.id_frizidera=fridge.id order by fridge.lokacija desc")
    data = c.fetchall()
    conn.close()
    return render_template('stanje.html', data=data)

@app.route("/stavi", methods=["GET","POST"])
def stavi():
    if request.method == "POST":
        conn = sqlite3.connect(sqlite_file)
        frid=request.form.get("bb")
        naziv=request.form.get("naziv")
        tip=request.form.get("tip")
        kolk=request.form.get("koliko")
        di=request.form.get("aa")
        c3=conn.cursor()
        provjera=c3.execute("select * from artikli where naziv=?", (naziv,)).fetchone()
        if provjera==None:
            if tip=="1":
                c1=conn.cursor()
                tip='Hrana'
                c1.execute("insert into artikli(naziv, tip) values(:naziv,:tip)",{"naziv":naziv,"tip":tip})
                conn.commit()
            if tip=="2":
                c1=conn.cursor()
                tip='Piće'
                c1.execute("insert into artikli(naziv, tip) values(:naziv,:tip)",{"naziv":naziv,"tip":tip})
                conn.commit()
        if frid=="1":
            frid=1212
            if di=="1":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=1 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
            if di=="2":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=2 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
        if frid=="2":
            frid=322
            if di=="1":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=1 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
            if di=="2":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=2 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
        if frid=="3":
            frid=11
            if di=="1":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=1 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
            if di=="2":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=2 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
        if frid=="4":
            frid=12
            if di=="1":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=1 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
            if di=="2":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=2 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
        if frid=="5":
            frid=344
            if di=="1":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=1 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
            if di=="2":
                c2=conn.cursor()
                priv=c2.execute("select artikli.id from artikli where naziv=?", (naziv,)).fetchone()
                ime=priv[0]
                priv=c2.execute("select police.id from police where broj_police=2 and id_frizidera=?", (frid,)).fetchone()
                poli=priv[0]
                c2.execute("insert into stanje(kolicina, id_police, id_artikla) values(:kol,:pol,:art)",{"kol":kolk,"pol":poli,"art":ime})
                conn.commit()
        flash ('Uspješno ste unijeli artikal u frižider!')
    return render_template('stavi.html')

@app.route("/izvadi", methods=["GET","POST"])
def vani():
    if request.method == "POST":
        conn = sqlite3.connect(sqlite_file)
        c4=conn.cursor()
        frid1=request.form.get("cc")
        naziv1=request.form.get("naziv")
        kolk1=request.form.get("koliko")
        di1=request.form.get("hh")
        priv=c4.execute("select fridge.id from fridge where redni_broj=?", (frid1,)).fetchone()
        frid1=priv[0]
        priv=c4.execute("select police.id from police where broj_police=? and id_frizidera=?", (di1, frid1)).fetchone()
        polica=priv[0]
        priv=c4.execute("select artikli.id from artikli where naziv=?", (naziv1,)).fetchone()
        artikl=priv[0]
        priv=c4.execute("select stanje.kolicina from stanje where id_police=? and id_artikla=?", (polica, artikl)).fetchone()
        kolicina=priv[0]
        if int(kolk1)>kolicina:
            flash ('Ne možeš uzeti količinu veću od one koja je u frižideru na stanju!')
        if int(kolk1)==kolicina:
            c4.execute("delete from stanje where id_police=? and id_artikla=?", (polica, artikl))
            conn.commit()
            flash ('Artikal izvađen i nema ga više u tom frižideru!')
        if int(kolk1)<kolicina:
            rez=kolicina-int(kolk1)
            c4.execute("update stanje set kolicina=? where id_police=? and id_artikla=?", (rez, polica, artikl))
            conn.commit()
            flash ('Artikal je izvađen i ali ga ima još u tom frižideru!')
    return render_template('izvadi.html')

if __name__ == "__main__":
    app.run()
