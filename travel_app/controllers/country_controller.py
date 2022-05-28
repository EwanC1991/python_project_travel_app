from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

# NEW
# GET 'countries/new'
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    return render_template("/countries/new.html")

# CREATE
# POST '/countries'

# SHOW
# GET '/countries/<id>'

# UPDATE
# PUT '/countries/<id>'

#DELETE
# DELETE '/countries/<id>'