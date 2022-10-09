from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

place=input("Enter city name : ")
location = geolocator.geocode(place)
print(location)