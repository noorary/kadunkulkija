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
admin          | admin          | admin123

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

## TO DO - viikko 4

#### Kurssin vaatimukset

- [ ] lomakkeet validioivat syötetyn tiedon
- [x] sovelluksessa on ainakin yksi monimutkaisempi yhteenvetokysely jonka tulokset näytetään käyttäjälle
    - [x] Users who have completed at least 5 plans
- [ ] ei injektiomahdollisuuksia


## TO DO - viikko 5

#### Kurssin vaatimukset

- [ ] autorisointi
- [ ] käytettävyyden viilausta
- [ ] toiminnallisuus on täydentynyt
- [ ] asennusohje
- [ ] käyttöohje

#### Muut

- [ ] kirjautuneelle käyttäjälle linkki omiin suunnitelmiin
- [ ] dropdown valikko navbariin

- [ ] salasanat tallennetaan tietokantaan kryptattuna
- [ ] muokkauksessa tieto lomakkeeseen valmiiksi

- [ ] Katujen listaukseen näkyviin myös kaupungin osa
- [ ] Admin voi poistaa kadun listauksesta
- [ ] Kadun nimeä voi muokata suoraan listauksesta
- [ ] Päivitä tietokantakaavio (admin-rooli)

## TO DO - viikko 6

- [ ] toiminnallisuus on täydentynyt
- [ ] ulkoasu, käytettävyys ja toiminnallisuus
- [ ] dokumentaation päivittäminen ja lisääminen
- [ ] koodikatselmointi

## TO DO - viimeinen viikko

- [ ] demo
- [ ] viimeiset viilaukset
- [ ] loppupalautus

## TO DO - kurssin arvosteluperusteet & muut tärkeät


- [ ] dokumentaatio
    - [ ] aiheen kuvaus
    - [ ] käyttöohje
    - [ ] asennusohje
    - [ ] rajoitteet (??)
    - [ ] puuttuvat ominaisuudet
    - [ ] user storyt
        - [ ] listaus käyttäjäryhmistä ja käyttötapauksista
    - [ ] user storyjen SQL kyselyt
    - [ ] tietokantarakenteen kuvaus
        - [ ] taulujen normalisointi tarvittaessa / perustelu normalisoinnin puutteelle
        - [ ] tietokantakaavio osa dokumentaatiota
        - [ ] tietokantakaavio vastaa todellista tietokantaa
        - [ ] CREATE TABLE lauseet ja indeksien lisäykset

- [ ] tietokannan toteutus
    - [ ] ei sql-injektiomahdollisuuksia
    - [ ] isoissa listauksissa sivutus
    - [ ] käyttäjien syötteet validioidaan palvelimella
    - [ ] indeksien käyttö
    - [ ] SQL-virheiden käsittely
    - [ ] tehokkaat kyselyt
    - [ ] monimutkaisempia yhteenvetokyselyitä

- [ ] web-sovellus
    - [ ] ei rikkinäisiä linkkejä
    - [ ] lomakkeet toimivat järkevillä syötteillä
    - [ ] sovellus toimii myös ei järkevillä syötteillä (validiointi joko palvelimella tai selaimella)
    - [ ] tyyli on yhtenäinen ja käyttä tuntuu luontevalta

- [ ] käytettävyys & saavutettavuus
    - [ ] sivut ovat loogisesti rakennetut ja helposti löydettävissä
        - [x] etusivu sovelluksen juuressa
        - [ ] järkevä yleisvalikko
    - [ ] käyttäjän syötteet validioidaan
    - [ ] virhetilanteissa ymmärrettävät virheviestit
    - [ ] ACheckerin ilmoittamat ongelmat korjattu
    - [ ] sovellus on käytettävä myös isoilla tietomäärillä
        - [ ] tulosten sivutus
        - [ ] hakutoiminnallisuus

- [ ] ylläpidettävyys
    - [ ] konfiguraatiot kehitysympäristölle
    - [ ] konfiguraatiot tuotantoympäristölle
    - [ ] sovellus ei sisällä tuotantoympäristön salasanoja tms
    - [ ] koodin laatu ok
        - [ ] ei copypaste - koodia
        - [ ] ei pois-kommentoitua koodia
    - [ ] sovellus pilkottu selkeisiin luokkiin
    - [ ] koodi on ymmärrettävää
        - [ ] tarpeelliset kohdat kommentoitu

- [ ] arvosana 5 minimivaatimukset
    - [x] vähintään 3 tietokantataulua (+ liitostaulut)
    - [x] käyttäjä liittyy muuhunkin kuin kirjautumiseen (suunnitelmat)
    - [ ] vähintään kahdesta tietokohtaasta täysi CRUD (suunnitelmat, käyttäjän tiedot?)
    - [ ] yksi tai useampi monesta moneen suhde
    - [ ] vähintään 2 monimutkaisempaa yhteenvetokyselyä
        - [x] Users who have completed at least 5 plans
        - [ ] Streets that are part of 1 or more plans


## TO DO - muuta

- [ ] kirjautuminen onnistui - ilmoitus
- [ ] kahta samaa käyttäjänimeä ei voi olla
- [ ] käyttäjä voi muokata omia tietojaan
- [ ] tyylittele sivuja

### Jatkokehitysideoita
