# Tietokantarakenteen kuvaus

## Tietokantakaavio

![Tietokantakaavio](https://github.com/noorary/kadunkulkija/blob/master/dokumentaatio/kadunkulkija.png?raw=true)

## CREATE TABLE -lauseet

```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        admin BOOLEAN NOT NULL, 
        PRIMARY KEY (id)
);

CREATE TABLE street (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(64) NOT NULL, 
        district_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(district_id) REFERENCES district (id)
);

CREATE TABLE district (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);

CREATE TABLE "plan" (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        plandate VARCHAR(64), 
        completed BOOLEAN NOT NULL, 
        street_id INTEGER NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (completed IN (0, 1)), 
        FOREIGN KEY(street_id) REFERENCES street (id), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```
