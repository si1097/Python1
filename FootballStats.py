import requests

def get_player_stats(player_name):
    # Replace 'YOUR_API_KEY' with your actual API key from Football-Data.org
    api_key = 'c2c8c66ff6ac412a95fe2bfb832c6037'
    
    # Make the API request to retrieve player data
    url = f'https://api.football-data.org/v2/players'
    headers = {'X-Auth-Token': api_key}
    params = {'name': player_name}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    # Extract player information from the API response
    if 'players' in data:
        player = data['players'][0]
        player_id = player['id']
        player_name = player['name']
        
        # Make another API request to get player statistics
        stats_url = f'https://api.football-data.org/v2/players/{player_id}/statistics'
        
        stats_response = requests.get(stats_url, headers=headers)
        if stats_response.status_code == 200:
            stats_data = stats_response.json()
            
            # Extract goals and assists for the 2022/23 season
            for season in stats_data['statistics']:
                if season['season'] == '2022':
                    goals = season['goals']['total']
                    assists = season['goals']['assists']
                    break
            
            # Display the player's goals and assists
            print(f"Player: {player_name}")
            print(f"Goals (2022/23 season): {goals}")
            print(f"Assists (2022/23 season): {assists}")
        else:
            print("Error: Failed to retrieve player statistics.")
    else:
        print(f"Player '{player_name}' not found.")

# Usage example
player_name = input("Enter player name: ")
get_player_stats(player_name)
