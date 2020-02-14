# Asennusohje

## Sovelluksen asentaminen omalle koneelle

Mene komentorivillä hakemistoon, johon haluat ladata lähdekoodin.

Suorita seuraava komento kloonataksesi repositorion

```
$ git clone git@github.com:noorary/kadunkulkija.git
``` 
Nyt lähdekoodi löytyy hakemistosta `kadunkulkija`.

## Sovelluksen suorittaminen paikallisesti

### 1. Vaatimukset

* python3
* sqlite3

`DATABASE_URL`-ympäristömuuttuja tulee olla määritelty, jotta sovelluksen voi käynnistää.

### 2. Python virtuaaliympäristön käyttöönotto

Suorita komento

```
$ python3 -m venv venv
```
Komento luo python-virtuaaliympäristön, johon projektin riippuvuudet asennetaan. Virtuaaliympäristö otetaan käyttöön komennolla

```
$ source venv/bin/activate
```

### 3. Flask - kirjaston käyttöönotto

Päivitä pip uusimpaan versioon komennolla
```
$ pip install --upgrade pip
```
Tämän jälkeen suorita komento 
```
$ pip install Flask
```
ottaaksesi käyttöön Flask-kirjaston.

### 4. Riippuvuuksien asentaminen

Projektin riippuvuudet saa asennettua kloonatun projektin mukana tulleesta tiedostosta `requirements.txt`
Suorita komento
```
$ pip install -r requirements.txt
```
### 5. Sovelluksen käynnistäminen 

Suorita projektin juuressa komento
```
$ python3 run.py
```
Sovellus käynnistyy oletusarvoisesti osoitteessa [http://localhost:5000](http://localhost:5000)

Avaa osoite selaimella ja voit käyttää sovellusta paikallisessa verkkoympäristössä.

## Sovelluksen suorittaminen Herokussa

Projektin suorittaminen Herokussa vaatii, että sovelluksen lähdekoodi on asennettu paikalliselle koneelle ylläolevan ohjeen mukaisesti. Lisäksi tulee olla käytössä Heroku-tunnus ja Heroku CLI. 
Heroku CLI saa asennettua Linuxissa komennolla
```
$ sudo snap install --classic heroku
```

### 1. Kirjaudu Herokuun ja luo projekti

```
$ heroku login
```

Mene komentorivillä paikallisen projektin juureen ja suorita komento
```
$ heroku create <projektin nimi>
```

### 2. Määrittele paikallisesta projektista Heroku-projekti
```
$ git remote add heroku
$ git add .
$ git commit -m "Inital heroku-commit"
$ git push heroku master
```

### 3. Määritä projektille PostreSQL tietokanta Herokuun

```
$ heroku config:set HEROKU=1
$ heroku addons:add heroku-postgresql:hobby-dev
```
Sovelluksen pitäisi nyt pyöriä Herokussa.





