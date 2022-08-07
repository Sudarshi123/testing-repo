
pip install geopy

# location to lat lon
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("peradeniya,kandy, Sri lanka")
print(location.address)

print((location.latitude, location.longitude))

print(location.raw)
#{'place_id': '9167009604', 'type': 'attraction', ...}