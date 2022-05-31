from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

# NEW
# GET 'countries/new'
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    continents = continent_repository.select_all()
    return render_template("/countries/new.html", all_continents=continents)

# CREATE
# POST '/countries'
@countries_blueprint.route("/countries", methods =['POST'])
def create_country():
    name = request.form['name']
    continent = continent_repository.select(request.form['continent_id'])
    country = Country(name, continent)
    country_repository.save(country)
    return redirect('/countries')

# SHOW
# GET '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('/countries/show.html', country=country, all_cities=cities)

#EDIT 
#GET 'countries/<id>/edit
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    continents = continent_repository.select_all()
    return render_template('countries/edit.html', country=country, all_cities=cities, all_continents=continents)

# UPDATE
# PUT '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    continent_id= request.form['continent_id']
    visited = bool(int(request.form['visited']))
    continent = continent_repository.select(continent_id)
    country = Country(name, continent, visited, id)
    country_repository.update(country)
    return redirect('/countries')


#DELETE
# DELETE '/countries/<id>'
@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect ('/countries')