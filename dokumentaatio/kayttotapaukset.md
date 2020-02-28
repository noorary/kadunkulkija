# Kadunkulkija - tietokantasovelluksen käyttötapauksia

Sovelluksesta löytyy tavallisia käyttäjiä 'user', sekä ylläpitäjiä 'admin'.

### Käyttäjänä haluan...

#### Toteutetut user storyt

* Rekistöröityä sovellukseen
* Kirjautua sovellukseen
* Tarkastella Helsingin katuja
* Tehdä suunnitelmia katujen vierailua varten
  * Merkata suunnitelman suoritetuksi
  * Muokata suunnitelmaa
  * Poistaa suunnitelman
* Lisätä katuja sovellukseen

#### Vielä toteuttamatta

* Tarkastella tietyn kaupunginosan katuja
* Nähdä kadut joilla olen käynyt
* Hallinnoida käyttäjätiliäni
  * Tarkastella, muokata ja poistaa tietojani

### Ylläpitäjänä haluan...

#### Toteutetut user storyt

* Hallinnoida katuja ja kaupunginosia
  * Muokata katuja
  * Lisätä kaupunginosia
  * Poistaa kaupunkeja


## SQL-kyselyt 

* Rekistöröityminen

```
INSERT INTO account ("date_created", "date_modified", "name", "username", "password", "admin") VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, false);
```

* Helsingin katujen tarkastelu

```
SELECT * FROM street;
```

* Kadun lisääminen

```
INSERT INTO street ("date_created", "date_modified", "name", "district_id") VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?);
```

* Katujen poistaminen

```
DELETE FROM street WHERE street.id = ' + id
'DELETE FROM street_plan WHERE street_id = ' + id
```

* Kadun nimen muokkaaminen
```
UPDATE street SET "date_modified"=CURRENT_TIMESTAMP, "name" = ? WHERE street."id" = ?;
```

* Kaupunginosan lisääminen
```
INSER INTO street ("date_created", "date_modified", "name", "district_id") VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?);
```

* Suunnitelman luominen
```
INSERT INTO plan ("date_created", "date_modified", "plandate", "completed", "street_id", "account_id") VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, false, ?, ?, ?);
```

* Suunnitelmien tarkastelu
```
SELECT * FROM plan LEFT JOIN account ON plan.account_id = account.id WHERE account.id = ?;
```

* Suunnitelman merkkaaminen tehdyksi
```
UPDATE plan SET "date_modified"=CURRENT_TIMESTAMP, "completed" = true WHERE account.id = ?;
```

* Suunnitelman poistaminen
```
DELETE FROM plan WHERE plan."id" = ?;
```






