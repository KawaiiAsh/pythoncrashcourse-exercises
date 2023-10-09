def get_city_info(city,country,population = ''):
    if population:
        return city.title() + ", " + country.title() + " - population " + str(population)  
    else:
        return city.title() + ", " + country.title()