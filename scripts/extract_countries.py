# THIS CODE BELOW HAS ALREADY BEEN RUN
import json

def main():
  with open('../SeedData/DefaultData/raw_countries.json', 'r') as file:
    raw_countries_list = json.load(file)['rankings']

  with open("../SeedData/DefaultData/confederations.json", 'r') as file:
    confederations = json.load(file)

  confederations_dict = {
    con['Name']:con['Id'] for con in confederations
  }
  
  out_dict = [
    {
      "Id": country["rankingItem"]["rank"],
      "FullName": country["rankingItem"]["name"],
      "FifaCode": country["rankingItem"]["countryCode"],
      "FlagUrl": country["rankingItem"]["flag"]["src"],
      "ConfederationId": confederations_dict[
        country['tag']['id']
      ]
    } for country in raw_countries_list
  ]
  
  with open("../SeedData/DefaultData/countries.json", 'w') as file:
    json.dump(out_dict, file, indent=2)

if __name__ == '__main__':
  main()