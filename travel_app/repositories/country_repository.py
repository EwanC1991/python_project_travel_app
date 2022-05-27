from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries (name, visited) VALUES (?, ?) RETURNING *"
    values = [country.name, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country