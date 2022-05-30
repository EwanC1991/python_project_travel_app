from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sights import Sight
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("/sights/index.html", all_sights=sights)

# NEW
# GET 'cities/new'
@sights_blueprint.route("/sights/new", methods=['GET'])
def new_sight():
    cities = city_repository.select_all()
    return render_template("sights/new.html", all_cities=cities)


# CREATE
# POST '/cities'
@sights_blueprint.route("/sights", methods=['POST'])
def create_sight():
    name = request.form['name']
    city = city_repository.select(request.form['city_id'])
    sight = Sight(name, city)
    sight_repository.save(sight)
    return redirect('/sights')

# SHOW
# GET '/cities/<id>'
@sights_blueprint.route("/sights/<id>", methods=['GET'])
def show_sight(id):
    sight = sight_repository.select(id)
    return render_template('sights/show.html', sight=sight)

#EDIT 
#GET 'cities/<id>/edit
@sights_blueprint.route("/sights/<id>/edit", methods=['GET'])
def edit_sight(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template('sights/edit/html', sight=sight, all_cities=cities)
# UPDATE
# PUT '/cities/<id>'
@sights_blueprint.route("/sights/<id>", methods=['POST'])
def update_sight(id):
    name = request.form['name']
    city_id = request.form['city_id']
    visited = bool(int(request.form['visited']))
    city = city_repository.select(city_id)
    sight = Sight(name, city, visited)
    sight_repository.update(sight)
    return redirect ('/sights')

#DELETE
# DELETE '/cities/<id>'

@sights_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sight(id):
    sight_repository.delete(id)
    return redirect ('/sights')