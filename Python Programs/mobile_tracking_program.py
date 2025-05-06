import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_number_details(number):
    # Parses the phone number
    phone_number = phonenumbers.parse(number)
    
    # Gets the timezone of the phone number
    time_zones = timezone.time_zones_for_number(phone_number)
    
    # Gets the geolocation of the phone number
    location = geocoder.description_for_number(phone_number, "en")
    
    # Gets the carrier of the phone number
    service_provider = carrier.name_for_number(phone_number, "en")
    
    return time_zones, location, service_provider

if __name__ == "__main__":
    number = input("Enter phone number with country code (e.g., +91XXXXXXXXXX): ")
    time_zones, location, service_provider = get_phone_number_details(number)
    
    print(f"Time Zones: {time_zones}")
    print(f"Location: {location}")
    print(f"Service Provider: {service_provider}")
