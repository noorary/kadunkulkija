# Kadunkulkija

## Aineopintojen harjoitustyö: tietokantasovellus, kevät 2020

Tämä sovellus on toteutettu keväällä 2020 Helsingin yliopiston
tietojenkäsittelytieteen kandiohjelman kurssilla Aineopintojen harjoitustyö:
tietokantasovellus.

[Asennusohje](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/asennusohje.md)
[Käyttöohje](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kayttoohje.md)
[Tietokantakaavio](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kadunkulkija.png)
[Käyttötapaukset](https://github.com/noorarytila/kadunkulkija/blob/master/dokumentaatio/kayttotapaukset.md)

### Heroku

Sovellus löytyy Herokusta osoitteesta https://kadunkulkija.herokuapp.com/

### Testitunnukset

Sovellukseen voi kirjautua testitunnuksilla

Käyttäjätyyppi | käyttäjätunnus | salasana
-------------- | -------------- | --------
user           | test           | tester123
admin          | admin          | admin123

### Projektin kuvaus

Projektin aiheena on sovellus, jossa käyttäjä näkee listattuna Helsingin kadut.

Käyttäjä voi luoda sovellukseen suunnitelman, johon lisätään päivämäärä ja katu tai katuja, joissa on tarkoitus vierailla.
Vierailun jälkeen katu voidaan merkitä käydyksi. Käyttäjä voi luoda, tarkastella, muokata ja 
poistaa suunnitelmia. 

Käyttäjät voivat lisätä katuja sovellukseen. Admin-käyttäjät voivat päivittää katujen nimiä sekä poistaa katuja.  

### Dokumentaatio

Tietokantakaavio

![Tietokantakaavio](https://raw.githubusercontent.com/noorarytila/kadunkulkija/master/dokumentaatio/kadunkulkija.png)

#### Sovelluksen rajoitteet ja puuttuvat ominaisuudet

## TO DO - viikko 5

#### Kurssin vaatimukset

- [ ] autorisointi

#### Yleiset to-do

- [x] kirjautuneelle käyttäjälle linkki omiin suunnitelmiin
- [x] dropdown valikko navbariin
- [x] Katujen listaukseen näkyviin myös kaupungin osa
- [x] Kadun nimeä voi muokata suoraan listauksesta

- [ ] "stats" omalle sivulleen 
    - [ ] tulosten sivutus

- [ ] salasanat tallennetaan tietokantaan kryptattuna
- [ ] muokkauksessa tieto lomakkeeseen valmiiksi

- [ ] kirjautuminen onnistui - ilmoitus
- [ ] kahta samaa käyttäjänimeä ei voi olla
- [ ] käyttäjä voi muokata omia tietojaan
- [ ] tyylittele sivuja

## TO DO - viikko 6

- [ ] monesta moneen suhde
    - [ ] suunnitelmaan liittyy useampi katu
- [x] toiminnallisuus on täydentynyt
- [x] ulkoasu, käytettävyys ja toiminnallisuus
- [ ] dokumentaation päivittäminen ja lisääminen
    - [x] tietokantakaavion päivittäminen
    - [ ] käyttötapausten päivittäminen
    - [ ] muut dokumentaation osat, kts. kurssin arvoteluperusteet
- [ ] koodikatselmointi

## TO DO - viimeinen viikko

- [ ] demo
- [ ] viimeiset viilaukset
- [ ] loppupalautus

## TO DO - kurssin arvosteluperusteet & muut tärkeät


- [ ] dokumentaatio
    - [x] aiheen kuvaus
    - [ ] käyttöohje
    - [x] asennusohje
    - [ ] rajoitteet ja puuttuvat ominaisuudet
    - [ ] user storyt
        - [ ] listaus käyttäjäryhmistä ja käyttötapauksista
    - [ ] user storyjen SQL kyselyt
    - [ ] tietokantarakenteen kuvaus
        - [ ] taulujen normalisointi tarvittaessa / perustelu normalisoinnin puutteelle
        - [x] tietokantakaavio osa dokumentaatiota
        - [x] tietokantakaavio vastaa todellista tietokantaa
        - [ ] CREATE TABLE lauseet ja indeksien lisäykset

- [ ] tietokannan toteutus
    - [x] ei sql-injektiomahdollisuuksia
    - [x] isoissa listauksissa sivutus
    - [ ] käyttäjien syötteet validioidaan palvelimella
    - [ ] indeksien käyttö
    - [ ] SQL-virheiden käsittely
    - [x] tehokkaat kyselyt
    - [x] monimutkaisempia yhteenvetokyselyitä

- [ ] web-sovellus
    - [x] ei rikkinäisiä linkkejä
    - [x] lomakkeet toimivat järkevillä syötteillä
    - [ ] sovellus toimii myös ei järkevillä syötteillä (validiointi joko palvelimella tai selaimella)
        - [ ] rekistöröitymislomake
    - [x] tyyli on yhtenäinen ja käyttö tuntuu luontevalta
    - [ ] sivutus käytössä
        - [ ] edit street name
        - [ ] plans
    - [ ] siistit lomakkeet

- [ ] käytettävyys & saavutettavuus
    - [x] sivut ovat loogisesti rakennetut ja helposti löydettävissä
        - [x] etusivu sovelluksen juuressa
        - [x] järkevä yleisvalikko
    - [x] käyttäjän syötteet validioidaan
    - [ ] virhetilanteissa ymmärrettävät virheviestit
        - [ ] rekistöröitymislomake!
    - [ ] ACheckerin ilmoittamat ongelmat korjattu
    - [ ] sovellus on käytettävä myös isoilla tietomäärillä
        - [ ] tulosten sivutus
        - [ ] hakutoiminnallisuus
    - [x] sovellus on hyödyllinen (käyttötapaukset mahdolliset tehdä)
    - [ ] tehokkuus: toivotut asiat voidaan tehdä ilman turhia välivaiheita

- [ ] ylläpidettävyys
    - [x] konfiguraatiot kehitysympäristölle
    - [x] konfiguraatiot tuotantoympäristölle
    - [ ] sovellus ei sisällä tuotantoympäristön salasanoja tms
    - [x] koodin laatu ok
    - [x] sovellus pilkottu selkeisiin luokkiin
    - [ ] koodi on ymmärrettävää
        - [ ] tarpeelliset kohdat kommentoitu

- [ ] arvosana 5 minimivaatimukset
    - [x] vähintään 3 tietokantataulua (+ liitostaulut)
    - [x] käyttäjä liittyy muuhunkin kuin kirjautumiseen (suunnitelmat)
    - [ ] vähintään kahdesta tietokohtaasta täysi CRUD 
        - [x] suunnitelmat
        - [ ] joku muu?
    - [ ] yksi tai useampi monesta moneen suhde
    - [x] vähintään 2 monimutkaisempaa yhteenvetokyselyä
        - [x] Users who have completed at least 5 plans
        - [x] Streets that are part of 1 or more plans


### To dot ennen loppupalautusta

- [ ] poista kommentoitu koodi
- [ ] Sovelluksen rajoitteet ja puuttuvat ominaisuudet
