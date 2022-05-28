import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()

country1 = Country("Spain", False)
country_repository.save(country1)
country2 = Country("France", True)
country_repository.save(country2)

city1 = City ("Barcelona", False, country1)
city_repository.save(city1)
city2 = City("Paris", True, country2)
city_repository.save(city2)

