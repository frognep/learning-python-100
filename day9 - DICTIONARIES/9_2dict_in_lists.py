travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#tODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, visit_count, cities_names):
  new_list = {
    "country": country_name,
    "visits": visit_count,
    "cities": cities_names,
    }
  travel_log.append(new_list)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# print(travel_log[0]["country"])