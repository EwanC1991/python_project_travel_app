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

country_repository.select_all()

city1 = City ("Barcelona", country1, False)
city_repository.save(city1)
city2 = City("Paris", country2, True)
city_repository.save(city2)

city_repository.select_all()

pdb.set_trace()
