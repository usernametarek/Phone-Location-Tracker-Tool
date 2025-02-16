import requests

phone_number = "+1-212-456-7890" #write your phone number here
api_key = "669e0f3c4641dee9ed4173ff6d363b15"  

api_url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"

response = requests.get(api_url)
data = response.json()

if data["valid"]:
    print("\nPhone Number Location\n")
    print("Country:", data["country_name"])
    print("City:", data["location"])
    print("Carrier:", data["carrier"])
else:
    print("Invalid phone number or API error.")


