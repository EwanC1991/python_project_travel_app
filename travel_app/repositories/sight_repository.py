from db.run_sql import run_sql

from models.sights import Sight

import repositories.city_repository as city_repository

def save(sight):
    sql = "INSERT INTO sights (name, city_id, visited) VALUES (?,?,?)"
    values = [sight.name, sight.city.id, sight.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight

def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        visited = True if row['visited'] == 1 else False
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'], city, visited, row['id'])
        sights.append(sight)
    return sights

def select(id):
    sight = None
    sql = "SELECT * FROM sight WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        visited = True if result['visited'] == 1 else False
        city = city_repository.select(result['city_id'])
        sight = Sight(result['name'], city, visited, result['id'])
    return sight

def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sights WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(sight):
    sql ="UPDATE sights SET (name, city_id, visited) = (?,?,?) WHERE id = ?"
    values = [sight.name, sight.city.id, sight.visited, sight.id]
    run_sql(sql, values)