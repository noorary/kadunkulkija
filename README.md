# Kadunkulkija

## Aineopintojen harjoitustyö: tietokantasovellus, kevät 2020

Tämä sovellus on toteutettu keväällä 2020 Helsingin yliopiston
tietojenkäsittelytieteen kandiohjelman kurssilla Aineopintojen harjoitustyö:
tietokantasovellus.

[Asennusohje](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/asennusohje.md)

[Käyttöohje](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kayttoohje.md)

[Tietokantarakenteen kuvaus](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kadunkulkija.png)

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

![Tietokantakaavio](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kadunkulkija.png?raw=true)

### Sovelluksen rajoitteet ja puuttuvat ominaisuudet

Sovellukseen jäi toteuttamatta indeksien käyttö tietokannassa, sekä sql-virheiden käsittley.

Autorisointi on toteutettu vain osittain. Tietyt osat sovelluksesta ovat kirjautumisen takana, mutta toteuttamatta on käyttäjän autentikointi roolin perusteella. Roolin perusteella kuitenkin määritellään, mitä linkkejä käyttäjälle näytetään.

Osa user storyista on toteuttamatta, niistä voi lähteä liikkeelle jatkokehityksessä. 
