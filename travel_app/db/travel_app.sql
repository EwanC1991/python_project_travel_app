PRAGMA  FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;

CREATE TABLE continents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);


CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited BOOLEAN,
    continent_id INTEGER NOT NULL,
        FOREIGN KEY (continent_id)
            REFERENCES continents(id) 
);

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited BOOLEAN,
    country_id INTEGER NOT NULL,
        FOREIGN KEY (country_id)
                REFERENCES countries(id) 
);

CREATE TABLE sights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited BOOLEAN,
    city_id INTEGER NOT NULL,
        FOREIGN KEY (city_id)
            REFERENCES cities(id) ON DELETE CASCADE
);