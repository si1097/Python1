import os, requests

def get_player_stats(player_name):
    api_key = os.getenv("FOOTBALL_DATA_API_KEY")
    if not api_key:
        raise RuntimeError("Set FOOTBALL_DATA_API_KEY in your environment.")

    # v4 competition scorers for Premier League (code: PL), season 2022 (i.e., 2022/23)
    url = "https://api.football-data.org/v4/competitions/PL/scorers"
    headers = {"X-Auth-Token": api_key}
    params = {"season": 2022, "limit": 200}  # raise limit so your player appears

    r = requests.get(url, headers=headers, params=params, timeout=8)
    r.raise_for_status()
    data = r.json()

    # Find the player in the scorers list by name (case-insensitive)
    scorers = data.get("scorers", [])
    match = next((s for s in scorers if s.get("player", {}).get("name", "").lower() == player_name.lower()), None)

    if not match:
        print(f"Player '{player_name}' not found in Premier League 2022/23 scorers.")
        return

    # Typical shape: match["goals"] and match.get("assists") (field names may vary)
    goals = match.get("goals") or match.get("numberOfGoals")
    assists = match.get("assists") 

    print(f"Player: {match['player']['name']}")
    print(f"Goals (2022/23 season): {goals}")
    print(f"Assists (2022/23 season): {assists if assists is not None else 'N/A'}")


