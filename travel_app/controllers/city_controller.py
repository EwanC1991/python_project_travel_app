from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities=cities)

# NEW
# GET 'cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("/cities/new.html", all_countries=countries)

# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    city = City(name, country)
    city_repository.save(city)
    return redirect('/cities')

# SHOW
# GET '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    sights = sight_repository.select_all()
    return render_template('cities/show.html', city=city, all_sights=sights)

#EDIT 
#GET 'cities/<id>/edit
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city=city, all_countries=countries)


# UPDATE
# PUT '/cities/<id>'
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = bool(int(request.form['visited']))
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect ('/cities')


#DELETE
# DELETE '/cities/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect ('/cities')