from db.run_sql import run_sql

from models.continent import Continent
from models.country import Country

def save(continent):
    sql = "INSERT INTO continents (name) VALUES (?) RETURNING *"
    values = [continent.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    continent.id = id
    return continent

def select_all():
    continents = []

    sql = "SELECT * FROM continents"
    results = run_sql(sql)
    for row in results:
        continent = Continent(row['name'], row['id'])
        continents.append(continent)
    return continents

def select(id):
    continent = None
    sql = "SELECT * FROM continents WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        continent = Continent(result['name'], result['id'])
    return continent

def delete_all():
    sql = "DELETE FROM continents"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM continents WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(continent):
    sql = "UPDATE continents SET (name) = (?) WHERE id = ?"
    values = [continent.name, continent.id]
    run_sql(sql, values)

def countries(continent):
    countries = []

    sql = "SELECT * FROM countries WHERE continent_id = ?"
    values = [continent.id]
    results = run_sql(sql, values)

    for row in results:
        visited = True if row['visited'] == 1 else False
        country = Country(row['name'], row['continent_id'], visited)
        countries.append(country)
    return countries

