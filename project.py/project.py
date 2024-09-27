import os
import requests
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import matplotlib.ticker as ticker

def main():
    api_key = os.getenv("RIOT_API_KEY")
    if not api_key:
        print("Error: Set the RIOT_API_KEY environment available")
        sys.exit(1)

    regions()
    region = input("Enter your region: ").strip().lower()
    gameName = input("Enter your summoner name: ").strip()
    tagLine = input("Enter your Tagline without # symbol: ").strip()

    summoner_data = search_summoner_by_name(region, gameName, tagLine, api_key)
    puuid = get_puuid(summoner_data)

    count = input("Number of matches you wish to consult: ").strip()
    if count.isnumeric():
        count = int(count)
        matchId = get_match_id(region, puuid, api_key, count)
    else:
        print(f"Please enter  valid integer for the number of matches")
        return
    
    placements = []
    damages = []
    for match in matchId:
        match_info = get_match_info(region, match, api_key)
        if match_info:
            placement = get_placement(match_info, puuid)
            placements.append(placement)
            damage = get_damage(match_info, puuid)
            damages.append(damage)
        else:
            print(f"Error. Failed to retrieve match information")
            placements.append(None)
            damages.append(None) 
    
    index = range(1, len(placements) + 1)
    
    p_table = placement_table(index, matchId, placements, damages)

    create_plot(placements, p_table, gameName)

def regions():
    print(f"Please enter your region. It must be one of the following:\n- americas\n- asia\n- europe\n- sea")

def search_summoner_by_name(region, gameName, tagLine, api_key):
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        sys.exit(f"Error retrieving summoner data: {error}")

def get_puuid(summoner_data):
    if summoner_data:
        return summoner_data.get("puuid")
    else:
        return None

def get_match_id(region, puuid, api_key, count=1):
    url = f"https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        sys.exit(f"Error retrieving match ID: {error}")

def get_match_info(region, match, api_key):
    url = f"https://{region}.api.riotgames.com/tft/match/v1/matches/{match}?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        sys.exit(f"Error retrieving match information: {error}")

def get_placement(match_info, puuid):
    participants = match_info.get("info", {}).get("participants", [])
    for participant in participants:
        if participant.get("puuid") == puuid:
            return participant.get("placement")
    return None

def get_damage(match_info, puuid):
    participants = match_info.get("info", {}).get("participants", [])
    for participant in participants:
        if participant.get("puuid") == puuid:
            return participant.get("total_damage_to_players")
    return None

def placement_table(index, matchId, placements, damages):
    data = {
        "Nº": index,
        "Match_ID": matchId,
        "Placement": placements,
        "Total_dmg": damages
    }
    df = pd.DataFrame(data)
    return df

def create_plot(placements, p_table, gameName):
    style.use('ggplot')

    fig1, ax1 = plt.subplots(figsize=(10, 6), layout="constrained")
    matches = range(1, len(placements) + 1)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
  
    ax1.plot(matches, p_table["Placement"], color="blue", marker="o", label="Placement")
    ax1.set_ylim(0, 9)
    ax1.invert_yaxis()
    ax1.set_xlabel("Matches", labelpad=15)
    ax1.set_ylabel("Placement", color="blue", labelpad=15)

    ax2 = ax1.twinx()

    ax2.plot(matches, p_table["Total_dmg"], color="red", marker="o", label="Total_dmg", linestyle="--")
    y_min, y_max = ax2.get_ylim()
    margin = 20
    if y_min < 0:
        ax2.set_ylim(y_min, y_max + margin)
    else:
        ax2.set_ylim(y_min - margin, y_max + margin)
    ax2.set_xlabel("Matches", labelpad=15)
    ax2.set_ylabel("Total dmg", color="red", labelpad=15)

    ax1.set_title(f"Player placement & damage dealt last {len(placements)} games\n Summoner: {gameName}", pad=20)
    ax1.grid(True)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

    num_rows = len(p_table)
    num_cols = len(p_table.columns)
    fig_height = num_rows * 0.2 + 2
    fig_width = num_cols * 2 + 2
    
    fig2, ax3 = plt.subplots(figsize=(fig_width, fig_height), layout="constrained")
    ax3.set_title(f"Player placement & damage dealt last {len(placements)} games\n Summoner: {gameName}", pad=20)
    ax3.xaxis.set_visible(False)
    ax3.yaxis.set_visible(False)
    ax3.set_frame_on(False)
    n_table = ax3.table(cellText=p_table.values, 
                       colLabels=p_table.columns,
                       colColours=["tab:blue"] * len(p_table.columns),
                       cellLoc="center",
                       loc="center")
    return plt.show()

if __name__ == "__main__":
    main()