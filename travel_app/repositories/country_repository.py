from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.continent_repository as continent_repository 

def save(country):
    sql = "INSERT INTO countries (name, continent_id, visited) VALUES (?, ?, ?) RETURNING *"
    values = [country.name, country.continent.id, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        visited = True if row['visited'] == 1 else False
        continent = continent_repository.select(row['continent_id'])
        country = Country(row['name'], continent, visited, row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        visited = True if result['visited'] == 1 else False
        continent = continent_repository.select(result['continent_id'])
        country = Country(result['name'], continent, visited, result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, continent_id, visited) = (?, ?, ?) WHERE id = ?"
    values = [country.name, country.continent.id, country.visited, country.id]
    run_sql(sql, values)

def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = ?"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        visited = True if row['visited'] == 1 else False
        city = City(row['name'], visited, row['country_id'])
        cities.append(city)
    return cities


