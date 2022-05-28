import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

country_repository.delete_all()

country1 = Country("Spain", False)
country_repository.save(country1)
country2 = Country("France", True)
country_repository.save(country2)


