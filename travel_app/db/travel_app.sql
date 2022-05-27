PRAGMA  FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited VARCHAR
)

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited VARCHAR,
    country_id INTEGER NOT NULL,
        FOREIGN KEY (country_id)
                REFERENCES countries(id)
)