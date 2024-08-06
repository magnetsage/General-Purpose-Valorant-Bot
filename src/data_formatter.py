from api_modules import valorant_api

def get_player_info(name: str, tag: str) -> dict:
    # Makes request to API and returns json data and error message if any
    basic_data, error_message = valorant_api.get_basic_account_details(name, tag)

    # Checks if nothing was returned from the API
    if basic_data != None:
        detailed_data, error_message = valorant_api.get_detailed_account_details(basic_data['data']['region'], basic_data['data']['puuid'])
        print(detailed_data)
    else:
        print('Error: ', error_message  )
    

get_player_info('H00DBYAIR', 'BMWM5')