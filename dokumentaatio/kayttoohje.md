# Käyttöohje

Avatessasi sovelluksen osoitteessa [https://kadunkulkija.herokuapp.com/](https://kadunkulkija.herokuapp.com/) sinut ohjataan ensimmäisenä sovelluksen etusivulle. Etusivulla on yleistä tietoa sovelluksesta. Ylänavigointipalkista voi (1) katsella sovelluksesta löytyviä katuja `List streets`, (2) lisätä kadun `Add a street` (vain kirjautuneet käyttäjät), (3) kirjautua sisään `Login` ja (4) rekistöröidä uuden käyttäjän `Sign up`. 

TÄHÄN KUVA ETUSIVUSTA

## Rekistöröityminen ja kirjautuminen

Navigaatiopalkin oikeasta reunasta löytyy mahdollisuus kirjautumiseen ja rekisteröitymiseen.

### Kirjautuminen 

Sovellukseen on määritelty kaksi testauskäyttöön soveltuvaa käyttäjätunnusta, yksi tavallinen käyttäjä ja yksi admin käyttäjä.

Käyttäjätyyppi | käyttäjätunnus | salasana
-------------- | -------------- | --------
user           | test           | tester123
admin          | admin          | admin123

### Rekistöröityminen

Halutessasi voit myös luoda sovellukseen oman käyttäjän. Tämä onnistuu klikkaamalla etusivulla `Sign up`ja täyttämällä tiedot lomakkeeseen. Kun uusi käyttäjä on luotu onnistuneesti, uudelleenohjaa sovellus sinut automaattisesti kirjautumissivulle.

### Uloskirjautuminen

Sovelluksesta pääsee kirjautumaan ulos klikkaamalla navigointipalkin oikeasta reunasta `Logout`.

## Katujen listaaminen ja lisääminen

### Katujen listaaminen

Klikkaamalla navigointipalkin `List streets`linkkiä pääset tarkastelemaan kaikkia sovelllukseen lisättyjä katuja. 

### Katujen lisääminen

Katujen pääsee lisäämään klikkaamalla navigointipalkin `Add a street` linkkiä. Katujen lisääminen vaatii sisäänkirjautumisen ja jos et ole kirjautunut sisään, ohjataan sinut kirjautumissivulle. 

Saat lisättyä uuden kadun tietokantaan kirjoittamalla tekstikenttään kadun nimen sekä valitsemalla pudotusvalikosta kaupunginosan. Kun tiedot on täytetty paina `Add a new street`painiketta ja katu lisätään tietokantaan. 

## Kaupunginosan lisääminen

Kaupunginosia voivat lisätä vain admin-käyttäjät. Jos kirjautuneella käyttäjällä on admin-oikeudet, löytyy navigointi palkista `Add a district` linkki. Linkkiä klikkaamalla avautuu näkymä, jossa olevaan lomakkeeseen tulee kirjoittaa kaupunginosan nimi. Klikkaamalla `Add a new district` painiketta kaupunginosa lisätään tietokantaan.

## Omien suunnitelmien tarkastelu ja lisääminen

### Tarkastelu

### Uuden suunnitelman lisääminen

### Suunnitelman merkkaaminen suoritetuksi