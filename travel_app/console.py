import pdb
from models.city import City
from models.country import Country
from models.continent import Continent
from models.sights import Sight

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.continent_repository as continent_repository
import repositories.sight_repository as sight_repository

country_repository.delete_all()
city_repository.delete_all()
continent_repository.delete_all()
sight_repository.delete_all()

continent1 = Continent("Europe")
continent_repository.save(continent1)
continent2 = Continent("Africa")
continent_repository.save(continent2)
continent3 = Continent("Asia")
continent_repository.save(continent3)
continent4 = Continent("North America")
continent_repository.save(continent4)
continent5 = Continent("Oceania")
continent_repository.save(continent5)
continent6 = Continent("South America")
continent_repository.save(continent6)
continent7 = Continent("Anartica")
continent_repository.save(continent7)

continent_repository.select_all()

country1 = Country("Spain", continent1, False)
country_repository.save(country1)
country2 = Country("France", continent1, True)
country_repository.save(country2)
country3 = Country("Algeria", continent2, False)
country_repository.save(country3)
country4 = Country("Cameroon", continent2, True)
country_repository.save(country4)
country5 = Country("Ghana", continent2, False)
country_repository.save(country5)
country6 = Country("Nigeria", continent2, True)
country_repository.save(country6)
country7 = Country("China", continent3, False)
country_repository.save(country7)
country8 = Country("India", continent3, True)
country_repository.save(country8)
country9 = Country("Japan", continent3, False)
country_repository.save(country9)
country10 = Country("Canada", continent4, True)
country_repository.save(country10)
country11 = Country("U.S.A", continent4, False)
country_repository.save(country11)
country12 = Country("Mexico", continent4, True)
country_repository.save(country12)
country13 = Country("Fiji", continent5, False)
country_repository.save(country13)
country14 = Country("Australia", continent5, True)
country_repository.save(country14)
country15 = Country("New Zealand", continent5, False)
country_repository.save(country15)
country16 = Country("Brazil", continent6, True)
country_repository.save(country16)
country17 = Country("Argentina", continent6, False)
country_repository.save(country17)
country18 = Country("Paraguay", continent6, True)
country_repository.save(country18)





country_repository.select_all()

city1 = City ("Barcelona", country1, False)
city_repository.save(city1)
city2 = City("Madrid", country1, False)
city_repository.save(city2)
city3= City("Seville", country1, False)
city_repository.save(city3)
city4 = City("Paris", country2, True)
city_repository.save(city4)
city5 = City("Toulouse", country2, True)
city_repository.save(city5)
city6 = City("Nice", country2, True)
city_repository.save(city6)

city_repository.select_all()

sight1 = Sight("Nou Camp", city1)
sight_repository.save(sight1)
sight2 = Sight("Bernabeu Stadium", city2)
sight_repository.save(sight2)
sight3 = Sight("Alcazar of Seville", city3)
sight_repository.save(sight3)
sight4 = Sight("Eiffel Tower", city4, True)
sight_repository.save(sight4)
sight5 = Sight("Basilique Saint-Sernin", city5, True)
sight_repository.save(sight5)
sight6 = Sight("Vieille Ville", city6, True)
sight_repository.save(sight6)

pdb.set_trace()
