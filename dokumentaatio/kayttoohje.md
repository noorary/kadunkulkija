# Käyttöohje

Käyttäjän avatessa sovelluksen osoitteessa [https://kadunkulkija.herokuapp.com/](https://kadunkulkija.herokuapp.com/) käyttäjä ohjataan ensimmäisenä sovelluksen etusivulle. Etusivulla on yleistä tietoa sovelluksesta. Ylänavigointipalkista voi (katsella sovelluksesta löytyviä katuja `List streets`, lisätä kadun `Add a street` (vain kirjautuneet käyttäjät), kirjautua sisään `Login` ja rekistöröidä uuden käyttäjän `Sign up` tai tarkastella tilastoja `Statistics`.
## Rekistöröityminen ja kirjautuminen

Navigaatiopalkin oikeasta reunasta löytyy mahdollisuus kirjautumiseen ja rekisteröitymiseen.

### Kirjautuminen 

Sovellukseen on määritelty kaksi testauskäyttöön soveltuvaa käyttäjätunnusta, yksi tavallinen käyttäjä ja yksi admin käyttäjä.

Käyttäjätyyppi | käyttäjätunnus | salasana
-------------- | -------------- | --------
user           | test           | tester123
admin          | admin          | admin123

### Rekistöröityminen

Halutessasi voit myös luoda sovellukseen oman käyttäjän. Tämä onnistuu klikkaamalla etusivulla `Sign up`ja täyttämällä tiedot lomakkeeseen. Kun uusi käyttäjä on luotu onnistuneesti, uudelleenohjaa sovellus käyttäjän automaattisesti kirjautumissivulle.

### Uloskirjautuminen

Sovelluksesta pääsee kirjautumaan ulos klikkaamalla navigointipalkin oikeasta reunasta `Logout`.

## Katujen listaaminen ja lisääminen

### Katujen listaaminen

Klikkaamalla navigointipalkin `Menu` - valikon `List streets`linkkiä pääsee tarkastelemaan kaikkia sovelllukseen lisättyjä katuja. 

### Katujen lisääminen

Katujen pääsee lisäämään tietokantaan klikkaamalla navigointipalkin `Menu` - valikon `Add a street` linkkiä. Katujen lisääminen vaatii sisäänkirjautumisen ja jos et ole kirjautunut sisään, ohjataan sinut kirjautumissivulle. 

Uuden kadun  saa lisättyä tietokantaan kirjoittamalla tekstikenttään kadun nimen sekä valitsemalla pudotusvalikosta kaupunginosan. Kun tiedot on täytetty paina `Add a new street`painiketta ja katu lisätään tietokantaan. 

Onnistuneen lisäämisen jälkeen käyttäjä ohjataan katujen listaukseen.

## Kaupunginosan lisääminen

Kaupunginosia voivat lisätä vain admin-käyttäjät. Jos kirjautuneella käyttäjällä on admin-oikeudet, löytyy navigointi palkin `Menu` - valikosta `Add a district` linkki. Linkkiä klikkaamalla avautuu näkymä, jossa olevaan lomakkeeseen tulee kirjoittaa kaupunginosan nimi. Klikkaamalla `Add a new district` painiketta kaupunginosa lisätään tietokantaan.

## Omien suunnitelmien tarkastelu ja lisääminen

### Tarkastelu

Kirjautunut käyttäjä löytää navigointivalikosta `My plan`-linkin, josta pääsee tarkastelemaan omia suunnitelmia. Avautuvalla sivulla voi merkata suunnitelman suoritetuksi tai poistaa suunnitelman.

### Uuden suunnitelman lisääminen

Suunnitelmien alta löytyy `Add new plan`-painike, jota klikkaamalla pääsee lisäämään uuden suunnitelman. Suunnitelmaan tulee valita katu, jossa on tarkoitus vierailla sekä suunniteltu päivä. Suunnitelman päivä on oletusarvoisesti suunnitelman luontipäivä. 

### Useamman kadun lisääminen suunnitelmaan

Suunnitelmaan pääsee lisäämään useampia katuja klikkaamalla halutun suunnitelman kohdalta `Add several streets`. Avautuvalta sivulta valitaan lisättävä katu ja katu lisätään suunnitelmaan klikkaamalla `Add more streets to the plan`.

### Tilastojen tarkastelu

Tilastoja pääsee tarkastelemaan klikkaamalla `Statistics`yläpalkista.

## Kadun nimen muokkaaminen

Jos käyttäjällä on admin-oikeudet, pääsee kadun nimeä muokkaamaan menun `Edit street name` -linkistä. Klikkaamalla `Edit <street name>`pääsee antamaan kadulle uuden nimen.

## Kaupunginosien lisääminen tietokantaan

Admin-oikeudellinen käyttäjä voi lisätä kaupunginosia tietokantaan klikkaamalla menusta `Add a district` linkkiä. Käyttäjälle avautuu lomake, johon kaupunginosan nimi kirjoitetaan. Painamalla `Add a new district` -painiketta kaupunginosa lisätään tietokantaan ja käyttäjä ohjataan kaupunginosien listaukseen. 
