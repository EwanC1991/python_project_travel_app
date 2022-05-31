from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository
import repositories.sight_repository as sight_repository

continents_blueprint = Blueprint("continents", __name__)

@continents_blueprint.route("/continents")
def continents():
    continents = continent_repository.select_all()
    return render_template("continents/index.html", all_continents=continents)

# SHOW
# GET '/countries/<id>'
@continents_blueprint.route("/continents/<id>", methods=['GET'])
def show_continent(id):
    continent = continent_repository.select(id)
    countries = country_repository.select_all()
    return render_template('/continents/show.html', continent=continent, all_countries=countries)

#SHOW VISITED
@continents_blueprint.route("/visited", methods=['GET'])
def show_all_visited():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    sights = sight_repository.select_all()
    return render_template ('visited.html', all_countries=countries, all_cities=cities, all_sights=sights)


#SHOW UNVISITED
@continents_blueprint.route("/unvisited", methods=['GET'])
def show_all_unvisited():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    sights = sight_repository.select_all()
    return render_template ('unvisited.html', all_countries=countries, all_cities=cities, all_sights=sights)