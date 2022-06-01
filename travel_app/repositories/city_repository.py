from db.run_sql import run_sql

from models.city import City
from models.sights import Sight

import repositories.country_repository as country_repository

def save(city):
    #TELLING SQL THAT I WOULD LIKE TO ENTER SOME VALUES INTO THE CITIES TABLE
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (?, ?, ?) RETURNING *"
    #PRESENTING THE VALUES I WOULD LIKE TO ENTER
    values = [city.name, city.country.id, city.visited]
    #TAKE THE SQL AND VALUES AND ENTER THEM INTO THE RUN_SQL FUNCTION
    results = run_sql(sql, values)
    #LOOK FOR THE ID ASSIGNED TO THE CITY ADDED
    id = results[0]['id']
    #ADD THAT ID TO THE CITY ADDED
    city.id = id
    #RETURN THE CITY WITH ITS NEW ID
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        visited = True if row['visited'] == 1 else False
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, visited, row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        visited = True if result['visited'] == 1 else False
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, visited, result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, visited, country_id) = (?, ?, ?) WHERE id = ?"
    values = [city.name, city.visited, city.country.id, city.id]
    run_sql(sql, values)

def sights(city):
    sights = []

    sql="SELECT * FROM sights WHERE city_id = ?"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        visited = True if row['visited'] == 1 else False
        sight = Sight(row['name'], visited, row['city_id'])
        sights.append(sight)
    return sights