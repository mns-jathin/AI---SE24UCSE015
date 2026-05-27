"""
AI Based Travel Planner
City: New York
"""

PLACES_KB = [

    {
        "name":"Statue of Liberty",
        "category":"history",
        "time":3,
        "cost":25,
        "area":"Lower Manhattan"
    },

    {
        "name":"Times Square",
        "category":"entertainment",
        "time":2,
        "cost":0,
        "area":"Midtown"
    },

    {
        "name":"Central Park",
        "category":"nature",
        "time":3,
        "cost":0,
        "area":"Manhattan"
    },

    {
        "name":"Brooklyn Bridge",
        "category":"landmark",
        "time":2,
        "cost":0,
        "area":"Brooklyn"
    },

    {
        "name":"Empire State Building",
        "category":"landmark",
        "time":2,
        "cost":45,
        "area":"Midtown"
    },

    {
        "name":"Metropolitan Museum",
        "category":"museum",
        "time":4,
        "cost":30,
        "area":"Manhattan"
    }

]


FOOD_KB={

"Lower Manhattan":[
"Bagel",
"Cheesecake"
],

"Midtown":[
"Pizza",
"Hot Dog"
],

"Manhattan":[
"Pancakes",
"Burger"
],

"Brooklyn":[
"Donuts",
"Pretzel"
]

}


DRINK_KB={

"Bagel":"Coffee",
"Cheesecake":"Milkshake",
"Pizza":"Soft Drink",
"Hot Dog":"Lemon Soda",
"Pancakes":"Orange Juice",
"Burger":"Cola",
"Donuts":"Cold Coffee",
"Pretzel":"Milkshake"

}


TRANSPORT_KB={

"budget":"Subway",
"standard":"Subway + Taxi",
"luxury":"Private Cab"

}


DAILY_COST_KB={

"budget":80,
"standard":150,
"luxury":350

}


def score_place(place,user):

    score=0

    if place["category"] in user["interests"]:
        score+=10

    if place["cost"]<=user["max_place_cost"]:
        score+=4

    if place["time"]<=user["max_time_per_place"]:
        score+=3

    if place["area"]==user["preferred_area"]:
        score+=5

    return score


def create_itinerary(user):

    scored=[]

    for place in PLACES_KB:

        score=score_place(
            place,
            user
        )

        scored.append(
            (score,place)
        )

    scored.sort(
        key=lambda x:x[0],
        reverse=True
    )

    selected=[]

    total_time=0

    available=user["days"]*8

    for score,place in scored:

        if total_time+place["time"]<=available:

            selected.append(
                place
            )

            total_time+=place["time"]

    return selected


def recommend_food(places):

    recommendations=[]

    areas=set(
        place["area"]
        for place in places
    )

    for area in areas:

        foods=FOOD_KB.get(
            area,
            []
        )

        for food in foods:

            recommendations.append({

                "food":food,
                "drink":DRINK_KB.get(
                    food,
                    "Local Drink"
                )

            })

    return recommendations


def estimate_budget(
        user,
        places
):

    travel=DAILY_COST_KB[
        user["travel_style"]
    ]*user["days"]

    attraction=sum(

        place["cost"]

        for place in places

    )

    food=40*user["days"]

    total=travel+attraction+food

    return{

        "Travel":travel,
        "Attraction":attraction,
        "Food":food,
        "Total":total

    }


def generate_plan(user):

    places=create_itinerary(
        user
    )

    foods=recommend_food(
        places
    )

    budget=estimate_budget(
        user,
        places
    )

    return{

        "city":"New York",
        "days":user["days"],
        "transport":TRANSPORT_KB[
            user["travel_style"]
        ],
        "places":places,
        "foods":foods,
        "budget":budget
    }


def print_plan(plan):

    print("\nAI TRAVEL PLAN")

    print(
        "City:",
        plan["city"]
    )

    print(
        "Days:",
        plan["days"]
    )

    print(
        "Transport:",
        plan["transport"]
    )

    print("\nPlaces")

    for place in plan["places"]:

        print(
            "-",
            place["name"]
        )

    print(
        "\nFood and Drinks"
    )

    for item in plan["foods"]:

        print(
            "-",
            item["food"],
            "->",
            item["drink"]
        )

    print(
        "\nEstimated Cost"
    )

    for k,v in plan["budget"].items():

        print(
            k,
            ":",
            v
        )


user_profile={

"days":2,

"interests":[
"history",
"nature",
"landmark"
],

"travel_style":"budget",

"preferred_area":"Manhattan",

"max_place_cost":50,

"max_time_per_place":4

}


plan=generate_plan(
    user_profile
)

print_plan(
    plan
)