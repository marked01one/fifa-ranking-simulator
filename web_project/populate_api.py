import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

import django
django.setup()

# POPULATE SCRIPT
from api.models import Country, Confederation
import json


def extract_confederations():
  with open('../seed_data/default_data/confederations.json') as file:
    return json.load(file)
  

def extract_countries():
  with open('../seed_data/default_data/countries.json') as file:
    return json.load(file)



def populate_default(confederations, countries):
  for entry in confederations:
    
    # Create new confederation entry
    confederation = Confederation.objects.get_or_create(name=entry['Name'])[0]
    confederation.save()
    
  for entry in countries:
    country = Country.objects.get_or_create(
      full_name=entry['FullName'],
      fifa_code=entry['FifaCode'],
      flag_url=entry['FlagUrl'],
      confederation=Confederation.objects.get(id=entry['ConfederationId'])
    )[0]
    country.save()
    


if __name__ == '__main__':
  confederations = extract_confederations()
  countries = extract_countries()
  
  populate_default(confederations, countries)
  
  print('Populate complete!')
  
  

