# Kadunkulkija

## Aineopintojen harjoitustyö: tietokantasovellus, kevät 2020

Tämä sovellus on toteutettu keväällä 2020 Helsingin yliopiston
tietojenkäsittelytieteen kandiohjelman kurssilla Aineopintojen harjoitustyö:
tietokantasovellus.

### Heroku

Sovellus löytyy Herokusta osoitteesta https://kadunkulkija.herokuapp.com/

### Testitunnukset

Sovellukseen voi kirjautua testitunnuksilla

Käyttäjätyyppi | käyttäjätunnus | salasana
-------------- | -------------- | --------
user           | test           | tester123

### Projektin kuvaus

Projektin aiheena on sovellus, jossa käyttäjä näkee listattuna Helsingin
kaupunginosat ja kadut. Käyttäjä voi luoda omia listoja esimerkiksi
suosikkikaduistaan ja pitää kirjaa missä kaikilla kaduilla on käynyt.

Käyttäjä voi luoda sovellukseen suunnitelman, johon lisätään päivämäärä ja katu, jossa on tarkoitus vierailla.
Vierailun jälkeen katu voidaan merkitä käydyksi. Käyttäjä voi luoda, tarkastella, muokata ja 
poistaa suunnitelmia. 

Käyttäjät voivat lisätä kaupunginosia ja katuja sovellukseen. Admin-käyttäjät voivat päivittää katujen ja kaupunginosien tietoja
sekä poistaa niitä.  


### Dokumentaatio

Tietokantakaavio

![Tietokantakaavio](https://raw.githubusercontent.com/noorarytila/kadunkulkija/master/dokumentaatio/kadunkulkija.png)

[Käyttötapaukset](https://github.com/noorarytila/kadunkulkija/blob/master/dokumentaatio/kayttotapaukset.md)


### TO DO - viikko 3

#### Kurssin vaatimukset

- [ ] lomakkeet validioivat syötetyn tiedon
- [x] WTForms käyttöön nimen muuttamiseen
- [x] sovelluksessa on mahdollisuus rekistöröitymiseen
- [x] sovelluksessa on mahdollisuus kirjautumiseen
- [x] README:stä löytyy testitunnuksen tiedot
- [x] sovelluksessa on ainakin 2 tietokantataulua
- [ ] ainakin yhteen tietokantataulun tietoihin liittyy täysi CRUD-toiminnallisuus
- [x] githubissa issuet päällä
- [x] Herokussa käytetään PostgreSQL-tietokannanhallintajärjestelmää
- [x] Viitteet taulujen välillä
- [ ] Linkki kaupunginosan lisäämiseen
- [ ] Roolitaulu pois ja käyttäjälle admin-boolean
    - [x] käyttäjä-taulu päivitetty
    - [ ] tietokantakaavio päivitetty

#### Muut

- [ ] kirjautuminen onnistui - ilmoitus
- [ ] kahta samaa käyttäjänimeä ei voi olla
- [ ] salasanat tallennetaan tietokantaan kryptattuna
- [x] kaupunginosa taulussa väh. yksi rivi täydellisenä
- [ ] muokkauksessa tieto lomakkeeseen valmiiksi
- [ ] pudotusvalikko toimintaan
- [ ] käyttäjä liittyy johonkin

## TO DO - viikko 4

- [x] sovelluksessa on ainakin 3 tietokantataulua joista jokainen on käytössä
- [ ] sovelluksessa on ainakin yksi monimutkaisempi yhteenvetokysely jonka tulokset näytetään käyttäjälle
- [ ] boostrap tms käytössä ulkoasun tyylittelyyn
- [ ] toiminnallisuus on täydentynyt

## TO DO - viikko 5

- [ ] autorisointi
- [ ] käytettävyyden viilausta
- [ ] toiminnallisuus on täydentynyt
- [ ] asennusohje
- [ ] käyttöohje

## TO DO - viikko 6

- [ ] toiminnallisuus on täydentynyt
- [ ] ulkoasu, käytettävyys ja toiminnallisuus
- [ ] dokumentaation päivittäminen ja lisääminen
- [ ] koodikatselmointi

## TO DO - viimeinen viikko

- [ ] demo
- [ ] viimeiset viilaukset
- [ ] loppupalautus

### Jatkokehitysideoita
