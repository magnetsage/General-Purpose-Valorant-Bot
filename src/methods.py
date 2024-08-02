import requests
import os
from api_modules import obtain_data

# API domain name
domain = 'https://api.henrikdev.xyz'

def get_basic_account_details(username : str, tagline : str):
    # Creates the URL to the API and sends a request
    url = f'{domain}/valorant/v2/account/{str(username)}/{str(tagline)}'
    data, error_message = obtain_data.obtain_api_data(url)

    if error_message != None:
        print(f'Error: {error_message}')
    else:
        print(data['data'])

def get_detailed_account_details(region : str, puuid : str):
    # Creates the URL to the API and sends a request
    url = f'{domain}/valorant/v2/by-puuid/mmr/{region}/{puuid}'
    data, error_message = obtain_data.obtain_api_data(url)

    if error_message != None:
        print(f'Error: {error_message}')
    else:
        print(data['data'])

name = input('Please enter your username: ')
tag = input('Please enter your tagline: ')

get_basic_account_details(name, tag)