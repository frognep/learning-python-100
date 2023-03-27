#nesting a list inside a dictionary + a dictionary inside a dictionary

# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }


#nesting a dictionary inside a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

# printing nested element

travel_log[0]["country"] = "U.S"

print(travel_log)