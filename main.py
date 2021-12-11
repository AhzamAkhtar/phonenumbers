import phonenumbers
from test import number
from phonenumbers import geocoder
#number="+917827549899"
ch_nmber = phonenumbers.parse(number, "CH")
print(number, "Is from ", geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("And Carieer name is",carrier.name_for_number(service_number, "en"))