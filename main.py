import phonenumbers
from test import number
from phonenumbers import geocoder
countrycode="+91"
lnumber="7827549899"
number=countrycode+lnumber
ch_nmber = phonenumbers.parse(number, "CH")
print(number, "Is from ", geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("And Carieer name is",carrier.name_for_number(service_number, "en"))