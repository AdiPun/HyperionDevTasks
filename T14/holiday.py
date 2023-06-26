# defining functions at the top
def hotel_cost():
    y = num_nights * 70
    print(f"For {num_nights} nights at a hotel it'll be £{y}")
    return y

def plane_cost():
    if city_flight == "A":
        y = 1700
        city = "Bridgetown, Barbados"
        print(f"Your flight to {city} will cost £{y}")
        return y
    if city_flight == "B":
        y = 3060232
        city = "Stoke on Trent, UK"
        print(f"Your flight to {city} will cost £{y}")
        return y
    if city_flight == "C":
        y = 250
        city = "Cagliari, Sardina"
        print(f"Your flight to {city} will cost £{y}")
        return y
    if city_flight == "D":
        y = 1600
        city = "Kathmandu, Nepal"
        print(f"Your flight to {city} will cost £{y}")
        return y

def car_rental():
    y = rental_days * 20
    print(f"For {rental_days} days of car hire it'll be £{y}")
    return y

def holiday_cost():
    y = flight + hotel + car
    print(f"Your total holiday cost is £{y} to {city} for {num_nights} hotel nights and {rental_days} days car hire")

# getting user inputs for city, hotel nights and days car hire
# just running the funtions
# defining an extra set of variables bc you can't call from inside functions
city = ""
city_flight = str(input("What city will you be flying to? Type 'A' 'B' 'C' or 'D'\nA. Bridgetown, Barbados\nB. Stoke on Trent, UK\nC. Cagliari, Sardinia\nD. Kathmandu, Nepal\n").upper())
flight = plane_cost()
num_nights = int(input("How many hotel nights will you need?\n"))
hotel = hotel_cost()
rental_days = int(input("How many days will you need car hire?\n"))
car = car_rental()

holiday_cost()