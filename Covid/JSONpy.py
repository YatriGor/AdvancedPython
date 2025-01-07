import os
import glob
import json
import sys
from datetime import datetime

#giving all folder paths
asia_folder = r'adv_python\ LAB4\covid_data\asia'
australia_folder = r'adv_python\LAB4\covid_data\austalia'
europe_folder = r'adv_python\LAB4\covid_data\europe'
n_america_folder = r'adv_python\LAB4\covid_data\nort america'
s_america_folder = r'adv_python\LAB4\covid_data\south america'




json_files_a = glob.glob(os.path.join(asia_folder, '**', '*.json'), recursive=True)
json_files_b = glob.glob(os.path.join(australia_folder, '**', '*.json'), recursive=True)
json_files_c = glob.glob(os.path.join(europe_folder, '**', '*.json'), recursive=True)
json_files_d = glob.glob(os.path.join(n_america_folder, '**', '*.json'), recursive=True)
json_files_e = glob.glob(os.path.join(s_america_folder, '**', '*.json'), recursive=True)

def print_total_cases():
    total_confirmed = 0
    total_deaths = 0
    total_recovered = 0
    total_active=0
    

    # Process JSON files for Asia
    print("Asia:")

    for file in json_files_a:
        with open(file) as f:
            val = json.load(f)
            print("Country:", val['country'])
            
            # Loop through each date's data
            for entry in val["data"]:
                total_confirmed += entry['confirmed_cases']['total']
                total_deaths+= entry['deaths']['total']
                total_recovered+= entry['recovered']['total']
            total_active = total_confirmed - total_recovered - total_deaths
            print("total confirmed cases: ",total_confirmed)
            print("total deaths: ", total_deaths)
            print("total recovered: ", total_recovered)
            print("total active cases: ",total_active)
    print("Austalia:")
    for file in json_files_b:
        with open(file) as f:
            val = json.load(f)
            print("Country:", val['country'])
            
            # Loop through each date's data
            for entry in val["data"]:
                total_confirmed += entry['confirmed_cases']['total']
                total_deaths+= entry['deaths']['total']
                total_recovered+= entry['recovered']['total']
            total_active = total_confirmed - total_recovered - total_deaths
            print("total confirmed cases: ",total_confirmed)
            print("total deaths: ", total_deaths)
            print("total recovered: ", total_recovered)
            print("total active cases: ",total_active)
    print("Europe:")

    for file in json_files_c:
        with open(file) as f:
            val = json.load(f)
            print("Country:", val['country'])
            
            # Loop through each date's data
            for entry in val["data"]:
                total_confirmed += entry['confirmed_cases']['total']
                total_deaths+= entry['deaths']['total']
                total_recovered+= entry['recovered']['total']
            total_active = total_confirmed - total_recovered - total_deaths
            print("total confirmed cases: ",total_confirmed)
            print("total deaths: ", total_deaths)
            print("total recovered: ", total_recovered)
            print("total active cases: ",total_active)
    print("North America:")
    for file in json_files_d:
        with open(file) as f:
            val = json.load(f)
            print("Country:", val['country'])
            
            # Loop through each date's data
            for entry in val["data"]:
                total_confirmed += entry['confirmed_cases']['total']
                total_deaths+= entry['deaths']['total']
                total_recovered+= entry['recovered']['total']
            total_active = total_confirmed - total_recovered - total_deaths
            print("total confirmed cases: ",total_confirmed)
            print("total deaths: ", total_deaths)
            print("total recovered: ", total_recovered)
            print("total active cases: ",total_active)
    print("South America:")
    for file in json_files_e:
        with open(file) as f:
            val = json.load(f)
            print("Country:", val['country'])
            
            # Loop through each date's data
            for entry in val["data"]:
                total_confirmed += entry['confirmed_cases']['total']
                total_deaths+= entry['deaths']['total']
                total_recovered+= entry['recovered']['total']
            total_active = total_confirmed - total_recovered - total_deaths
            print("total confirmed cases: ",total_confirmed)
            print("total deaths: ", total_deaths)
            print("total recovered: ", total_recovered)
            print("total active cases: ",total_active)

def custom_data():
    date = input("enter date you want to go with: ")
    date_obj = datetime.strptime(date,"%d/%m/%Y")
    date = date_obj.strftime("%d-%m-%Y")
    country = input ("enter country: ")
    
    if country == "india" or country == "china":
        folder = asia_folder
    elif country == "australia":
        folder = australia_folder
    elif country == "italy" or country =="germany":
        folder = europe_folder
    elif country == "brazil":
        folder = s_america_folder
    elif country == "usa":
        folder = n_america_folder 
    else :
        sys.exit("country is not in list")
        
    json_file = glob.glob(os.path.join(folder,'**','*.json' ), recursive=True)
    
    for file in json_file:
        with open(file) as f:
            val = json.load(f)
            if val['country'] == country:
                for i in val['data']:
                    
                    if i['date'] == date:

                        print(f"confiremed cases on {date} in country {country} is :",i['confirmed_cases']['total']) 
            
# print_total_cases()    
custom_data()