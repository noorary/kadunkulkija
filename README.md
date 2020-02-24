# Kadunkulkija

## Aineopintojen harjoitustyö: tietokantasovellus, kevät 2020

Tämä sovellus on toteutettu keväällä 2020 Helsingin yliopiston
tietojenkäsittelytieteen kandiohjelman kurssilla Aineopintojen harjoitustyö:
tietokantasovellus.

[Asennusohje](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/asennusohje.md)

[Käyttöohje](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kayttoohje.md)

[Tietorakenteen kuvaus](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kadunkulkija.png)

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


### Sovelluksen rajoitteet ja puuttuvat ominaisuudet

#### Yleiset to-do

- [x] rekistöröitymislomakkeen validiointi
- [x] rekistöröitymislomakkeen virheviestit
- [ ] monesta moneen suhde
    - [ ] suunnitelmaan liittyy useampi katu
- [ ] toinen täysi CRUD

- [ ] sivutus käytössä
     - [ ] edit street name
     - [ ] plans

- [ ] autorisointi

- [ ] "stats" omalle sivulleen 
    - [ ] tulosten sivutus

- [ ] taulujen normalisointi
- [ ] indeksien käyttö
- [ ] SQL virheiden käsittely

- [ ] AChecker
- [ ] Haku käytössä kaduilla

- [ ] koodin kommentointi

- [ ] sivujen asettelut kuntoon

- [ ] salasanat tallennetaan tietokantaan kryptattuna
- [ ] muokkauksessa tieto lomakkeeseen valmiiksi

- [ ] kirjautuminen onnistui - ilmoitus
- [ ] kahta samaa käyttäjänimeä ei voi olla
- [ ] käyttäjä voi muokata omia tietojaan
- [ ] tyylittele sivuja

## TO DO - viikko 6

- [ ] koodikatselmointi

## TO DO - viimeinen viikko

- [ ] demo
- [ ] viimeiset viilaukset
- [ ] loppupalautus

### To dot ennen loppupalautusta

- [ ] poista kommentoitu koodi
- [ ] Sovelluksen rajoitteet ja puuttuvat ominaisuudet

## TO DO - kurssin arvosteluperusteet & muut tärkeät


- [ ] dokumentaatio
    - [x] aiheen kuvaus
    - [x] käyttöohje
    - [x] asennusohje
    - [ ] rajoitteet ja puuttuvat ominaisuudet
    - [x] user storyt
    - [x] user storyjen SQL kyselyt
    - [ ] tietokantarakenteen kuvaus
        - [ ] taulujen normalisointi tarvittaessa / perustelu normalisoinnin puutteelle
        - [x] tietokantakaavio osa dokumentaatiota
        - [x] tietokantakaavio vastaa todellista tietokantaa
        - [x] CREATE TABLE lauseet ja indeksien lisäykset

- [ ] tietokannan toteutus
    - [x] ei sql-injektiomahdollisuuksia
    - [x] isoissa listauksissa sivutus
    - [x] käyttäjien syötteet validioidaan palvelimella
    - [ ] indeksien käyttö
    - [ ] SQL-virheiden käsittely
    - [x] tehokkaat kyselyt
    - [x] monimutkaisempia yhteenvetokyselyitä

- [ ] web-sovellus
    - [x] ei rikkinäisiä linkkejä
    - [x] lomakkeet toimivat järkevillä syötteillä
    - [ ] sovellus toimii myös ei järkevillä syötteillä (validiointi joko palvelimella tai selaimella)
    - [x] tyyli on yhtenäinen ja käyttö tuntuu luontevalta
    - [ ] siistit lomakkeet

- [ ] käytettävyys & saavutettavuus
    - [x] sivut ovat loogisesti rakennetut ja helposti löydettävissä
        - [x] etusivu sovelluksen juuressa
        - [x] järkevä yleisvalikko
    - [x] käyttäjän syötteet validioidaan
    - [ ] virhetilanteissa ymmärrettävät virheviestit
    - [ ] ACheckerin ilmoittamat ongelmat korjattu
    - [ ] sovellus on käytettävä myös isoilla tietomäärillä
        - [ ] tulosten sivutus
        - [ ] hakutoiminnallisuus
    - [x] sovellus on hyödyllinen (käyttötapaukset mahdolliset tehdä)
    - [x] tehokkuus: toivotut asiat voidaan tehdä ilman turhia välivaiheita

- [ ] ylläpidettävyys
    - [x] konfiguraatiot kehitysympäristölle
    - [x] konfiguraatiot tuotantoympäristölle
    - [x] sovellus ei sisällä tuotantoympäristön salasanoja tms
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
